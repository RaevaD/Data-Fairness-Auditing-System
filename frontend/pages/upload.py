import streamlit as st

# Replace the top of show_upload_page with:
def show_upload_page(BASE_URL):
    st.title('Fairness Auditing System')
    st.caption('Automated dataset quality scoring and algorithmic bias detection')
    st.divider()

    if not st.session_state.logged_in:
        col1, col2, col3 = st.columns([1, 2, 1])  # center the login form
        with col2:
            st.subheader('Sign in to continue')
            username = st.text_input('Username', placeholder='Enter username')
            password = st.text_input('Password', type='password', placeholder='Enter password')

        col1, col2 = st.columns(2)
        with col1:
            if st.button('Login', use_container_width=True):
                res = st.session_state.api_session.post(
                    f'{BASE_URL}/auth/login',
                    json={'username': username, 'password': password}
                )
                if res.status_code == 200:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success('Logged in!')
                    st.rerun()
                else:
                    st.error('Login failed. Check your credentials.')

        with col2:
            if st.button('Register', use_container_width=True):
                res = st.session_state.api_session.post(
                    f'{BASE_URL}/auth/register',
                    json={'username': username, 'password': password}
                )
                if res.status_code == 201:
                    st.success('Registered! Now log in.')
                else:
                    st.error(f'Registration failed: {res.json().get("error", "Unknown error")}')
    else:
        st.subheader(f'Welcome, {st.session_state.username}! Upload a Dataset')
        uploaded_file = st.file_uploader('Choose a CSV or Excel file', type=['csv', 'xlsx', 'xls'])

        if uploaded_file:
            if st.button('Upload Dataset'):
                with st.spinner('Uploading...'):
                    res = st.session_state.api_session.post(
                        f'{BASE_URL}/api/upload',
                        files={'file': (uploaded_file.name, uploaded_file.getvalue())}
                    )
                if res.status_code == 200:
                    data = res.json()
                    st.session_state.dataset_id = data['dataset_id']
                    st.success(f"Uploaded: {data['filename']}")
                    stats = data['stats']
                    col1, col2, col3 = st.columns(3)
                    col1.metric('Rows', stats['total_rows'])
                    col2.metric('Columns', stats['total_columns'])
                    col3.metric('Missing %', f"{stats['missing_percentage']}%")
                    st.info(f"Protected attributes detected: {', '.join(stats.get('protected_attributes', []))}")
                else:
                    st.error('Upload failed.')
                    if st.session_state.dataset_id:
                        if st.button('Check Quality →'):
                            st.session_state.current_page = 'quality'
                            st.rerun()