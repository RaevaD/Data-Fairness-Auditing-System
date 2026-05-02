import streamlit as st

def show_fairness_page(BASE_URL):
    st.title('Fairness Audit Report')
    st.caption('Bias detection across protected demographic attributes')
    st.divider()

    if not st.session_state.fairness_result:
        st.warning('No fairness audit run yet. Go to Quality Report and click "Run Fairness Audit".')
        return

    result = st.session_state.fairness_result
    fairness_data = result.get('fairness_audit') or result.get('fairness') or {}
    audit = fairness_data.get('results') or fairness_data or {}

    # Remove non-dict entries (metadata keys)
    audit = {k: v for k, v in audit.items() if isinstance(v, dict)}

    # No protected attributes found
    if not audit:
        st.warning('No protected attributes found in this dataset.')
        st.info('Fairness audit cannot be performed without demographic columns such as gender, race, or age. You can still generate an AI quality explanation below.')
        st.divider()
        if st.toggle('Show AI Explanation'):
            if not st.session_state.explanation_result:
                with st.spinner('Generating AI explanation...'):
                    res = st.session_state.api_session.post(
                        f'{BASE_URL}/api/explain',
                        json={'dataset_id': st.session_state.dataset_id}
                    )
                if res.status_code == 200:
                    st.session_state.explanation_result = res.json()
                else:
                    st.error('Could not generate explanation. Check your API key in the .env file.')
                    return
            explanation = st.session_state.explanation_result['explanation']
            st.subheader('Quality Summary')
            st.info(explanation['quality_summary']['explanation'])
        return

<<<<<<< HEAD
    # Show outcome column used
    outcome_col = fairness_data.get('outcome_attribute')
    if outcome_col:
        st.caption(f'Outcome column: **{outcome_col}**')

    # Overall summary
    summary = fairness_data.get('summary', {})
    if summary:
        s1, s2, s3 = st.columns(3)
        s1.metric('Attributes Checked', summary.get('total_attributes_checked', len(audit)))
        s2.metric('Fair', summary.get('fair_attributes', 0))
        s3.metric('Unfair', summary.get('unfair_attributes', 0))
        st.divider()

=======
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
    # Render per-attribute results
    for attribute, results in audit.items():

        if 'error' in results:
            with st.container(border=True):
                st.subheader(attribute.capitalize())
                st.warning(f'Could not audit this attribute — {results["error"]}')
            continue

        with st.container(border=True):
            col_a, col_b = st.columns([4, 1])
            with col_a:
                st.subheader(attribute.capitalize())
<<<<<<< HEAD
                priv = results.get('privileged_group')
                unpriv = results.get('unprivileged_group')
                if priv and unpriv:
                    st.caption(f'Privileged: {priv} · Unprivileged: {unpriv}')
=======
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
            with col_b:
                if results.get('is_fair', False):
                    st.success('FAIR')
                else:
                    st.error('UNFAIR')

            col1, col2, col3 = st.columns(3)
            di  = results.get('disparate_impact')
            dp  = results.get('demographic_parity')
            spd = results.get('spd')

            if di is not None:
                col1.metric('Disparate Impact', round(di, 3),
<<<<<<< HEAD
                            help='Threshold: 0.8 or above is fair (80% rule, EEOC).')
=======
                            help='Threshold: 0.8 or above is fair.')
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
            if dp is not None:
                col2.metric('Demographic Parity', round(dp, 3),
                            help='Threshold: 0.1 or below is fair.')
            if spd is not None:
                col3.metric('SPD', round(spd, 3),
<<<<<<< HEAD
                            help='Statistical Parity Difference: close to 0 is fair (range: -0.1 to 0.1).')
=======
                            help='Close to 0 is fair.')
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4

            if di is not None:
                THRESHOLD_DI = 0.8
                DISPLAY_MAX_DI = 1.2
                progress_di = min(float(di), DISPLAY_MAX_DI) / DISPLAY_MAX_DI
                is_fair_di = di >= THRESHOLD_DI
                st.write(f'Disparate Impact — fair if above {THRESHOLD_DI}')
                st.progress(progress_di)
                if is_fair_di:
                    st.caption(f'{round(di, 3)} — Above fairness threshold.')
                else:
                    st.caption(f'{round(di, 3)} — Below the fairness threshold. Bias detected.')

            if dp is not None:
                THRESHOLD_DP = 0.1
                progress_dp = min(float(dp), 1.0)
                is_fair_dp = dp <= THRESHOLD_DP
                st.write(f'Demographic Parity — fair if below {THRESHOLD_DP}')
                st.progress(progress_dp)
                if is_fair_dp:
                    st.caption(f'{round(dp, 3)} — Within the fairness threshold.')
                else:
                    st.caption(f'{round(dp, 3)} — Exceeds fairness threshold. Bias detected.')

            if spd is not None:
                THRESHOLD_SPD = 0.1
                abs_spd = abs(float(spd))
                progress_spd = min(abs_spd, 1.0)
                is_fair_spd = abs_spd <= THRESHOLD_SPD
                sign_str = f'+{round(spd, 3)}' if spd > 0 else str(round(spd, 3))
<<<<<<< HEAD
                st.write(f'Statistical Parity Difference — fair if within ±{THRESHOLD_SPD}')
=======
                st.write(f'Statistical Parity Difference — fair if within {THRESHOLD_SPD}')
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
                st.progress(progress_spd)
                if is_fair_spd:
                    st.caption(f'{sign_str} — Within the fairness threshold.')
                else:
                    st.caption(f'{sign_str} — Exceeds fairness threshold. Bias detected.')

    st.divider()
<<<<<<< HEAD
    show_explanation = st.toggle('Show AI Explanation & Remediation Plan')

    if show_explanation:
        if not st.session_state.explanation_result:
            with st.spinner('Generating AI explanation and remediation plan... this may take 10–20 seconds.'):
=======
    show_explanation = st.toggle('Show AI Explanation')

    if show_explanation:
        if not st.session_state.explanation_result:
            with st.spinner('Generating AI explanation...'):
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
                res = st.session_state.api_session.post(
                    f'{BASE_URL}/api/explain',
                    json={'dataset_id': st.session_state.dataset_id}
                )
            if res.status_code == 200:
                st.session_state.explanation_result = res.json()
            else:
                st.error('Could not generate explanation. Check your API key in the .env file.')
                return

<<<<<<< HEAD
        exp_data = st.session_state.explanation_result
        explanation = exp_data.get('explanation', {})
        remediation = exp_data.get('remediation_plan', {})

        st.subheader('Quality Summary')
        quality_exp = explanation.get('quality_summary', {})
        if isinstance(quality_exp, dict):
            st.info(quality_exp.get('explanation', 'No quality explanation available.'))
        else:
            st.info(str(quality_exp))

        st.subheader('Fairness Analysis & Action Items')
        fairness_exp = explanation.get('fairness_summary', {})
        if isinstance(fairness_exp, dict):
            st.info(fairness_exp.get('explanation', 'No fairness explanation available.'))
        else:
            st.info(str(fairness_exp))

        # Remediation Plan
        if remediation and remediation.get('source') != 'no_findings':
            st.divider()
            st.subheader('Remediation Plan')

            source = remediation.get('source', '')
            if source == 'fallback':
                st.warning('Remediation plan generated with fallback (Gemini unavailable).')

            critical = remediation.get('critical_priority', [])
            high = remediation.get('high_priority', [])
            medium = remediation.get('medium_priority', [])

            if critical:
                st.markdown('#### 🔴 Critical Priority')
                for item in critical:
                    with st.container(border=True):
                        st.markdown(f"**Issue:** {item.get('issue', '')}")
                        st.markdown(f"**Fix:** {item.get('fix', '')}")
                        if item.get('technique'):
                            st.caption(f"Technique: {item['technique']}")
                        if item.get('verification'):
                            st.caption(f"Verification: {item['verification']}")

            if high:
                st.markdown('#### 🟡 High Priority')
                for item in high:
                    with st.container(border=True):
                        st.markdown(f"**Issue:** {item.get('issue', '')}")
                        st.markdown(f"**Fix:** {item.get('fix', '')}")
                        if item.get('technique'):
                            st.caption(f"Technique: {item['technique']}")
                        if item.get('verification'):
                            st.caption(f"Verification: {item['verification']}")

            if medium:
                st.markdown('#### 🟢 Medium Priority')
                for item in medium:
                    with st.container(border=True):
                        st.markdown(f"**Issue:** {item.get('issue', '')}")
                        st.markdown(f"**Fix:** {item.get('fix', '')}")
                        if item.get('verification'):
                            st.caption(f"Verification: {item['verification']}")
=======
        explanation = st.session_state.explanation_result['explanation']
        st.subheader('Quality Summary')
        st.info(explanation['quality_summary']['explanation'])
        st.subheader('Fairness Analysis & Action Items')
        st.info(explanation['fairness_summary']['explanation'])
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
