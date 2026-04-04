import streamlit as st

def show_fairness_page(BASE_URL):
    st.title('Fairness Audit Report')
    st.caption('Bias detection across protected demographic attributes')
    st.divider()

    if not st.session_state.fairness_result:
        st.warning('No fairness audit run yet. Go to Quality Report and click "Run Fairness Audit".')
        return

    audit = st.session_state.fairness_result['fairness_audit']

    for attribute, results in audit.items():
        with st.container(border=True):

            # Inline attribute name + verdict badge
            col_a, col_b = st.columns([4, 1])
            with col_a:
                st.subheader(attribute.capitalize())
            with col_b:
                if results['is_fair']:
                    st.success('FAIR')
                else:
                    st.error('UNFAIR')

            # Metrics row
            col1, col2, col3 = st.columns(3)
            di = results['disparate_impact']
            col1.metric(
                'Disparate Impact',
                round(di, 3),
                help='Threshold: 0.8. Below = biased.'
            )
            col2.metric(
                'Demographic Parity',
                round(results['demographic_parity'], 3),
                help='Threshold: less than 0.1 is fair'
            )
            col3.metric(
                'SPD',
                round(results['spd'], 3),
                help='Close to 0 = fair'
            )

            # Disparate impact bar
            st.write('Disparate Impact — threshold at 0.8')
            st.progress(min(di, 1.0))

            if di < 0.8:
                st.caption(f'{round(di, 3)} — Below the fairness threshold. Bias detected.')
            else:
                st.caption(f'{round(di, 3)} — Above the fairness threshold. Passes.')

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