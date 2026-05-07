import os
import time
import logging
import json
import re
from typing import Dict
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


class AIExplainer:

    def __init__(self):
        api_key = os.environ.get("GOOGLE_API_KEY")

        if not api_key:
            logger.warning("GOOGLE_API_KEY not set. AI explanations will not work.")
            self.client = None
        else:
            from google import genai
            self.client = genai.Client(api_key=api_key)

        self.model = "gemini-2.5-flash"

    def _call_gemini(self, prompt: str) -> str:
        if not self.client:
            return "Explanation unavailable — GOOGLE_API_KEY not set."

        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )
                if response and response.text:
                    return response.text.strip()
                return "Explanation unavailable."

            except Exception as e:
                error_msg = str(e)
                if "429" in error_msg:
                    time.sleep(2)
                    continue
                logger.error(f"Gemini API error: {error_msg}")
                return "Explanation unavailable."

        return "Explanation unavailable."

    def _redact_scores_from_dict(self, data: Dict) -> str:
        """Convert dict to string with numerical scores replaced"""
        redacted = data.copy()

        def recurse_redact(obj):
            if isinstance(obj, dict):
                return {
                    k: recurse_redact(v)
                    for k, v in obj.items()
                    if k not in ['overall_score', 'scores', 'overall_grade']
                }
            elif isinstance(obj, (int, float)):
                return "[redacted]"
            elif isinstance(obj, list):
                return [recurse_redact(item) for item in obj]
            return obj

        return json.dumps(recurse_redact(redacted), indent=2)

    def _sanitize_explanation_text(self, text: str) -> str:
        """Remove numerical scores from explanation text"""
        text = re.sub(r'\b\d+(\.\d+)?/100\b', '', text)
        text = re.sub(r'\bscore:\s*\d+(\.\d+)?%?\b', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\b\d+(\.\d+)?%\b', '', text)
        text = re.sub(
            r'\boverall score[:\s]+\d+(\.\d+)?\b',
            '',
            text,
            flags=re.IGNORECASE
        )
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    # ── Phase 2: Semantic column classification ────────────────────────────────
    def analyze_column_semantics(self, df) -> Dict:
        try:
            if not self.client:
                return self._fallback_column_detection(df)

            column_info = {}

            for col in df.columns:
                sample_values = df[col].dropna().head(10).tolist()
                column_info[col] = {
                    "dtype": str(df[col].dtype),
                    "sample_values": sample_values
                }

            prompt = f"""
You are a fairness auditing expert analyzing a dataset.

Classify each column into EXACTLY ONE of these categories:

1. protected_attributes: demographic/sensitive columns (gender, race, age, religion, disability)
2. outcome_variables: the target/dependent variable being predicted (income, loan_approval, hired) — ONE maximum
3. proxy_variables: columns that INDIRECTLY encode demographic info (zip_code, first_name, neighborhood)
4. legitimate_features: all other columns used for analysis

CRITICAL RULES:
- Look at ACTUAL VALUES not just column names
- Only ONE outcome variable maximum
- If unsure, classify as legitimate_feature

Return ONLY valid JSON (no markdown, no backticks):

{{
  "protected_attributes": ["col1"],
  "outcome_variables": ["target_col"],
  "proxy_variables": ["col2"],
  "legitimate_features": ["col3", "col4"]
}}

Dataset columns with samples:
{json.dumps(column_info, indent=2)}
"""

            response_text = self._call_gemini(prompt)
            json_match = re.search(r"\{.*\}", response_text, re.DOTALL)

            if not json_match:
                raise ValueError("No JSON found in Gemini response")

            parsed = json.loads(json_match.group())

            return {
                "protected_attributes": parsed.get("protected_attributes", []),
                "outcome_variables": parsed.get("outcome_variables", []),
                "proxy_variables": parsed.get("proxy_variables", []),
                "legitimate_features": parsed.get("legitimate_features", []),
                "source": "gemini"
            }

        except Exception as e:
            logger.error(f"Semantic analysis error: {str(e)}")
            return self._fallback_column_detection(df)

    def _fallback_column_detection(self, df) -> Dict:
        protected_keywords = [
            'gender', 'sex', 'race', 'ethnicity', 'age',
            'religion', 'disability', 'marital', 'nationality', 'caste'
        ]

        protected = []
        legitimate = []

        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in protected_keywords):
                protected.append(col)
            else:
                legitimate.append(col)

        return {
            "protected_attributes": protected,
            "outcome_variables": [],
            "proxy_variables": [],
            "legitimate_features": legitimate,
            "source": "fallback"
        }

    # ── Phase 3: Plain-English explanation ────────────────────────────────────
    def explain_quality(self, quality_result: Dict) -> Dict:
        try:
            prompt = f"""
You are a data quality expert. Explain this result in simple, qualitative terms for a non-technical audience.

STRICT FORMATTING RULES — follow exactly or the output will break:
- DO NOT use any ** bold markers anywhere — not around labels, not around words, nowhere
- DO NOT use any # heading markers — not ## Summary, not # anything
- DO NOT add any preamble or intro sentence before the first item
- DO NOT mention any numerical scores, percentages, or grades
- Use ONLY qualitative language: "severe issues", "poor quality", "good quality", etc.

Analysis findings (numerical scores redacted):
{self._redact_scores_from_dict(quality_result)}

Respond using EXACTLY this plain-text structure with no markdown whatsoever:

Summary:
2-3 plain sentences describing the overall data quality. No numbers.

Key Issues:
1. Issue name: Description of the issue and its real-world impact on data reliability.
2. Issue name: Description of the issue and its real-world impact on data reliability.
3. Issue name: Description of the issue and its real-world impact on data reliability.

Recommended Actions:
1. Action title: Specific concrete step to address the most critical issue.
2. Action title: Specific concrete step to address the second issue.
3. Action title: Specific concrete step to address the third issue.
"""

            explanation = self._call_gemini(prompt)
            explanation = self._sanitize_explanation_text(explanation)

            return {
                "type": "quality_explanation",
                "explanation": explanation,
            }

        except Exception as e:
            return {
                "type": "quality_explanation",
                "explanation": "Explanation unavailable.",
                "error": str(e),
            }

    def explain_fairness(self, fairness_result: Dict) -> Dict:
        try:
            if not fairness_result:
                return {
                    "type": "fairness_explanation",
                    "explanation": "No fairness results available."
                }

            results = fairness_result.get("results", {})
            findings = []

            for attr, result in results.items():
                if not isinstance(result, dict):
                    continue
                findings.append(
                    f"{attr}: {result.get('verdict')} | "
                    f"DI={result.get('disparate_impact')} | "
                    f"SPD={result.get('spd')}"
                )

            if not findings:
                return {
                    "type": "fairness_explanation",
                    "explanation": "No fairness results available."
                }

            prompt = f"""
You are a fairness expert. Explain these audit results in simple, clear terms for a non-technical audience.

CRITICAL RULES:
- Use plain language — no jargon without explanation
- DO NOT add any preamble, intro sentence, or conversational filler before the first heading
- Start your response DIRECTLY with "## Summary" — no text before it
- Use **bold** for emphasis within sentences (e.g. group names, key terms) — do NOT use bold for entire sentences
- Do NOT wrap verdict words like UNFAIR or FAIR in double asterisks — write them plainly

Findings:
{chr(10).join(findings)}

Respond using EXACTLY this markdown structure — no deviations, no extra sections:

## Summary
2-3 sentences summarising whether the dataset is fair or biased, which attributes are affected, and what the overall verdict means in plain terms.

## Real-World Impact
1. **Group or attribute affected:** Explain in plain terms what this bias means for real people — what outcomes are affected and who is disadvantaged.
2. **Group or attribute affected:** Explain in plain terms what this bias means for real people — what outcomes are affected and who is disadvantaged.

## Recommended Actions
1. **Action title:** Concrete step to reduce bias for the most affected group.
2. **Action title:** Concrete step to reduce bias for the second issue.
3. **Action title:** Concrete step to improve overall fairness of the dataset or model.
"""

            explanation = self._call_gemini(prompt)

            return {
                "type": "fairness_explanation",
                "explanation": explanation,
            }

        except Exception as e:
            return {
                "type": "fairness_explanation",
                "explanation": "Explanation unavailable.",
                "error": str(e),
            }

    def generate_full_report(
        self,
        quality_result: Dict,
        fairness_result: Dict
    ) -> Dict:

        logger.info("Generating full AI explanation report")

        return {
            "report_type": "full_ai_explanation",
            "quality_summary": self.explain_quality(quality_result),
            "fairness_summary": self.explain_fairness(fairness_result),
        }
