import streamlit as st

def show_info_page(topic):

    if st.button('← Back to Home'):
        st.session_state.current_page = 'landing'
        st.rerun()

    st.divider()

    if topic == 'quality':
        st.title('Data Quality Scoring')
        st.caption('How the system evaluates your dataset across 4 dimensions')
        st.divider()

        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-left:3px solid #ff6f00; border-radius:6px; padding:1.2rem; margin-bottom:1.5rem;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#ff6f00; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">Overall Score Formula</div>
            <div style="font-family:'DM Mono',monospace; font-size:14px; color:#ffffff;">
                Score = (Completeness × 0.35) + (Validity × 0.25) + (Consistency × 0.25) + (Uniqueness × 0.15)
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.subheader('Completeness — 35% weight')
        st.markdown("""
        Measures how much of your data is present versus missing.
        """)
        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#ff6f00;">
                Completeness = 1 - (missing_cells / total_cells)
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        - A score of **1.0** means no missing values anywhere in the dataset
        - A score of **0.8** means 20% of all cells are empty or null
        - Missing data can introduce bias and reduce model reliability
        - Grade thresholds: A ≥ 0.95, B ≥ 0.85, C ≥ 0.70, D ≥ 0.50, F < 0.50
        """)

        st.subheader('Validity — 25% weight')
        st.markdown("""
        Measures whether values conform to expected rules and constraints.
        """)
        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#ff6f00;">
                Validity = 1 - (invalid_values / total_checked_values)
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Checks numeric columns for impossible values (e.g. age < 0)
        - Checks categorical columns for unexpected categories
        - Each column has rules defined — violations are counted and reported
        """)

        st.subheader('Consistency — 25% weight')
        st.markdown("""
        Measures whether values make logical sense in relation to each other.
        """)
        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#ff6f00;">
                Consistency = 1 - (violated_rules / total_rules_checked)
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Example rule: if age < 18, education should not be a postgraduate degree
        - Example rule: if age < 16, income column should be empty
        - Cross-column logical checks catch real-world impossibilities
        """)

        st.subheader('Uniqueness — 15% weight')
        st.markdown("""
        Measures how many rows are duplicated in the dataset.
        """)
        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#ff6f00;">
                Uniqueness = 1 - (duplicate_rows / total_rows)
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Duplicate rows artificially inflate certain patterns in your data
        - Can cause overfitting in machine learning models
        - A score of 1.0 means every row is unique
        """)

    elif topic == 'fairness':
        st.title('Fairness Audit Metrics')
        st.caption('How the system detects algorithmic bias in your dataset')
        st.divider()

        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-left:3px solid #db1886; border-radius:6px; padding:1.2rem; margin-bottom:1.5rem;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#db1886; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">What is algorithmic bias?</div>
            <div style="font-size:13px; color:#ffffff; line-height:1.7;">
                Algorithmic bias occurs when a dataset or model systematically produces unfair outcomes 
                for certain demographic groups. Protected attributes like gender, race, and age are 
                checked against outcome variables like income or loan approval.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.subheader('Disparate Impact (DI)')
        st.markdown("""
        The ratio of positive outcome rates between an unprivileged group and a privileged group.
        """)
        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#db1886;">
                DI = P(positive outcome | unprivileged) / P(positive outcome | privileged)
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        - **DI ≥ 0.8** — considered fair by the 80% rule (four-fifths rule)
        - **DI < 0.8** — bias detected, unprivileged group receives fewer positive outcomes
        - **DI = 1.0** — perfect equality between groups
        - **DI > 1.0** — unprivileged group actually receives more positive outcomes
        - Example: if 60% of men get high income but only 22% of women do, DI = 0.22/0.60 = 0.36 — UNFAIR
        """)

        st.subheader('Demographic Parity Difference (DPD)')
        st.markdown("""
        The absolute difference in positive outcome rates between groups.
        """)
        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#db1886;">
                DPD = |P(positive | unprivileged) - P(positive | privileged)|
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        - **DPD ≤ 0.1** — considered fair
        - **DPD > 0.1** — meaningful gap exists between groups
        - Unlike DI, this is an absolute difference not a ratio
        - Easier to interpret: a DPD of 0.3 means a 30 percentage point gap
        """)

        st.subheader('Statistical Parity Difference (SPD)')
        st.markdown("""
        Similar to DPD but can be positive or negative, showing direction of bias.
        """)
        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#db1886;">
                SPD = P(positive | unprivileged) - P(positive | privileged)
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        - **|SPD| ≤ 0.1** — considered fair
        - **SPD < 0** — privileged group receives more positive outcomes
        - **SPD > 0** — unprivileged group receives more positive outcomes
        - **SPD = 0** — perfect statistical parity
        """)

    elif topic == 'ai':
        st.title('AI Explanation Engine')
        st.caption('How Claude generates plain English explanations of your audit results')
        st.divider()

        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-left:3px solid #608ec7; border-radius:6px; padding:1.2rem; margin-bottom:1.5rem;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#608ec7; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">Powered by Anthropic Claude</div>
            <div style="font-size:13px; color:#ffffff; line-height:1.7;">
                After running quality scoring and fairness auditing, the system sends the full 
                results to Claude — Anthropic's AI model — which generates a plain English 
                explanation along with 3 concrete action items to improve your dataset.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.subheader('What the AI receives')
        st.markdown("""
        - Overall quality grade and dimension scores
        - Fairness audit results for each protected attribute
        - Disparate Impact, Demographic Parity, and SPD values
        - Dataset statistics (rows, columns, missing data)
        """)

        st.subheader('What the AI produces')
        st.markdown("""
        - **Quality summary** — plain English interpretation of the grade and scores
        - **Fairness analysis** — explanation of which groups are disadvantaged and by how much
        - **3 action items** — specific, prioritised steps to improve data quality and fairness
        """)

        st.subheader('Why plain English matters')
        st.markdown("""
        Statistical fairness metrics like Disparate Impact and SPD are accurate but 
        hard to interpret for non-technical stakeholders. The AI explanation bridges 
        the gap — turning numbers into narratives that anyone can understand and act on.
        """)

        st.subheader('Model used')
        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#608ec7;">
                Model: claude-sonnet-4-20250514
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Anthropic's most capable model for analysis tasks
        - Each explanation call uses approximately 1,000–2,000 tokens
        - Requires a valid ANTHROPIC_API_KEY in your .env file
        """)

    elif topic == 'history':
        st.title('Audit History')
        st.caption('How the system tracks and stores your previous audits')
        st.divider()

        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-left:3px solid #ffffff; border-radius:6px; padding:1.2rem; margin-bottom:1.5rem;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#ffffff; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">Persistent storage</div>
            <div style="font-size:13px; color:#ffffff; line-height:1.7;">
                Every dataset you upload and audit is stored in a SQLite database. 
                You can log back in at any time and retrieve previous results without 
                re-uploading or re-running the audit.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.subheader('What gets stored')
        st.markdown("""
        - Dataset filename, row count, column count
        - Full quality scoring results across all 4 dimensions
        - Fairness audit results for all protected attributes
        - AI explanation text if generated
        - Upload timestamp and user account
        """)

        st.subheader('How to access history')
        st.markdown("""
        - Log in to your account
        - Click **History** in the left sidebar
        - See a table of all previously uploaded datasets
        - Click **View Results** on any row to retrieve the full audit report
        """)

        st.subheader('Data privacy')
        st.markdown("""
        - All data is stored locally on the server running the backend
        - No data is sent externally except to the Anthropic API for AI explanations
        - Each user account only sees their own datasets
        - Logout clears your session but your data remains in the database
        """)