"""
LLM Handler

Block 1: Extract Python code block from LLM response
Block 2: Send prompt to Together AI and return code + text
"""

import re
import streamlit as st
from together import Together
from interpreter_utils import code_interpret

# Block 1: Extract the Python code block from triple-backtick markdown format
pattern = re.compile(r"```python\n(.*?)\n```", re.DOTALL)

def match_code_blocks(llm_response: str) -> str:
    match = pattern.search(llm_response)
    return match.group(1) if match else ""

# Block 2: Construct prompt and fetch code using Together AI
def chat_with_llm(code_interpreter, user_message, dataset_path):
    system_prompt = f"""You're a Python data scientist. Use dataset at '{dataset_path}' to answer user query. Use Python code in your response."""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]

    with st.spinner('Getting response from Together AI LLM...'):
        client = Together(api_key=st.session_state.together_api_key)
        response = client.chat.completions.create(
            model=st.session_state.model_name,
            messages=messages,
        )
        response_message = response.choices[0].message.content
        python_code = match_code_blocks(response_message)

        if python_code:
            results = code_interpret(code_interpreter, python_code)
            return results, response_message
        else:
            st.warning("⚠️ No Python code found.")
            return None, response_message
