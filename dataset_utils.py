"""
Dataset Utilities

Block 1: Upload user-selected file to E2B sandbox
"""

import streamlit as st

# Block 1: Write file to sandbox
def upload_dataset(code_interpreter, uploaded_file):
    dataset_path = f"./{uploaded_file.name}"
    try:
        code_interpreter.files.write(dataset_path, uploaded_file)
        return dataset_path
    except Exception as e:
        st.error(f"File upload error: {e}")
        raise
