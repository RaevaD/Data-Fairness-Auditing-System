import streamlit as st

def show_upload_page(BASE_URL):
    st.title('Upload Dataset')
    st.caption(f'Signed in as {st.session_state.username}')
    st.divider()

    uploaded_file = st.file_uploader('Choose a CSV or Excel file', type=['csv', 'xlsx', 'xls'])

    if uploaded_file:
        if st.button('Upload Dataset'):
            with st.spinner('Uploading and analyzing columns with AI... this may take a few seconds.'):
                try:
                    res = st.session_state.api_session.post(
                        f'{BASE_URL}/api/upload',
                        files={'file': (uploaded_file.name, uploaded_file.getvalue())}
                    )
                    if res.status_code == 200:
                        data = res.json()
                        st.session_state.dataset_id = data['dataset_id']
                        st.session_state.quality_result = None
                        st.session_state.fairness_result = None
                        st.session_state.explanation_result = None

                        # Store semantic analysis and auto-detected outcome column
                        semantic = data.get('semantic_analysis', {})
                        st.session_state.semantic_analysis = semantic
                        outcome_vars = semantic.get('outcome_variables', [])
                        st.session_state.outcome_column = outcome_vars[0] if outcome_vars else None

                        st.success(f"Uploaded: {data['filename']}")
                        stats = data['stats']
                        col1, col2, col3 = st.columns(3)
                        col1.metric('Rows', stats['total_rows'])
                        col2.metric('Columns', stats['total_columns'])
                        col3.metric('Missing %', f"{stats['missing_percentage']}%")

                        # Show semantic analysis summary
                        if semantic:
                            st.divider()
                            st.subheader('AI Column Classification')
                            source = semantic.get('source', 'unknown')
                            if source == 'fallback':
                                st.warning('Gemini AI unavailable — used keyword fallback for column detection.')
                            else:
                                st.caption('Columns classified by Gemini AI')

                            sc1, sc2 = st.columns(2)
                            with sc1:
                                protected = semantic.get('protected_attributes', [])
                                if protected:
                                    st.info(f"**Protected attributes:** {', '.join(protected)}")
                                else:
                                    st.warning('No protected attributes detected.')
                                proxy = semantic.get('proxy_variables', [])
                                if proxy:
                                    st.warning(f"**Proxy variables:** {', '.join(proxy)}")
                            with sc2:
                                outcome = semantic.get('outcome_variables', [])
                                if outcome:
                                    st.success(f"**Outcome variable:** {', '.join(outcome)}")
                                else:
                                    st.warning('No outcome variable detected — you will need to specify it during audit.')
                    else:
                        st.error('Upload failed.')
                except Exception as e:
                    st.error(f'Upload error: {e}')

    if st.session_state.get('dataset_id'):
        if st.button('Check Quality →'):
            st.session_state.current_page = 'quality'
            st.rerun()