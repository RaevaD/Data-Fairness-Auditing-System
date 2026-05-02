import streamlit as st

import streamlit as st

def show_quality_page(BASE_URL):
    st.title('Data Quality Report')
    st.caption(f'Dataset: {st.session_state.dataset_id[:8]}...' if st.session_state.dataset_id else '')
    st.divider()

    if not st.session_state.dataset_id:
        st.warning('No dataset uploaded yet. Go to Upload first.')
        return

    if not st.session_state.quality_result:
        with st.spinner('Fetching quality report...'):
            res = st.session_state.api_session.get(
                f'{BASE_URL}/api/quality/{st.session_state.dataset_id}'
            )
        if res.status_code == 200:
            st.session_state.quality_result = res.json()
        else:
            st.error('Could not fetch quality report.')
            return

    dq = st.session_state.quality_result['data_quality']
    grade = dq['overall_grade']
    score = round(dq['overall_score'] * 100)

    # Coloured grade card
    grade_colours = {'A': '#27ae60', 'B': '#2ecc71', 'C': '#f39c12', 'D': '#e74c3c', 'F': '#c0392b'}
    colour = grade_colours.get(grade, '#888')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div style="background:#1e1e2e; border:1px solid {colour}; border-radius:10px; padding:1.2rem; text-align:center">
            <div style="font-size:2.5rem; font-weight:700; color:{colour}">{grade}</div>
            <div style="font-size:0.8rem; color:#888; margin-top:4px">Overall Grade</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.metric('Overall Score', f'{score}%')
    with col3:
        st.metric('Status', 'Analysed')

    st.divider()
    st.subheader('Dimension Breakdown')

    st.write('**Completeness** — 35% weight')
    st.progress(dq['completeness']['score'])
    st.caption(f"{round(dq['completeness']['score']*100)}% — {dq['completeness']['missing_cells']} missing cells")

    st.write('**Validity** — 25% weight')
    st.progress(dq['validity']['score'])
    st.caption(f"{round(dq['validity']['score']*100)}% — {dq['validity']['total_invalid']} invalid values")

    st.write('**Consistency** — 25% weight')
    st.progress(dq['consistency']['score'])
    st.caption(f"{round(dq['consistency']['score']*100)}% — {dq['consistency']['n_violations']} violations")

    st.write('**Uniqueness** — 15% weight')
    st.progress(dq['uniqueness']['score'])
    st.caption(f"{round(dq['uniqueness']['score']*100)}% — {dq['uniqueness']['duplicate_rows']} duplicate rows")

    st.divider()
    if grade in ['A', 'B']:
        st.info(dq['recommendation'])
    else:
        st.warning(dq['recommendation'])

    # --- Fairness Audit Section ---
    st.divider()
    st.subheader('Run Fairness Audit')

    audit_allowed = st.session_state.quality_result.get('audit_allowed', False)
    detected_attrs = st.session_state.quality_result.get('detected_attributes', [])

    # Outcome column: pre-fill from semantic analysis, allow override
    semantic = st.session_state.get('semantic_analysis') or {}
    all_columns = list(st.session_state.quality_result.get('data_quality', {}).get('columns', [])) or []
    
    # Try to get columns from stats_report if available
    default_outcome = st.session_state.get('outcome_column') or ''

    outcome_input = st.text_input(
        'Outcome column',
        value=default_outcome,
        help='The column to measure fairness against (e.g. income, hired, loan_approved).'
    )

    # Protected attributes — pre-fill from detection, allow override
    if not audit_allowed:
        st.warning('No protected attributes were auto-detected. Enter them manually below (comma-separated) to proceed.')
        manual_attrs_input = st.text_input(
            'Protected attributes (comma-separated)',
            placeholder='e.g. sex, race, age'
        )
        protected_attrs = [a.strip() for a in manual_attrs_input.split(',') if a.strip()] if manual_attrs_input else []
    else:
        st.info(f"Auto-detected protected attributes: **{', '.join(detected_attrs)}**")
        override_input = st.text_input(
            'Override protected attributes (optional, comma-separated)',
            placeholder='Leave blank to use auto-detected',
            value=''
        )
        protected_attrs = [a.strip() for a in override_input.split(',') if a.strip()] if override_input else detected_attrs

    can_run = bool(outcome_input) and bool(protected_attrs)

    if st.button('Run Fairness Audit →', disabled=not can_run):
        dataset_id = st.session_state.dataset_id
        with st.spinner('Running fairness audit...'):
            payload = {
                'dataset_id': dataset_id,
                'outcome_column': outcome_input,
                'protected_attributes': protected_attrs
            }
            res = st.session_state.api_session.post(
                f'{BASE_URL}/api/audit',
                json=payload
            )
        if res.status_code == 200:
            st.session_state.fairness_result = res.json()
            st.session_state.outcome_column = outcome_input
            st.success('Audit complete! Go to Fairness Report in the sidebar.')
        else:
            err = res.json()
            st.error(f'Fairness audit failed: {err.get("error", "Unknown error")}')
            if 'available_columns' in err:
                st.info(f"Available columns: {', '.join(err['available_columns'])}")
            if 'next_step' in err:
                st.info(f"Required next step: {err['next_step']}")