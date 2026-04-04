import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
import requests
from pages.upload import show_upload_page
from pages.quality import show_quality_page
from pages.fairness import show_fairness_page
from pages.history import show_history_page

st.set_page_config(page_title='Fairness Auditing System', layout='wide')

st.markdown("""
<style>
    /* Clean typography */
    h1 { font-weight: 600 !important; letter-spacing: -0.5px; }
    h2 { font-weight: 500 !important; color: #e0e0e0; }
    h3 { font-weight: 500 !important; }

    /* Remove default Streamlit top padding */
    .block-container { padding-top: 2rem !important; }

    /* Cleaner metric cards */
    [data-testid="metric-container"] {
        background: #1e1e2e;
        border: 1px solid #2e2e3e;
        border-radius: 10px;
        padding: 1rem;
    }

    /* Cleaner buttons */
    .stButton > button {
        border-radius: 6px;
        font-weight: 500;
        letter-spacing: 0.3px;
    }

    /* Cleaner sidebar */
    [data-testid="stSidebar"] {
        border-right: 1px solid #2e2e3e;
    }

    /* Progress bars — thinner and cleaner */
    .stProgress > div > div {
        height: 6px !important;
        border-radius: 3px !important;
    }

    /* Info/warning boxes — less rounded, more editorial */
    [data-testid="stAlert"] {
        border-radius: 6px !important;
        border-left-width: 3px !important;
    }
</style>
""", unsafe_allow_html=True)

BASE_URL = 'http://localhost:5000'

# Session state init
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
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'upload'
if 'api_session' not in st.session_state:
    st.session_state.api_session = requests.Session()

def logout():
    st.session_state.api_session.post(f'{BASE_URL}/auth/logout')
    for key in list(st.session_state.keys()):
        del st.session_state[key]

if not st.session_state.logged_in:
    show_upload_page(BASE_URL)
else:
    # Styled sidebar header
    st.sidebar.markdown("## Fairness Auditor")
    st.sidebar.markdown(
        f"<small style='color:#888'>Signed in as <strong>{st.session_state.username}</strong></small>",
        unsafe_allow_html=True
    )
    st.sidebar.divider()

    page = st.sidebar.radio(
        'Navigate',
        ['Upload', 'Quality Report', 'Fairness Report', 'History'],
        index=['Upload', 'Quality Report', 'Fairness Report', 'History'].index(
            {'upload': 'Upload', 'quality': 'Quality Report',
             'fairness': 'Fairness Report', 'history': 'History'}
            .get(st.session_state.current_page, 'Upload')
        )
    )

    st.sidebar.divider()
    if st.sidebar.button('Logout', use_container_width=True):
        logout()
        st.rerun()

    if page == 'Upload':
        st.session_state.current_page = 'upload'
        show_upload_page(BASE_URL)
    elif page == 'Quality Report':
        st.session_state.current_page = 'quality'
        show_quality_page(BASE_URL)
    elif page == 'Fairness Report':
        st.session_state.current_page = 'fairness'
        show_fairness_page(BASE_URL)
    elif page == 'History':
        st.session_state.current_page = 'history'
        show_history_page(BASE_URL)