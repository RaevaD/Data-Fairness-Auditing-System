import streamlit as st

def show_landing_page():
    st.markdown("""
    <div style="text-align:center; padding: 4rem 2rem 2rem;">
        <h1 style="font-size:3rem; font-weight:700; color:#7f77dd; letter-spacing:-2px; margin-bottom:0.5rem;">
            Fairness Auditor
        </h1>
        <p style="font-family:'DM Mono',monospace; font-size:14px; color:#5dcaa5; margin-bottom:3rem;">
            Automated dataset quality scoring & algorithmic bias detection
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="background:#12103a; border:0.5px solid #2a2560; border-radius:12px; padding:2rem; margin-bottom:2rem;">
            <div style="margin-bottom:1.5rem;">
                <div style="font-family:'DM Mono',monospace; font-size:10px; color:#7f77dd; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px;">What this does</div>
                <p style="font-size:14px; color:#e8e0ff; line-height:1.7;">
                    Upload any CSV or Excel dataset. The system scores it across 4 quality dimensions,
                    audits it for algorithmic bias against protected demographic groups, and generates
                    a plain English AI explanation using Claude.
                </p>
            </div>
            <p style="font-family:'DM Mono',monospace; font-size:10px; color:#2a2560; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px;">Click any card to learn more</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div style="background:#0e0c2e; border:0.5px solid #2a2560; border-left:4px solid #7f77dd;
                        border-radius:0 8px 8px 0; padding:16px; margin-bottom:4px;">
                <div style="font-family:'DM Mono',monospace; font-size:11px; color:#7f77dd;
                            letter-spacing:1px; margin-bottom:6px;">QUALITY SCORING</div>
                <div style="font-size:13px; color:#afa9ec; line-height:1.5;">Completeness, Validity, Consistency, Uniqueness</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="learn-more-btn">', unsafe_allow_html=True)
            if st.button('Learn more', key='info_quality', use_container_width=True):
                st.session_state.current_page = 'info_quality'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("<div style='margin-top:12px;'></div>", unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#061a20; border:0.5px solid #0a3d35; border-left:4px solid #5dcaa5;
                        border-radius:0 8px 8px 0; padding:16px; margin-bottom:4px;">
                <div style="font-family:'DM Mono',monospace; font-size:11px; color:#5dcaa5;
                            letter-spacing:1px; margin-bottom:6px;">AI EXPLANATION</div>
                <div style="font-size:13px; color:#9fe1cb; line-height:1.5;">Plain English report with action items</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="learn-more-btn">', unsafe_allow_html=True)
            if st.button('Learn more', key='info_ai', use_container_width=True):
                st.session_state.current_page = 'info_ai'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div style="background:#0a1f18; border:0.5px solid #0f3d28; border-left:4px solid #1d9e75;
                        border-radius:0 8px 8px 0; padding:16px; margin-bottom:4px;">
                <div style="font-family:'DM Mono',monospace; font-size:11px; color:#1d9e75;
                            letter-spacing:1px; margin-bottom:6px;">FAIRNESS AUDIT</div>
                <div style="font-size:13px; color:#5dcaa5; line-height:1.5;">Disparate Impact, Demographic Parity, SPD</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="learn-more-btn">', unsafe_allow_html=True)
            if st.button('Learn more', key='info_fairness', use_container_width=True):
                st.session_state.current_page = 'info_fairness'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("<div style='margin-top:12px;'></div>", unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#12103a; border:0.5px solid #2a2560; border-left:4px solid #afa9ec;
                        border-radius:0 8px 8px 0; padding:16px; margin-bottom:4px;">
                <div style="font-family:'DM Mono',monospace; font-size:11px; color:#afa9ec;
                            letter-spacing:1px; margin-bottom:6px;">AUDIT HISTORY</div>
                <div style="font-size:13px; color:#cecbf6; line-height:1.5;">Track all previous dataset audits</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="learn-more-btn">', unsafe_allow_html=True)
            if st.button('Learn more', key='info_history', use_container_width=True):
                st.session_state.current_page = 'info_history'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown('<div class="auth-buttons">', unsafe_allow_html=True)
            if st.button('Login', use_container_width=True, type='primary'):
                st.session_state.current_page = 'login'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div class="auth-buttons">', unsafe_allow_html=True)
            if st.button('Register', use_container_width=True, type='primary'):
                st.session_state.current_page = 'register'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)


def show_login_page(BASE_URL):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align:center; margin-bottom:2rem; padding-top:3rem;">
            <h1 style="font-size:2rem; color:#7f77dd;">Sign in</h1>
            <p style="font-family:'DM Mono',monospace; font-size:12px; color:#5dcaa5;">
                Enter your credentials to continue
            </p>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input('Username', placeholder='Enter username')
        password = st.text_input('Password', type='password', placeholder='Enter password')

        st.markdown('<div class="auth-buttons">', unsafe_allow_html=True)
        if st.button('Login', use_container_width=True, type='primary'):
            if not username or not password:
                st.error('Please enter both username and password.')
            else:
                try:
                    res = st.session_state.api_session.post(
                        f'{BASE_URL}/auth/login',
                        json={'username': username, 'password': password}
                    )
                    if res.status_code == 200:
                        data = res.json()
                        st.session_state.token = data.get('token')
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.session_state.current_page = 'upload'
                        st.rerun()
                    else:
                        st.error(res.json().get('error', 'Login failed.'))
                except Exception:
                    st.error('Cannot connect to server. Make sure the backend is running.')
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button('Back to Home', use_container_width=True):
            st.session_state.current_page = 'landing'
            st.rerun()


def show_register_page(BASE_URL):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align:center; margin-bottom:2rem; padding-top:3rem;">
            <h1 style="font-size:2rem; color:#7f77dd;">Create account</h1>
            <p style="font-family:'DM Mono',monospace; font-size:12px; color:#5dcaa5;">
                Choose a username and password
            </p>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input('Username', placeholder='Choose a username')
        password = st.text_input('Password', type='password', placeholder='Choose a password')

        st.markdown('<div class="auth-buttons">', unsafe_allow_html=True)
        if st.button('Create Account', use_container_width=True, type='primary'):
            if not username or not password:
                st.error('Please fill in both fields.')
            else:
                try:
                    res = st.session_state.api_session.post(
                        f'{BASE_URL}/auth/register',
                        json={'username': username, 'password': password}
                    )
                    if res.status_code == 201:
                        login_res = st.session_state.api_session.post(
                            f'{BASE_URL}/auth/login',
                            json={'username': username, 'password': password}
                        )
                        if login_res.status_code == 200:
                            data = login_res.json()
                            st.session_state.token = data.get('token')
                            st.session_state.logged_in = True
                            st.session_state.username = username
                            st.session_state.current_page = 'upload'
                            st.rerun()
                    else:
                        st.error(res.json().get('error', 'Registration failed.'))
                except Exception:
                    st.error('Cannot connect to server. Make sure the backend is running.')
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button('Back to Home', use_container_width=True):
            st.session_state.current_page = 'landing'
            st.rerun()


def show_upload_page(BASE_URL):
    st.title('Upload Dataset')
    st.caption(f'Signed in as {st.session_state.username}')
    st.divider()

    uploaded_file = st.file_uploader('Choose a CSV or Excel file', type=['csv', 'xlsx', 'xls'])

    if uploaded_file:
        if st.button('Upload Dataset'):
            with st.spinner('Uploading...'):
                try:
                    headers = {}
                    if st.session_state.get('token'):
                        headers['Authorization'] = f'Bearer {st.session_state.token}'
                    res = st.session_state.api_session.post(
                        f'{BASE_URL}/api/upload',
                        files={'file': (uploaded_file.name, uploaded_file.getvalue())},
                        headers=headers
                    )
                    if res.status_code == 200:
                        data = res.json()
                        st.session_state.dataset_id = data['dataset_id']
                        stats = data['stats']
                        st.session_state.upload_stats = stats
                        st.session_state.semantic_analysis = data.get('semantic_analysis', {})
                        st.success(f"Uploaded: {data['filename']}")

                        col1, col2, col3 = st.columns(3)
                        col1.metric('Rows', stats.get('total_rows', '—'))
                        col2.metric('Columns', stats.get('total_columns', '—'))
                        col3.metric('Missing %', f"{stats.get('missing_percentage', 0)}%")

                        protected = stats.get('protected_attributes', [])
                        if protected:
                            st.info(f"Protected attributes detected: {', '.join(protected)}")
                        else:
                            st.warning('No protected attributes detected. Fairness audit may be limited.')
                            st.session_state.no_protected_attrs = True
                    else:
                        st.error(res.json().get('error', 'Upload failed.'))
                except Exception as e:
                    st.error(f'Upload error: {e}')

    if st.session_state.get('dataset_id'):
        if st.button('Check Quality →'):
            st.session_state.current_page = 'quality'
            st.rerun()