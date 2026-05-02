"""
<<<<<<< HEAD
AI Explanation Engine
- Phase 2: Semantic column analysis via Gemini
- Phase 3: Explanation + remediation plan generation
=======
AI Explanation Engine (FIXED: outcome column consistency)
- Phase 2: Semantic column analysis with proxy variable detection
- Phase 3: Remediation plan generation
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
"""

import os
import time
import logging
import json
import re
<<<<<<< HEAD
from typing import Dict
from dotenv import load_dotenv
=======
from typing import Dict, List
from dotenv import load_dotenv
from google import genai
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4

load_dotenv()
logger = logging.getLogger(__name__)


class AIExplainer:

    def __init__(self):
        api_key = os.environ.get("GOOGLE_API_KEY")

        if not api_key:
<<<<<<< HEAD
            logger.warning("GOOGLE_API_KEY not set. AI explanations will not work.")
            self.client = None
        else:
            from google import genai
            self.client = genai.Client(api_key=api_key)

        self.model = "gemini-2.5-flash"

    def _call_gemini(self, prompt: str) -> str:
        if not self.client:
            return "Explanation unavailable — GOOGLE_API_KEY not set."

=======
            logger.warning("GOOGLE_API_KEY not set.")

        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-2.5-flash"

    def _call_gemini(self, prompt: str) -> str:
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )
<<<<<<< HEAD
                if response and response.text:
                    return response.text.strip()
=======

                if response and response.text:
                    return response.text.strip()

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
                return "Explanation unavailable."

            except Exception as e:
                error_msg = str(e)
<<<<<<< HEAD
                if "429" in error_msg:
                    time.sleep(2)
                    continue
=======

                if "429" in error_msg:
                    time.sleep(2)
                    continue

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
                logger.error(f"Gemini API error: {error_msg}")
                return "Explanation unavailable."

        return "Explanation unavailable."

<<<<<<< HEAD
    # ── Phase 2: Semantic column classification ────────────────────────────────
    def analyze_column_semantics(self, df) -> Dict:
        try:
            if not self.client:
                return self._fallback_column_detection(df)

=======
    # ✅ PHASE 2 — SEMANTIC COLUMN ANALYSIS WITH PROXY DETECTION
    def analyze_column_semantics(self, df) -> Dict:
        """
        PHASE 2: Semantic analysis of columns with proxy variable detection
        
        Returns:
        {
            "protected_attributes": [...],
            "outcome_variables": [...],
            "proxy_variables": [...],
            "legitimate_features": [...],
            "source": "gemini" | "fallback"
        }
        """
        try:
            # Build column summary: name + data type + sample values
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
            column_info = {}
            for col in df.columns:
                sample_values = df[col].dropna().head(10).tolist()
                column_info[col] = {
                    "dtype": str(df[col].dtype),
                    "sample_values": sample_values
                }

            prompt = f"""
You are a fairness auditing expert analyzing a dataset.

<<<<<<< HEAD
Classify each column into EXACTLY ONE of these categories:

1. protected_attributes: demographic/sensitive columns (gender, race, age, religion, disability)
2. outcome_variables: the target/dependent variable being predicted (income, loan_approval, hired) — ONE maximum
3. proxy_variables: columns that INDIRECTLY encode demographic info (zip_code, first_name, neighborhood)
4. legitimate_features: all other columns used for analysis

CRITICAL RULES:
- Look at ACTUAL VALUES not just column names
=======
Your task: Classify each column into EXACTLY ONE of these categories:

1. **protected_attributes**: Columns that contain demographic or sensitive information
   (e.g., gender, race, age, ethnicity, religion, disability status)

2. **outcome_variables**: The target/dependent variable being predicted or analyzed
   (typically binary or categorical labels like income, loan_approval, hired)

3. **proxy_variables**: Columns that INDIRECTLY encode demographic information
   Examples:
   - zip_code (correlates with race due to historical segregation)
   - first_name (can indicate gender or ethnicity)
   - neighborhood (correlates with income/race)
   - education_institution (may correlate with socioeconomic status)

4. **legitimate_features**: All other columns used for analysis
   (education_level, work_hours, job_title, etc.)

CRITICAL RULES:
- Look at ACTUAL VALUES, not just column names
- "vintage" with values [2018, 2019, 2020] → legitimate_feature (wine year)
- "age" with values [25, 34, 19, 42] → protected_attribute (person age)
- zip_code → proxy_variable (encodes race/income)
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
- Only ONE outcome variable maximum
- If unsure, classify as legitimate_feature

Return ONLY valid JSON (no markdown, no backticks):

{{
<<<<<<< HEAD
  "protected_attributes": ["col1"],
  "outcome_variables": ["target_col"],
  "proxy_variables": ["col2"],
  "legitimate_features": ["col3", "col4"]
=======
  "protected_attributes": ["col1", "col2"],
  "outcome_variables": ["target_col"],
  "proxy_variables": ["col3"],
  "legitimate_features": ["col4", "col5"]
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
}}

Dataset columns with samples:
{json.dumps(column_info, indent=2)}
"""

            response_text = self._call_gemini(prompt)
<<<<<<< HEAD
=======

            # Extract JSON from response (handles markdown code blocks)
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
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
<<<<<<< HEAD
            return self._fallback_column_detection(df)

    def _fallback_column_detection(self, df) -> Dict:
        protected_keywords = [
            'gender', 'sex', 'race', 'ethnicity', 'age',
            'religion', 'disability', 'marital', 'nationality', 'caste'
        ]
        protected = []
        legitimate = []

=======
            # Fallback: use simple regex detection
            return self._fallback_column_detection(df)

    def _fallback_column_detection(self, df) -> Dict:
        """
        Fallback when Gemini fails: simple keyword matching
        """
        protected_keywords = ['gender', 'sex', 'race', 'ethnicity', 'age', 
                              'religion', 'disability', 'marital', 'nationality']
        
        protected = []
        legitimate = []
        
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in protected_keywords):
                protected.append(col)
            else:
                legitimate.append(col)
<<<<<<< HEAD

=======
        
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
        return {
            "protected_attributes": protected,
            "outcome_variables": [],
            "proxy_variables": [],
            "legitimate_features": legitimate,
            "source": "fallback"
        }

<<<<<<< HEAD
    # ── Phase 3: Plain-English explanation ────────────────────────────────────
    def explain_quality(self, quality_result: Dict) -> Dict:
        try:
            prompt = f"""
You are a data quality expert. Explain this result in simple terms:

{json.dumps(quality_result, indent=2)}

Give:
1. Summary (2-3 sentences)
2. Key issues
3. 3 actionable improvements
"""
            explanation = self._call_gemini(prompt)
            return {
                "type": "quality_explanation",
                "grade": quality_result.get("overall_grade"),
                "score": quality_result.get("overall_score"),
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
You are a fairness expert. Explain these results in simple terms:

{chr(10).join(findings)}

Give:
1. Summary (2-3 sentences)
2. Real-world impact
3. 3 actionable recommendations
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

    def generate_full_report(self, quality_result: Dict, fairness_result: Dict) -> Dict:
        logger.info("Generating full AI explanation report")
        return {
            "report_type": "full_ai_explanation",
            "quality_summary": self.explain_quality(quality_result),
            "fairness_summary": self.explain_fairness(fairness_result),
        }

    # ── Phase 3: Remediation plan ──────────────────────────────────────────────
    def generate_remediation_plan(self, quality_result: Dict, fairness_result: Dict,
                                   dataset_info: Dict) -> Dict:
        try:
            findings = []

            outcome_column = dataset_info.get("outcome_column")
            if outcome_column:
                findings.append(f"Target outcome column: {outcome_column}")

            if quality_result:
                overall_score = quality_result.get("overall_score", 0)
                findings.append(f"Overall quality score: {overall_score}/100")

                scores = quality_result.get("scores", {})
                if scores.get("completeness", 100) < 95:
                    findings.append(
                        f"Completeness: {scores.get('completeness')}% (missing values detected)"
                    )

            if fairness_result and fairness_result.get("results"):
                if not outcome_column:
                    outcome_column = fairness_result.get("outcome_attribute")

=======
    # ✅ PHASE 3 — REMEDIATION PLAN GENERATION (FIXED: Use stored outcome column)
    def generate_remediation_plan(self, quality_result: Dict, fairness_result: Dict, 
                                   dataset_info: Dict) -> Dict:
        """
        PHASE 3: Generate specific, actionable remediation plan
        
        Args:
            quality_result: Quality analysis results
            fairness_result: Fairness audit results
            dataset_info: Basic dataset info (rows, columns, column_names, outcome_column)
        
        Returns:
            {
                "critical_priority": [...],
                "high_priority": [...],
                "medium_priority": [...],
                "source": "gemini" | "fallback"
            }
        """
        try:
            # Extract key findings for the prompt
            findings = []
            
            # 🔧 FIX: Get outcome column from fairness audit (source of truth)
            outcome_column = dataset_info.get("outcome_column")
            if outcome_column:
                findings.append(f"Target outcome column: {outcome_column}")
            
            # Quality findings
            if quality_result:
                overall_score = quality_result.get("overall_score", 0)
                findings.append(f"Overall quality score: {overall_score}/100")
                
                scores = quality_result.get("scores", {})
                if scores.get("completeness", 100) < 95:
                    findings.append(
                        f"Completeness: {scores.get('completeness')}% "
                        f"(missing values detected)"
                    )
            
            # Fairness findings
            if fairness_result and fairness_result.get("results"):
                # 🔧 FIX: Extract outcome column from fairness_result if not in dataset_info
                if not outcome_column:
                    outcome_column = fairness_result.get("outcome_attribute")
                
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
                for attr, result in fairness_result["results"].items():
                    if isinstance(result, dict):
                        di = result.get("disparate_impact", "N/A")
                        spd = result.get("spd", "N/A")
                        verdict = result.get("verdict", "UNKNOWN")
<<<<<<< HEAD
=======
                        # 🔧 FIX: Use actual outcome column from audit
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
                        actual_outcome = result.get("outcome_attribute", outcome_column)
                        findings.append(
                            f"Fairness - {attr} vs {actual_outcome}: DI={di}, SPD={spd}, verdict={verdict}"
                        )

            if not findings:
                return {
                    "critical_priority": [],
                    "high_priority": [],
                    "medium_priority": [],
                    "source": "no_findings"
                }

            prompt = f"""
You are a data quality and fairness expert providing remediation guidance.

Dataset Info:
- Rows: {dataset_info.get('rows', 'unknown')}
- Columns: {dataset_info.get('columns', 'unknown')}
- Column names: {dataset_info.get('column_names', [])}
<<<<<<< HEAD
- Outcome column: {outcome_column or 'not specified'}
=======
- Outcome column being analyzed: {outcome_column or 'not specified'}
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4

Findings:
{chr(10).join(findings)}

Generate a SPECIFIC remediation plan. Rules:
1. Reference ACTUAL column names from this dataset
2. Reference ACTUAL numbers from the findings
<<<<<<< HEAD
3. Prioritize: CRITICAL (fairness violations) > HIGH (quality issues) > MEDIUM (improvements)
4. Give concrete steps with verification
=======
3. When discussing outcome, reference the actual outcome column: {outcome_column or '[outcome]'}
4. Prioritize: CRITICAL (fairness violations) > HIGH (quality issues) > MEDIUM (improvements)
5. Give concrete steps, not generic advice
6. Each recommendation: what to do + why + verification step
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4

Return ONLY valid JSON (no markdown, no backticks):

{{
  "critical_priority": [
    {{
      "issue": "specific issue with actual column name and number",
      "fix": "concrete action to take",
<<<<<<< HEAD
      "technique": "technique name",
      "verification": "how to confirm it worked"
    }}
  ],
  "high_priority": [],
  "medium_priority": []
=======
      "verification": "how to confirm it worked"
    }}
  ],
  "high_priority": [...],
  "medium_priority": [...]
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
}}
"""

            response_text = self._call_gemini(prompt)
<<<<<<< HEAD
=======

            # Extract JSON
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
            json_match = re.search(r"\{.*\}", response_text, re.DOTALL)
            if not json_match:
                raise ValueError("No JSON in remediation response")

            parsed = json.loads(json_match.group())

            return {
                "critical_priority": parsed.get("critical_priority", []),
                "high_priority": parsed.get("high_priority", []),
                "medium_priority": parsed.get("medium_priority", []),
                "source": "gemini"
            }

        except Exception as e:
<<<<<<< HEAD
            logger.error(f"Remediation plan error: {str(e)}")
=======
            logger.error(f"Remediation plan generation error: {str(e)}")
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
            return {
                "critical_priority": [],
                "high_priority": [],
                "medium_priority": [],
                "source": "fallback",
                "error": str(e)
<<<<<<< HEAD
            }
=======
            }

    # EXISTING METHODS (unchanged)
    def explain_quality(self, quality_result: Dict) -> Dict:
        try:
            prompt = f"""
You are a data quality expert.

Explain this result in simple terms:

{quality_result}

Give:
1. Summary (2-3 sentences)
2. Key issues
3. 3 actionable improvements
"""

            explanation = self._call_gemini(prompt)

            return {
                "type": "quality_explanation",
                "grade": quality_result.get("overall_grade"),
                "score": quality_result.get("overall_score"),
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
You are a fairness expert.

Explain these results in simple terms:

{chr(10).join(findings)}

Give:
1. Summary (2-3 sentences)
2. Real-world impact
3. 3 actionable recommendations
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

    def generate_full_report(self, quality_result: Dict, fairness_result: Dict) -> Dict:
        logger.info("Generating full AI explanation report")

        return {
            "report_type": "full_ai_explanation",
            "quality_summary": self.explain_quality(quality_result),
            "fairness_summary": self.explain_fairness(fairness_result),
        }
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
