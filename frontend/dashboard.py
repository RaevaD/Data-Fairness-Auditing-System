import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
import requests
<<<<<<< HEAD
from pages.upload import show_upload_page
=======
from pages.upload import show_landing_page, show_login_page, show_register_page, show_upload_page
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
from pages.quality import show_quality_page
from pages.fairness import show_fairness_page
from pages.history import show_history_page
from pages.info import show_info_page

st.set_page_config(page_title='Fairness Auditing System', layout='wide')

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700&family=DM+Mono:wght@300;400;500&display=swap');

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif !important;
    background-color: #030303 !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
h1 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.8rem !important;
    letter-spacing: -1px !important;
    color: #ff6f00 !important;
}
h2 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    color: #db1886 !important;
    letter-spacing: -0.3px !important;
}
h3 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    color: #608ec7 !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
p, li, span, div {
    font-family: 'Syne', sans-serif !important;
    color: #ffffff !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
[data-testid="stCaptionContainer"] p {
    font-family: 'DM Mono', monospace !important;
    font-size: 11px !important;
    color: #608ec7 !important;
    letter-spacing: 0.5px !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
.block-container {
    border-top: 2px solid #db1886;
    padding-top: 2rem !important;
    background-color: #030303 !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
[data-testid="metric-container"] {
    background: #0a0a0a !important;
    border: 1px solid #1a1a1a !important;
    border-radius: 10px !important;
    padding: 1rem !important;
}
[data-testid="metric-container"] label {
    font-family: 'DM Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    color: #608ec7 !important;
}
[data-testid="stMetricValue"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 1.6rem !important;
    color: #ff6f00 !important;
}
<<<<<<< HEAD
=======

/* Default button — outline orange */
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
.stButton > button {
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    letter-spacing: 0.5px !important;
    border-radius: 6px !important;
    border: 1px solid #ff6f00 !important;
    color: #ff6f00 !important;
    background: transparent !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    background: #ff6f00 !important;
    color: #030303 !important;
}
<<<<<<< HEAD
=======

/* Auth buttons — filled solid orange */
div.auth-buttons .stButton > button {
    background: #ff6f00 !important;
    color: #030303 !important;
    border: none !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    border-radius: 6px !important;
}
div.auth-buttons .stButton > button:hover {
    background: #cc5a00 !important;
    color: #030303 !important;
}

/* Learn more buttons — subtle ghost */
div.learn-more-btn .stButton > button {
    background: transparent !important;
    color: #444 !important;
    border: 1px solid #1a1a1a !important;
    font-size: 11px !important;
    font-weight: 400 !important;
    letter-spacing: 0.5px !important;
    padding: 0.3rem 0.8rem !important;
    border-radius: 4px !important;
}
div.learn-more-btn .stButton > button:hover {
    border-color: #444 !important;
    color: #888 !important;
    background: transparent !important;
}

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
.stProgress > div > div {
    height: 4px !important;
    border-radius: 2px !important;
    background: #ff6f00 !important;
}
.stProgress > div {
    background: #1a1a1a !important;
    border-radius: 2px !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
[data-testid="stSidebar"] {
    background-color: #080808 !important;
    border-right: 1px solid #1a1a1a !important;
}
[data-testid="stSidebar"] * {
    font-family: 'Syne', sans-serif !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
.stTextInput > div > div > input {
    font-family: 'DM Mono', monospace !important;
    font-size: 13px !important;
    background: #0a0a0a !important;
    border: 1px solid #1a1a1a !important;
    color: #ffffff !important;
    border-radius: 6px !important;
}
.stTextInput > div > div > input:focus {
    border-color: #ff6f00 !important;
    box-shadow: 0 0 0 1px #ff6f00 !important;
}
.stTextInput label {
    color: #608ec7 !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 11px !important;
    letter-spacing: 0.5px !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
[data-testid="stFileUploader"] {
    background: #0a0a0a !important;
    border: 1px dashed #1a1a1a !important;
    border-radius: 8px !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
[data-testid="stAlert"] {
    border-radius: 0 6px 6px 0 !important;
    border-left-width: 3px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 12px !important;
    background: #0a0a0a !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
[data-testid="stDataFrame"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 12px !important;
}
<<<<<<< HEAD
hr {
    border-color: #1a1a1a !important;
}
=======

hr {
    border-color: #1a1a1a !important;
}

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
[data-testid="stToggle"] label {
    font-family: 'Syne', sans-serif !important;
    color: #ff6f00 !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] small {
    font-family: 'DM Mono', monospace !important;
    font-size: 11px !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
div[data-testid="stSidebar"] div.nav-upload button {
    background-color: #0a0f18 !important;
    border: 1px solid #608ec744 !important;
    color: #608ec7 !important;
    border-radius: 8px !important;
    font-size: 0.9rem !important;
    font-weight: 400 !important;
    width: 100% !important;
    text-align: left !important;
    margin-bottom: 4px !important;
}
div[data-testid="stSidebar"] div.nav-upload-active button {
    background-color: #608ec7 !important;
    border: 2px solid #608ec7 !important;
    color: #030303 !important;
    border-radius: 8px !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    text-align: left !important;
    margin-bottom: 4px !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
div[data-testid="stSidebar"] div.nav-quality button {
    background-color: #180a00 !important;
    border: 1px solid #ff6f0044 !important;
    color: #ff6f00 !important;
    border-radius: 8px !important;
    font-size: 0.9rem !important;
    font-weight: 400 !important;
    width: 100% !important;
    text-align: left !important;
    margin-bottom: 4px !important;
}
div[data-testid="stSidebar"] div.nav-quality-active button {
    background-color: #ff6f00 !important;
    border: 2px solid #ff6f00 !important;
    color: #030303 !important;
    border-radius: 8px !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    text-align: left !important;
    margin-bottom: 4px !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
div[data-testid="stSidebar"] div.nav-fairness button {
    background-color: #180008 !important;
    border: 1px solid #db188644 !important;
    color: #db1886 !important;
    border-radius: 8px !important;
    font-size: 0.9rem !important;
    font-weight: 400 !important;
    width: 100% !important;
    text-align: left !important;
    margin-bottom: 4px !important;
}
div[data-testid="stSidebar"] div.nav-fairness-active button {
    background-color: #db1886 !important;
    border: 2px solid #db1886 !important;
    color: #ffffff !important;
    border-radius: 8px !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    text-align: left !important;
    margin-bottom: 4px !important;
}
<<<<<<< HEAD
=======

>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
div[data-testid="stSidebar"] div.nav-history button {
    background-color: #0a0a0a !important;
    border: 1px solid #ffffff22 !important;
    color: #888888 !important;
    border-radius: 8px !important;
    font-size: 0.9rem !important;
    font-weight: 400 !important;
    width: 100% !important;
    text-align: left !important;
    margin-bottom: 4px !important;
}
div[data-testid="stSidebar"] div.nav-history-active button {
    background-color: #ffffff !important;
    border: 2px solid #ffffff !important;
    color: #030303 !important;
    border-radius: 8px !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    text-align: left !important;
    margin-bottom: 4px !important;
}
</style>
""", unsafe_allow_html=True)

BASE_URL = 'http://localhost:5000'

<<<<<<< HEAD
# ── Session state init (single, clean block) ──────────────────────────────────
=======
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
<<<<<<< HEAD
if 'token' not in st.session_state:
    st.session_state.token = None
=======
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
if 'dataset_id' not in st.session_state:
    st.session_state.dataset_id = None
if 'quality_result' not in st.session_state:
    st.session_state.quality_result = None
if 'fairness_result' not in st.session_state:
    st.session_state.fairness_result = None
if 'explanation_result' not in st.session_state:
    st.session_state.explanation_result = None
<<<<<<< HEAD
if 'semantic_analysis' not in st.session_state:
    st.session_state.semantic_analysis = None
if 'outcome_column' not in st.session_state:
    st.session_state.outcome_column = None
=======
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
if 'no_protected_attrs' not in st.session_state:
    st.session_state.no_protected_attrs = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'landing'
if 'api_session' not in st.session_state:
    st.session_state.api_session = requests.Session()

<<<<<<< HEAD

# ── Auth helpers ──────────────────────────────────────────────────────────────
def do_login(username, password):
    try:
        res = requests.post(
            f'{BASE_URL}/auth/login',
            json={'username': username, 'password': password}
        )
        if res.status_code == 200:
            data = res.json()
            token = data['token']
            st.session_state.token = token
            st.session_state.api_session.headers.update({
                'Authorization': f'Bearer {token}'
            })
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.current_page = 'upload'
            st.rerun()
        else:
            st.error(res.json().get('error', 'Login failed.'))
    except Exception:
        st.error('Cannot connect to server. Make sure the backend is running on port 5000.')


def do_register(username, password):
    try:
        res = requests.post(
            f'{BASE_URL}/auth/register',
            json={'username': username, 'password': password}
        )
        if res.status_code == 201:
            st.success('Account created! Signing you in...')
            do_login(username, password)
        else:
            st.error(res.json().get('error', 'Registration failed.'))
    except Exception:
        st.error('Cannot connect to server. Make sure the backend is running on port 5000.')


def logout():
    try:
        st.session_state.api_session.post(f'{BASE_URL}/auth/logout')
    except Exception:
        pass
    for key in list(st.session_state.keys()):
        del st.session_state[key]

def show_landing_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align:center; padding-top:4rem; margin-bottom:2.5rem;">
            <h1 style="font-size:2.8rem; letter-spacing:-2px;">Fairness Auditor</h1>
            <p style="font-family:'DM Mono',monospace; font-size:12px; color:#608ec7;">
                Automated dataset quality scoring & algorithmic bias detection
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background:#0a0a0a; border:1px solid #1a1a1a; border-radius:12px; padding:1.5rem; margin-bottom:1.5rem;">
            <div style="font-family:'DM Mono',monospace; font-size:10px; color:#ff6f00; letter-spacing:1px; text-transform:uppercase; margin-bottom:8px;">What this does</div>
            <p style="font-size:13px; color:#ffffff; line-height:1.7; margin:0;">
                Upload any CSV or Excel dataset. The system scores it across 4 quality dimensions,
                audits it for bias against protected demographic groups, and generates a plain
                English explanation with a prioritised remediation plan.
            </p>
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
            if st.button('Learn more', key='info_quality', use_container_width=True):
                st.session_state.current_page = 'info_quality'
                st.rerun()

            st.markdown("<div style='margin-top:12px;'></div>", unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#030303; border:1px solid #1a1a1a; border-left:3px solid #608ec7; border-radius:6px; padding:12px; margin-bottom:4px;">
                <div style="font-family:'DM Mono',monospace; font-size:10px; color:#608ec7; margin-bottom:4px;">AI EXPLANATION</div>
                <div style="font-size:12px; color:#888;">Plain English report with remediation plan</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button('Learn more', key='info_ai', use_container_width=True):
                st.session_state.current_page = 'info_ai'
                st.rerun()

        with c2:
            st.markdown("""
            <div style="background:#030303; border:1px solid #1a1a1a; border-left:3px solid #db1886; border-radius:6px; padding:12px; margin-bottom:4px;">
                <div style="font-family:'DM Mono',monospace; font-size:10px; color:#db1886; margin-bottom:4px;">FAIRNESS AUDIT</div>
                <div style="font-size:12px; color:#888;">Disparate Impact, Demographic Parity, SPD</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button('Learn more', key='info_fairness', use_container_width=True):
                st.session_state.current_page = 'info_fairness'
                st.rerun()

            st.markdown("<div style='margin-top:12px;'></div>", unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#030303; border:1px solid #1a1a1a; border-left:3px solid #ffffff; border-radius:6px; padding:12px; margin-bottom:4px;">
                <div style="font-family:'DM Mono',monospace; font-size:10px; color:#ffffff; margin-bottom:4px;">AUDIT HISTORY</div>
                <div style="font-size:12px; color:#888;">Track all previous dataset audits</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button('Learn more', key='info_history', use_container_width=True):
                st.session_state.current_page = 'info_history'
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2 = st.columns(2)
        with b1:
            if st.button('Login', use_container_width=True, key='landing_login'):
                st.session_state.current_page = 'login'
                st.rerun()
        with b2:
            if st.button('Register', use_container_width=True, key='landing_register'):
                st.session_state.current_page = 'login'
                st.rerun()
                
# ── Login page ────────────────────────────────────────────────────────────────
def show_login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align:center; padding-top:4rem; margin-bottom:2rem;">
            <h1 style="font-size:2.5rem; letter-spacing:-2px;">Fairness Auditor</h1>
            <p style="font-family:'DM Mono',monospace; font-size:12px; color:#608ec7;">
                Automated dataset quality scoring & bias detection
            </p>
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["Login", "Register"])

        with tab1:
            username = st.text_input('Username', key='login_user', placeholder='Enter username')
            password = st.text_input('Password', key='login_pass', type='password', placeholder='Enter password')
            if st.button('Login', use_container_width=True, key='btn_login'):
                if not username or not password:
                    st.error('Please enter both username and password.')
                else:
                    do_login(username, password)

        with tab2:
            new_user = st.text_input('Username', key='reg_user', placeholder='Choose a username')
            new_pass = st.text_input('Password', key='reg_pass', type='password', placeholder='Min 6 characters')
            if st.button('Create Account', use_container_width=True, key='btn_register'):
                if not new_user or not new_pass:
                    st.error('Please fill in both fields.')
                elif len(new_pass) < 6:
                    st.error('Password must be at least 6 characters.')
                else:
                    do_register(new_user, new_pass)


# ── Main app routing ──────────────────────────────────────────────────────────
if not st.session_state.logged_in:
    if st.session_state.current_page == 'login':
        show_login_page()
=======
def logout():
    st.session_state.api_session.post(f'{BASE_URL}/auth/logout')
    for key in list(st.session_state.keys()):
        del st.session_state[key]

if not st.session_state.logged_in:
    if st.session_state.current_page == 'login':
        show_login_page(BASE_URL)
    elif st.session_state.current_page == 'register':
        show_register_page(BASE_URL)
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
    elif st.session_state.current_page == 'info_quality':
        show_info_page('quality')
    elif st.session_state.current_page == 'info_fairness':
        show_info_page('fairness')
    elif st.session_state.current_page == 'info_ai':
        show_info_page('ai')
    elif st.session_state.current_page == 'info_history':
        show_info_page('history')
    else:
        show_landing_page()
else:
<<<<<<< HEAD
    # Sidebar
=======
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
    st.sidebar.markdown(
        "<p style='font-family:Syne,sans-serif; font-size:16px; font-weight:700; color:#ff6f00; margin-bottom:2px;'>Fairness Auditor</p>",
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        f"<p style='font-family:DM Mono,monospace; font-size:11px; color:#608ec7;'>signed in as {st.session_state.username}</p>",
        unsafe_allow_html=True
    )
    st.sidebar.divider()
    st.sidebar.markdown(
        "<p style='font-family:DM Mono,monospace; font-size:10px; letter-spacing:1px; color:#444; text-transform:uppercase;'>Progress</p>",
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        f"<p style='font-family:DM Mono,monospace; font-size:12px; color:{'#ff6f00' if st.session_state.dataset_id else '#333'};'>{'✓' if st.session_state.dataset_id else '○'} Dataset uploaded</p>",
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        f"<p style='font-family:DM Mono,monospace; font-size:12px; color:{'#ff6f00' if st.session_state.quality_result else '#333'};'>{'✓' if st.session_state.quality_result else '○'} Quality checked</p>",
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        f"<p style='font-family:DM Mono,monospace; font-size:12px; color:{'#db1886' if st.session_state.fairness_result else '#333'};'>{'✓' if st.session_state.fairness_result else '○'} Fairness audited</p>",
        unsafe_allow_html=True
    )
    st.sidebar.divider()

    nav_items = [
        ('Upload',          'upload',   'upload'),
        ('Quality Report',  'quality',  'quality'),
        ('Fairness Report', 'fairness', 'fairness'),
        ('History',         'history',  'history'),
    ]

    for label, key, css_key in nav_items:
        is_active = st.session_state.current_page == key
        css_class = f'nav-{css_key}-active' if is_active else f'nav-{css_key}'
        st.sidebar.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
        if st.sidebar.button(label, key=f'nav_{key}', use_container_width=True):
            st.session_state.current_page = key
            st.rerun()
        st.sidebar.markdown('</div>', unsafe_allow_html=True)

    st.sidebar.divider()
    if st.sidebar.button('Logout', use_container_width=True):
        logout()
        st.rerun()

<<<<<<< HEAD
    # Page routing
=======
>>>>>>> 6aa08780c6ead22649d69d286c1030c5c71d05b4
    if st.session_state.current_page == 'upload':
        show_upload_page(BASE_URL)
    elif st.session_state.current_page == 'quality':
        show_quality_page(BASE_URL)
    elif st.session_state.current_page == 'fairness':
        show_fairness_page(BASE_URL)
    elif st.session_state.current_page == 'history':
        show_history_page(BASE_URL)