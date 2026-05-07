import streamlit as st

def show_quality_page(BASE_URL):
    if not st.session_state.dataset_id:
        st.warning('No dataset uploaded yet. Go to Upload first.')
        return

    if 'quality_result' not in st.session_state:
       st.session_state.quality_result = None

    if st.session_state.quality_result is None:
        with st.spinner('Fetching quality report...'):
            headers = {}
            if st.session_state.get('token'):
                headers['Authorization'] = f'Bearer {st.session_state.token}'
            res = st.session_state.api_session.get(
                f'{BASE_URL}/api/quality/{st.session_state.dataset_id}',
                headers=headers
            )
        if res.status_code == 200:
            st.session_state.quality_result = res.json()
        else:
            st.error(f'Could not fetch quality report. Status: {res.status_code}')
            return

    dq = st.session_state.quality_result['data_quality']
    grade = dq['overall_grade']
    score = round(dq['overall_score'] * 100)
    
    # 🔄 Refresh Button (FORCE REFETCH + UI UPDATE)
    if st.button("🔄 Refresh Quality"):
       st.session_state.quality_result = None
       st.rerun()

    def score_color(s):
        if s >= 90: return '#1d9e75'
        if s >= 70: return '#ef9f27'
        return '#e24b4a'

    def score_glow(s):
        if s == 100: return f'text-shadow: 0 0 12px {score_color(s)}55;'
        return ''

    grade_colours = {
        'A': '#1d9e75', 'B': '#5dcaa5',
        'C': '#ef9f27', 'D': '#e24b4a', 'F': '#a32d2d'
    }
    ring_col = grade_colours.get(grade, '#7f77dd')

    upload_stats = st.session_state.get('upload_stats', {})
    rows = upload_stats.get('total_rows', '—')
    cols = upload_stats.get('total_columns', '—')

    st.markdown(f"""
    <style>
    @keyframes fillBar {{
        from {{ width: 0%; }}
        to {{ width: var(--target-width); }}
    }}
    .dim-bar-track {{
        height: 9px;
        background: #1a1a2e;
        border-radius: 5px;
        overflow: hidden;
        margin: 10px 0 6px;
    }}
    .dim-bar-fill {{
        height: 100%;
        border-radius: 5px;
        animation: fillBar 1.1s ease-in-out forwards;
    }}
    </style>

    <div style="display:flex; align-items:center; gap:24px; padding:1.2rem 0 0.8rem;">
        <div style="width:88px; height:88px; border-radius:50%;
                    border:2.5px solid {ring_col};
                    background: {ring_col}18;
                    display:flex; flex-direction:column; align-items:center;
                    justify-content:center; flex-shrink:0;">
            <span style="font-size:2.2rem; font-weight:600; color:{ring_col};
                         {score_glow(score)}">{grade}</span>
            <span style="font-size:10px; color:#666; margin-top:-3px; letter-spacing:0.5px;">grade</span>
        </div>
        <div>
            <div style="font-size:1.5rem; font-weight:600; color:#e8e0ff; letter-spacing:-0.5px;">
                Data Quality Report
            </div>
            <div style="font-size:12px; color:#7f77dd; font-family:'DM Mono',monospace; margin-top:4px;">
                dataset: {st.session_state.dataset_id[:8]}...
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    sc = score_color(score)
    st.markdown(f"""
    <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin:18px 0;">
        <div style="background:linear-gradient(135deg,#12103a,#1a1640);
                    border:0.5px solid #2a2560; border-radius:12px; padding:20px; text-align:center;">
            <div style="font-size:2.2rem; font-weight:600; color:{sc};
                        {score_glow(score)}">{score}%</div>
            <div style="font-size:13px; color:#888; margin-top:5px; letter-spacing:0.3px;">overall score</div>
        </div>
        <div style="background:linear-gradient(135deg,#0a1f1a,#0d2420);
                    border:0.5px solid #0f3d30; border-radius:12px; padding:20px; text-align:center;">
            <div style="font-size:2.2rem; font-weight:600; color:#1d9e75;">{rows}</div>
            <div style="font-size:13px; color:#888; margin-top:5px; letter-spacing:0.3px;">rows</div>
        </div>
        <div style="background:linear-gradient(135deg,#0a1f1a,#0d2420);
                    border:0.5px solid #0f3d30; border-radius:12px; padding:20px; text-align:center;">
            <div style="font-size:2.2rem; font-weight:600; color:#5dcaa5;">{cols}</div>
            <div style="font-size:13px; color:#888; margin-top:5px; letter-spacing:0.3px;">columns</div>
        </div>
    </div>

    <div style="font-size:12px; font-weight:600; color:#7f77dd; text-transform:uppercase;
                letter-spacing:1.2px; margin:20px 0 14px;">dimension breakdown</div>
    """, unsafe_allow_html=True)

    dimensions = [
        ('Completeness', '35% weight', dq['completeness']['score'],
         f"{dq['completeness']['missing_cells']} missing cells", '#7f77dd', '#12103a', '#2a2560'),
        ('Validity', '25% weight', dq['validity']['score'],
         f"{dq['validity']['total_invalid']} invalid values", '#1d9e75', '#0a1f1a', '#0f3d30'),
        ('Consistency', '25% weight', dq['consistency']['score'],
         f"{dq['consistency']['n_violations']} violations", '#5dcaa5', '#0e0c2e', '#1e1a50'),
        ('Uniqueness', '15% weight', dq['uniqueness']['score'],
         f"{dq['uniqueness']['duplicate_rows']} duplicate rows", '#afa9ec', '#061a14', '#0a2e22'),
    ]

    for name, weight, raw_score, detail, bar_col, bg_col, border_col in dimensions:
        pct = round(raw_score * 100) if raw_score <= 1 else round(raw_score)
        fill = min(pct, 100)
        col = score_color(pct)
        glow = score_glow(pct)
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,{bg_col},{bg_col}ee);
                    border:0.5px solid {border_col}; border-radius:12px;
                    padding:18px 22px; margin-bottom:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <div>
                    <span style="font-size:15px; font-weight:600; color:#e8e0ff;">{name}</span>
                    <span style="font-size:12px; font-weight:400; color:#444;
                                 margin-left:10px;">— {weight}</span>
                </div>
                <span style="font-family:'DM Mono',monospace; font-size:18px;
                             font-weight:600; color:{col}; {glow}">{pct}%</span>
            </div>
            <div class="dim-bar-track">
                <div class="dim-bar-fill"
                     style="width:{fill}%; background:{bar_col};
                            transition: width 1.1s ease-in-out;"></div>
            </div>
            <div style="font-family:'DM Mono',monospace; font-size:13px;
                        color:#555; margin-top:4px;">{detail}</div>
        </div>
        """, unsafe_allow_html=True)

    rec_border = '#1d9e75' if grade in ['A', 'B'] else '#e24b4a'
    rec_bg = 'linear-gradient(135deg,#0a1f1a,#0d2420)' if grade in ['A', 'B'] else 'linear-gradient(135deg,#1f0a0a,#220d0d)'
    st.markdown(f"""
    <div style="background:{rec_bg}; border-left:3px solid {rec_border};
                border-radius:0 10px 10px 0; padding:14px 20px;
                font-size:14px; color:#bbb; margin:18px 0; line-height:1.6;">
        {dq['recommendation']}
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.subheader('Run Fairness Audit')

    audit_allowed = st.session_state.quality_result.get('audit_allowed', False)
    detected_attrs = st.session_state.quality_result.get('detected_attributes', [])
    semantic = st.session_state.get('semantic_analysis') or {}
    outcome_vars = semantic.get('outcome_variables', [])
    default_outcome = st.session_state.get('outcome_column') or (outcome_vars[0] if outcome_vars else '')

    outcome_input = st.text_input(
        'Outcome column',
        value=default_outcome,
        help='The column to measure fairness against (e.g. income, hired, loan_approved).'
    )

    if not audit_allowed:
        st.warning('No protected attributes were auto-detected. Enter them manually below.')
        manual_attrs_input = st.text_input(
            'Protected attributes (comma-separated)',
            placeholder='e.g. sex, race, age'
        )
        protected_attrs = [a.strip() for a in manual_attrs_input.split(',') if a.strip()] if manual_attrs_input else []
    else:
        st.info(f"Auto-detected protected attributes: **{', '.join(detected_attrs)}**")
        override_input = st.text_input(
            'Override protected attributes (optional)',
            placeholder='Leave blank to use auto-detected',
            value=''
        )
        protected_attrs = [a.strip() for a in override_input.split(',') if a.strip()] if override_input else detected_attrs

    can_run = bool(outcome_input) and bool(protected_attrs)

    if st.button('Run Fairness Audit →', disabled=not can_run):
        with st.spinner('Running fairness audit...'):
            headers = {}
            if st.session_state.get('token'):
                headers['Authorization'] = f'Bearer {st.session_state.token}'
            payload = {
                'dataset_id': st.session_state.dataset_id,
                'outcome_column': outcome_input,
                'protected_attributes': protected_attrs
            }
            res = st.session_state.api_session.post(
                f'{BASE_URL}/api/audit',
                json=payload,
                headers=headers
            )
        if res.status_code == 200:
            st.session_state.fairness_result = res.json()
            st.session_state.outcome_column = outcome_input
            st.session_state.current_page = 'fairness'
            st.rerun()
        else:
            err = res.json()
            st.error(f'Fairness audit failed: {err.get("error", "Unknown error")}')
            if 'available_columns' in err:
                st.info(f"Available columns: {', '.join(err['available_columns'])}")
            if 'next_step' in err:
                st.info(f"Required next step: {err['next_step']}")