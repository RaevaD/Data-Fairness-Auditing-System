import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
import requests
from pages.upload import show_landing_page, show_login_page, show_register_page, show_upload_page
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

p, li, span, div {
    font-family: 'Syne', sans-serif !important;
    color: #ffffff !important;
}

[data-testid="stCaptionContainer"] p {
    font-family: 'DM Mono', monospace !important;
    font-size: 11px !important;
    color: #608ec7 !important;
    letter-spacing: 0.5px !important;
}

.block-container {
    border-top: 2px solid #db1886;
    padding-top: 2rem !important;
    background-color: #030303 !important;
}

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

/* Default button — outline orange */
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

.stProgress > div > div {
    height: 4px !important;
    border-radius: 2px !important;
    background: #ff6f00 !important;
}
.stProgress > div {
    background: #1a1a1a !important;
    border-radius: 2px !important;
}

[data-testid="stSidebar"] {
    background-color: #080808 !important;
    border-right: 1px solid #1a1a1a !important;
}
[data-testid="stSidebar"] * {
    font-family: 'Syne', sans-serif !important;
}

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

[data-testid="stFileUploader"] {
    background: #0a0a0a !important;
    border: 1px dashed #1a1a1a !important;
    border-radius: 8px !important;
}

[data-testid="stAlert"] {
    border-radius: 0 6px 6px 0 !important;
    border-left-width: 3px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 12px !important;
    background: #0a0a0a !important;
}

[data-testid="stDataFrame"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 12px !important;
}

hr {
    border-color: #1a1a1a !important;
}

[data-testid="stToggle"] label {
    font-family: 'Syne', sans-serif !important;
    color: #ff6f00 !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] small {
    font-family: 'DM Mono', monospace !important;
    font-size: 11px !important;
}

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

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'dataset_id' not in st.session_state:
    st.session_state.dataset_id = None
if 'quality_result' not in st.session_state:
    st.session_state.quality_result = None
if 'fairness_result' not in st.session_state:
    st.session_state.fairness_result = None
if 'explanation_result' not in st.session_state:
    st.session_state.explanation_result = None
if 'no_protected_attrs' not in st.session_state:
    st.session_state.no_protected_attrs = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'landing'
if 'api_session' not in st.session_state:
    st.session_state.api_session = requests.Session()

def logout():
    st.session_state.api_session.post(f'{BASE_URL}/auth/logout')
    for key in list(st.session_state.keys()):
        del st.session_state[key]

if not st.session_state.logged_in:
    if st.session_state.current_page == 'login':
        show_login_page(BASE_URL)
    elif st.session_state.current_page == 'register':
        show_register_page(BASE_URL)
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

    if st.session_state.current_page == 'upload':
        show_upload_page(BASE_URL)
    elif st.session_state.current_page == 'quality':
        show_quality_page(BASE_URL)
    elif st.session_state.current_page == 'fairness':
        show_fairness_page(BASE_URL)
    elif st.session_state.current_page == 'history':
        show_history_page(BASE_URL)