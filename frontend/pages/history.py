import streamlit as st
import pandas as pd

def show_history_page(BASE_URL):
    st.title('Audit History')
    st.caption('All previously uploaded and analysed datasets')
    st.divider()

    headers = {}
    if st.session_state.get('token'):
        headers['Authorization'] = f'Bearer {st.session_state.token}'

    res = st.session_state.api_session.get(f'{BASE_URL}/api/datasets', headers=headers)

    if res.status_code != 200:
        st.error('Could not load history.')
        return

    data = res.json()
    datasets = data.get('datasets', [])

    if not datasets:
        st.markdown("""
        <div style="background:#12103a; border:0.5px solid #2a2560; border-radius:10px;
                    padding:20px; text-align:center; color:#555; font-size:13px;">
            No datasets uploaded yet.
        </div>
        """, unsafe_allow_html=True)
        return

    st.markdown(f"""
    <div style="background:#12103a; border:0.5px solid #2a2560; border-radius:10px;
                padding:14px 20px; margin-bottom:16px; display:inline-block;">
        <span style="font-family:'DM Mono',monospace; font-size:1.4rem; color:#7f77dd;">{len(datasets)}</span>
        <span style="font-size:12px; color:#555; margin-left:8px;">total datasets</span>
    </div>
    """, unsafe_allow_html=True)

    df = pd.DataFrame(datasets)[['filename', 'total_rows', 'total_columns', 'processed']]
    df.columns = ['Filename', 'Rows', 'Columns', 'Processed']
    df['Processed'] = df['Processed'].map({True: 'Yes', False: 'No'})
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.divider()
    st.subheader('View Results')

    for ds in datasets:
        st.markdown(f"""
        <div style="background:#12103a; border:0.5px solid #2a2560; border-radius:10px;
                    padding:12px 16px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
            <div>
                <div style="font-size:13px; font-weight:500; color:#e8e0ff;">{ds['filename']}</div>
                <div style="font-family:'DM Mono',monospace; font-size:11px; color:#555; margin-top:2px;">
                    {ds['total_rows']:,} rows · {ds['total_columns']} columns
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button('View Results', key=ds['dataset_id']):
            res2 = st.session_state.api_session.get(
                f'{BASE_URL}/api/results/{ds["dataset_id"]}',
                headers=headers
            )
            if res2.status_code == 200:
                st.json(res2.json())
            else:
                st.error('Results not available.')

    st.divider()
    if st.button('Logout', type='primary'):
        st.session_state.api_session.post(f'{BASE_URL}/auth/logout', headers=headers)
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()