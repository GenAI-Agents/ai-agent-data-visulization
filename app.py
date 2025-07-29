"""
AI Data Visualization Agent – Streamlit App
Author: Refactored for educational use

This is the entry point for the AI agent app. It integrates the user interface,
session state management, file upload, and LLM-based agent execution.

Block 1: Import required modules and helper components
Block 2: Define the main app function
Block 3: Handle file upload, data preview, and LLM querying
"""

# Block 1: Import necessary libraries and modular components
import streamlit as st
from interface import setup_sidebar, show_dataset_preview
from session_manager import initialize_session_state
from dataset_utils import upload_dataset
from llm_handler import chat_with_llm
from interpreter_utils import run_in_sandbox
import pandas as pd

# Block 2: Main app function that runs Streamlit UI
def main():
    st.set_page_config(page_title="📊 AI Data Visualization Agent", layout="wide")
    st.title("📊 AI Data Visualization Agent")
    st.write("Upload your dataset and ask questions about it!")

    # Block 2.1: Initialize all session variables
    initialize_session_state()

    # Block 2.2: Load API key input and model selection UI
    setup_sidebar()

    # Block 3.1: Let user upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Block 3.2: Load and display data preview
        df = pd.read_csv(uploaded_file)
        show_dataset_preview(df)

        # Block 3.3: Accept user query in natural language
        query = st.text_area("What would you like to know about your data?",
                             "Can you compare the average cost for two people between different categories?")

        # Block 3.4: Process query when button is clicked
        if st.button("Analyze"):
            if not st.session_state.together_api_key or not st.session_state.e2b_api_key:
                st.error("Please enter both API keys in the sidebar.")
            else:
                run_in_sandbox(uploaded_file, query)

# Entry point
if __name__ == "__main__":
    main()
