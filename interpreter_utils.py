"""
Interpreter Utilities

Block 1: Run Python code inside E2B sandbox
Block 2: Display result (plot, table, image, etc.) in Streamlit
"""

import sys
import io
import contextlib
import base64
from PIL import Image
import pandas as pd
import streamlit as st
from e2b_code_interpreter import Sandbox
from dataset_utils import upload_dataset

# Block 1: Run and capture sandbox output
def code_interpret(interpreter, code):
    with st.spinner('Running code in E2B sandbox...'):
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()

        with contextlib.redirect_stdout(stdout_capture), contextlib.redirect_stderr(stderr_capture):
            exec_result = interpreter.run_code(code)

        if exec_result.error:
            st.error(f"Execution Error: {exec_result.error}")
            return None
        return exec_result.results

# Block 2: Run agent and visualize results
def run_in_sandbox(uploaded_file, query):
    with Sandbox(api_key=st.session_state.e2b_api_key) as code_interpreter:
        dataset_path = upload_dataset(code_interpreter, uploaded_file)
        results, response = chat_with_llm(code_interpreter, query, dataset_path)

        st.subheader("💬 LLM Response")
        st.write(response)

        if results:
            st.subheader("📊 Visualization / Output")
            for result in results:
                if hasattr(result, 'png') and result.png:
                    image = Image.open(io.BytesIO(base64.b64decode(result.png)))
                    st.image(image, caption="Generated Visualization")
                elif hasattr(result, 'figure'):
                    st.pyplot(result.figure)
                elif hasattr(result, 'show'):
                    st.plotly_chart(result)
                elif isinstance(result, (pd.DataFrame, pd.Series)):
                    st.dataframe(result)
                else:
                    st.write(result)
