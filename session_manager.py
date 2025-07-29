"""
Session Manager

Block 1: Define helper to initialize session variables
"""

import streamlit as st

# Block 1: Set default session values if not already defined
def initialize_session_state():
    if 'together_api_key' not in st.session_state:
        st.session_state.together_api_key = ''
    if 'e2b_api_key' not in st.session_state:
        st.session_state.e2b_api_key = ''
    if 'model_name' not in st.session_state:
        st.session_state.model_name = ''
