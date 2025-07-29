"""
Interface Module

Handles all Streamlit UI rendering related to user input:
- API keys
- Model selection
- Dataset preview

Block 1: Sidebar configuration for API keys and model selection
Block 2: Displaying uploaded dataset with toggle
"""

import streamlit as st

# Block 1: Sidebar controls
def setup_sidebar():
    st.sidebar.header("🔑 API Keys and Model Configuration")

    # Input field for Together AI key
    st.session_state.together_api_key = st.sidebar.text_input("Together AI API Key", type="password")
    st.sidebar.markdown("[Get API Key](https://api.together.ai/signin)")

    # Input field for E2B key
    st.session_state.e2b_api_key = st.sidebar.text_input("E2B API Key", type="password")
    st.sidebar.markdown("[Get E2B API Key](https://e2b.dev/docs/legacy/getting-started/api-key)")

    # Dropdown for selecting LLM
    model_options = {
        "Meta-Llama 3.1 405B": "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        "DeepSeek V3": "deepseek-ai/DeepSeek-V3",
        "Qwen 2.5 7B": "Qwen/Qwen2.5-7B-Instruct-Turbo",
        "Meta-Llama 3.3 70B": "meta-llama/Llama-3.3-70B-Instruct-Turbo"
    }

    selected_model = st.selectbox("Select Model", list(model_options.keys()))
    st.session_state.model_name = model_options[selected_model]

# Block 2: Dataset preview
def show_dataset_preview(df):
    st.write("Dataset:")
    if st.checkbox("Show full dataset"):
        st.dataframe(df)
    else:
        st.write("Preview (first 5 rows):")
        st.dataframe(df.head())
