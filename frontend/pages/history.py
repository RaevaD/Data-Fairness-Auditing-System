import streamlit as st
import pandas as pd

def show_history_page(BASE_URL):
    st.title('Audit History')
    st.caption('All previously uploaded and analysed datasets')
    st.divider()

    res = st.session_state.api_session.get(f'{BASE_URL}/api/datasets')

    if res.status_code != 200:
        st.error('Could not load history.')
        return

    data = res.json()
    datasets = data.get('datasets', [])

    if not datasets:
        st.info('No datasets uploaded yet. Upload a file to get started.')
        return

    # Summary metric
    st.metric('Total Datasets', len(datasets))
    st.divider()

    # Clean table
    df = pd.DataFrame(datasets)[['filename', 'total_rows', 'total_columns', 'processed']]
    df.columns = ['Filename', 'Rows', 'Columns', 'Processed']
    df['Processed'] = df['Processed'].map({True: 'Yes', False: 'No'})
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.divider()
    st.subheader('View Results')

    for ds in datasets:
        with st.container(border=True):
            col1, col2, col3 = st.columns([3, 1, 1])
            col1.write(f"**{ds['filename']}**")
            col2.caption(f"{ds['total_rows']:,} rows")
            col3.caption(f"{ds['total_columns']} columns")

            if st.button('View Results', key=ds['dataset_id']):
                res2 = st.session_state.api_session.get(
                    f'{BASE_URL}/api/results/{ds["dataset_id"]}'
                )
                if res2.status_code == 200:
                    st.json(res2.json())
                else:
                    st.error('Results not available for this dataset.')

    st.divider()
    if st.button('Logout', type='primary'):
        st.session_state.api_session.post(f'{BASE_URL}/auth/logout')
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()