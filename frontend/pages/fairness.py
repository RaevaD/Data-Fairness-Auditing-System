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
                            help='Threshold: 0.8 or above is fair.')
            if dp is not None:
                col2.metric('Demographic Parity', round(dp, 3),
                            help='Threshold: 0.1 or below is fair.')
            if spd is not None:
                col3.metric('SPD', round(spd, 3),
                            help='Close to 0 is fair.')

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
                st.write(f'Statistical Parity Difference — fair if within {THRESHOLD_SPD}')
                st.progress(progress_spd)
                if is_fair_spd:
                    st.caption(f'{sign_str} — Within the fairness threshold.')
                else:
                    st.caption(f'{sign_str} — Exceeds fairness threshold. Bias detected.')

    st.divider()
    show_explanation = st.toggle('Show AI Explanation')

    if show_explanation:
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
        st.subheader('Fairness Analysis & Action Items')
        st.info(explanation['fairness_summary']['explanation'])