import streamlit as st

def show_info_page(topic):
    if st.button('← Back'):
        st.session_state.current_page = 'landing'
        st.rerun()

    st.divider()

    if topic == 'quality':
        st.title('Data Quality Scoring')
        st.caption('How the system evaluates your dataset across 4 dimensions')
        st.divider()

        st.markdown("""
        <div style="background:#0e0c2e; border:0.5px solid #2a2560; border-left:3px solid #7f77dd; border-radius:0 6px 6px 0; padding:1.2rem; margin-bottom:1.5rem;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#7f77dd; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">Overall Score Formula</div>
            <div style="font-family:'DM Mono',monospace; font-size:14px; color:#e8e0ff;">
                Score = (Completeness × 0.35) + (Validity × 0.25) + (Consistency × 0.25) + (Uniqueness × 0.15)
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.subheader('Completeness — 35% weight')
        st.markdown('Measures how much of your data is present versus missing.')
        st.markdown("""
        <div style="background:#0e0c2e; border:0.5px solid #2a2560; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#afa9ec;">Completeness = 1 - (missing_cells / total_cells)</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
- Score of **1.0** = no missing values anywhere
- Score of **0.8** = 20% of all cells are empty
- Missing data can introduce bias and reduce model reliability
- Grades: A ≥ 0.95, B ≥ 0.85, C ≥ 0.70, D ≥ 0.50, F < 0.50
        """)

        st.subheader('Validity — 25% weight')
        st.markdown('Measures whether values conform to expected rules and constraints.')
        st.markdown("""
        <div style="background:#0e0c2e; border:0.5px solid #2a2560; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#afa9ec;">Validity = 1 - (invalid_values / total_checked_values)</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
- Checks numeric columns for impossible values (e.g. age < 0)
- Checks categorical columns for unexpected categories
- Each column has rules defined — violations are counted and reported
        """)

        st.subheader('Consistency — 25% weight')
        st.markdown('Measures whether values make logical sense in relation to each other.')
        st.markdown("""
        <div style="background:#0e0c2e; border:0.5px solid #2a2560; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#afa9ec;">Consistency = 1 - (violated_rules / total_rules_checked)</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
- Example: if age < 18, education should not be postgraduate
- Example: if age < 16, income column should be empty
- Cross-column logical checks catch real-world impossibilities
        """)

        st.subheader('Uniqueness — 15% weight')
        st.markdown('Measures how many rows are duplicated in the dataset.')
        st.markdown("""
        <div style="background:#0e0c2e; border:0.5px solid #2a2560; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#afa9ec;">Uniqueness = 1 - (duplicate_rows / total_rows)</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
- Duplicate rows inflate certain patterns and can cause overfitting
- Score of 1.0 means every row is unique
        """)

    elif topic == 'fairness':
        st.title('Fairness Audit Metrics')
        st.caption('How the system detects algorithmic bias in your dataset')
        st.divider()

        st.markdown("""
        <div style="background:#061a14; border:0.5px solid #0f3d30; border-left:3px solid #1d9e75; border-radius:0 6px 6px 0; padding:1.2rem; margin-bottom:1.5rem;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#1d9e75; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">What is algorithmic bias?</div>
            <div style="font-size:13px; color:#e8e0ff; line-height:1.7;">
                Algorithmic bias occurs when a dataset or model systematically produces unfair outcomes
                for certain demographic groups. Protected attributes like gender, race, and age are
                checked against outcome variables like income or loan approval.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.subheader('Disparate Impact (DI)')
        st.markdown('Ratio of positive outcome rates between unprivileged and privileged groups.')
        st.markdown("""
        <div style="background:#061a14; border:0.5px solid #0f3d30; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#5dcaa5;">DI = P(positive outcome | unprivileged) / P(positive outcome | privileged)</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
- **DI ≥ 0.8** — fair (80% / four-fifths rule)
- **DI < 0.8** — bias detected against unprivileged group
- **DI = 1.0** — perfect equality
- Example: 60% of men vs 22% of women get high income → DI = 0.36 → UNFAIR
        """)

        st.subheader('Demographic Parity Difference (DPD)')
        st.markdown('Absolute difference in positive outcome rates between groups.')
        st.markdown("""
        <div style="background:#061a14; border:0.5px solid #0f3d30; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#5dcaa5;">DPD = |P(positive | unprivileged) - P(positive | privileged)|</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
- **DPD ≤ 0.1** — fair
- **DPD > 0.1** — meaningful gap exists between groups
- A DPD of 0.3 means a 30 percentage point gap
        """)

        st.subheader('Statistical Parity Difference (SPD)')
        st.markdown('Like DPD but signed — shows the direction of bias.')
        st.markdown("""
        <div style="background:#061a14; border:0.5px solid #0f3d30; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#5dcaa5;">SPD = P(positive | unprivileged) - P(positive | privileged)</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
- **|SPD| ≤ 0.1** — fair
- **SPD < 0** — privileged group gets more positive outcomes
- **SPD = 0** — perfect statistical parity
        """)

    elif topic == 'ai':
        st.title('AI Explanation Engine')
        st.caption('How the AI generates plain English explanations of your audit results')
        st.divider()

        st.markdown("""
        <div style="background:#0e0c2e; border:0.5px solid #2a2560; border-left:3px solid #5dcaa5; border-radius:0 6px 6px 0; padding:1.2rem; margin-bottom:1.5rem;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#5dcaa5; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">AI-Powered Explanations</div>
            <div style="font-size:13px; color:#e8e0ff; line-height:1.7;">
                After running quality scoring and fairness auditing, the system sends the results
                to an AI model which generates a plain English explanation and a prioritised remediation
                plan grouped by severity.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.subheader('What the AI receives')
        st.markdown("""
- Overall quality grade and dimension scores
- Fairness audit results for each protected attribute
- DI, DPD, and SPD values
- Dataset statistics (rows, columns, missing data)
        """)

        st.subheader('What the AI produces')
        st.markdown("""
- **Quality summary** — plain English interpretation of grades and scores
- **Fairness analysis** — which groups are disadvantaged and by how much
- **Remediation plan** — Critical / High / Medium priority action items with techniques and verification steps
        """)

        st.subheader('Model used')
        st.markdown("""
        <div style="background:#0e0c2e; border:0.5px solid #2a2560; border-radius:6px; padding:1rem; margin:0.5rem 0 1rem;">
            <div style="font-family:'DM Mono',monospace; font-size:13px; color:#5dcaa5;">Requires a valid API key in your .env file</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
- Upload step and explain step both call the AI — expect 5–15 seconds each
- Each explanation uses approximately 1,000–2,000 tokens
        """)

    elif topic == 'history':
        st.title('Audit History')
        st.caption('How the system tracks and stores your previous audits')
        st.divider()

        st.markdown("""
        <div style="background:#0e0c2e; border:0.5px solid #2a2560; border-left:3px solid #afa9ec; border-radius:0 6px 6px 0; padding:1.2rem; margin-bottom:1.5rem;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#afa9ec; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">Persistent storage</div>
            <div style="font-size:13px; color:#e8e0ff; line-height:1.7;">
                Every dataset you upload and audit is stored in a SQLite database.
                Log back in at any time to retrieve previous results without re-uploading.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.subheader('What gets stored')
        st.markdown("""
- Dataset filename, row/column count
- Full quality scoring results across all 4 dimensions
- Fairness audit results for all protected attributes
- AI explanation and remediation plan if generated
- Upload timestamp and user account
        """)

        st.subheader('How to access history')
        st.markdown("""
- Log in to your account
- Click **History** in the left sidebar
- See all previously uploaded datasets
- Click **View Results** on any row to retrieve the full report
        """)