import streamlit as st

def show_landing_page():
    st.markdown("""
    <div style="text-align:center; padding: 4rem 2rem 2rem;">
        <h1 style="font-size:3rem; font-weight:700; color:#ff6f00; letter-spacing:-2px; margin-bottom:0.5rem;">
            Fairness Auditor
        </h1>
        <p style="font-family:'DM Mono',monospace; font-size:14px; color:#608ec7; margin-bottom:3rem;">
            Automated dataset quality scoring & algorithmic bias detection
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-radius:12px; padding:2rem; margin-bottom:2rem;">
            <div style="margin-bottom:1.5rem;">
                <div style="font-family:'DM Mono',monospace; font-size:10px; color:#ff6f00; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px;">What this does</div>
                <p style="font-size:14px; color:#ffffff; line-height:1.7;">
                    Upload any CSV or Excel dataset. The system scores it across 4 quality dimensions,
                    audits it for algorithmic bias against protected demographic groups, and generates
                    a plain English AI explanation using Claude.
                </p>
            </div>
            <p style="font-family:'DM Mono',monospace; font-size:10px; color:#444; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px;">Click any card to learn more</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div style="background:#030303; border:1px solid #1a1a1a; border-left:3px solid #ff6f00; border-radius:6px; padding:12px; margin-bottom:4px;">
                <div style="font-family:'DM Mono',monospace; font-size:10px; color:#ff6f00; margin-bottom:4px;">QUALITY SCORING</div>
                <div style="font-size:12px; color:#888;">Completeness, Validity, Consistency, Uniqueness</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="learn-more-btn">', unsafe_allow_html=True)
            if st.button('Learn more', key='info_quality', use_container_width=True):
                st.session_state.current_page = 'info_quality'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("<div style='margin-top:12px;'></div>", unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#030303; border:1px solid #1a1a1a; border-left:3px solid #608ec7; border-radius:6px; padding:12px; margin-bottom:4px;">
                <div style="font-family:'DM Mono',monospace; font-size:10px; color:#608ec7; margin-bottom:4px;">AI EXPLANATION</div>
                <div style="font-size:12px; color:#888;">Plain English report with action items</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="learn-more-btn">', unsafe_allow_html=True)
            if st.button('Learn more', key='info_ai', use_container_width=True):
                st.session_state.current_page = 'info_ai'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div style="background:#030303; border:1px solid #1a1a1a; border-left:3px solid #db1886; border-radius:6px; padding:12px; margin-bottom:4px;">
                <div style="font-family:'DM Mono',monospace; font-size:10px; color:#db1886; margin-bottom:4px;">FAIRNESS AUDIT</div>
                <div style="font-size:12px; color:#888;">Disparate Impact, Demographic Parity, SPD</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<div class="learn-more-btn">', unsafe_allow_html=True)
            if st.button('Learn more', key='info_fairness', use_container_width=True):
                st.session_state.current_page = 'info_fairness'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("<div style='margin-top:12px;'></div>", unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#030303; border:1px solid #1a1a1a; border-left:3px solid #ffffff; border-radius:6px; padding:12px; margin-bottom:4px;">
                <div style="font-family:'DM Mono',monospace; font-size:10px; color:#ffffff; margin-bottom:4px;">AUDIT HISTORY</div>
                <div style="font-size:12px; color:#888;">Track all previous dataset audits</div>
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
            if st.button('Login', use_container_width=True):
                st.session_state.current_page = 'login'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div class="auth-buttons">', unsafe_allow_html=True)
            if st.button('Register', use_container_width=True):
                st.session_state.current_page = 'register'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)


def show_login_page(BASE_URL):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align:center; margin-bottom:2rem; padding-top:3rem;">
            <h1 style="font-size:2rem; color:#ff6f00;">Sign in</h1>
            <p style="font-family:'DM Mono',monospace; font-size:12px; color:#608ec7;">
                Enter your credentials to continue
            </p>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input('Username', placeholder='Enter username')
        password = st.text_input('Password', type='password', placeholder='Enter password')

        st.markdown('<div class="auth-buttons">', unsafe_allow_html=True)
        if st.button('Login', use_container_width=True):
            if not username or not password:
                st.error('Please enter both username and password.')
            else:
                try:
                    res = st.session_state.api_session.post(
                        f'{BASE_URL}/auth/login',
                        json={'username': username, 'password': password}
                    )
                    if res.status_code == 200:
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.session_state.current_page = 'upload'
                        st.rerun()
                    else:
                        st.error('Login failed. Check your credentials.')
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
            <h1 style="font-size:2rem; color:#ff6f00;">Create account</h1>
            <p style="font-family:'DM Mono',monospace; font-size:12px; color:#608ec7;">
                Choose a username and password
            </p>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input('Username', placeholder='Choose a username')
        password = st.text_input('Password', type='password', placeholder='Choose a password')

        st.markdown('<div class="auth-buttons">', unsafe_allow_html=True)
        if st.button('Create Account', use_container_width=True):
            if not username or not password:
                st.error('Please fill in both fields.')
            else:
                try:
                    res = st.session_state.api_session.post(
                        f'{BASE_URL}/auth/register',
                        json={'username': username, 'password': password}
                    )
                    if res.status_code == 201:
                        st.success('Account created! Signing you in...')
                        login_res = st.session_state.api_session.post(
                            f'{BASE_URL}/auth/login',
                            json={'username': username, 'password': password}
                        )
                        if login_res.status_code == 200:
                            st.session_state.logged_in = True
                            st.session_state.username = username
                            st.session_state.current_page = 'upload'
                            st.rerun()
                    else:
                        st.error(f'Registration failed: {res.json().get("error", "Unknown error")}')
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
                        protected = stats.get('protected_attributes', [])
                        if protected:
                            st.info(f"Protected attributes detected: {', '.join(protected)}")
                        else:
                            st.warning('No protected attributes detected. Fairness audit will be skipped.')
                            st.session_state.no_protected_attrs = True
                    else:
                        st.error('Upload failed.')
                except Exception as e:
                    st.error(f'Upload error: {e}')

    if st.session_state.get('dataset_id'):
        if st.button('Check Quality →'):
            st.session_state.current_page = 'quality'
            st.rerun()