
# gui.py

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import re
from prompts import system_prompt_1, system_prompt_2


GROQ_API_KEY="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"


# ChatGroq initialization
chat = ChatGroq(
    temperature=0,
    model_name="gemma2-9b-it",
    max_tokens=1024,
    groq_api_key=GROQ_API_KEY  # Optional if not set as an environment variable
)

def generate_prompt(prompt_text, user_input):
    return ChatPromptTemplate.from_messages([("system", prompt_text), ("human", user_input)])

def extract_code(llm_response):
    # Define the pattern to match the Python code block
    pattern = re.compile(r'```python(.*?)```', re.DOTALL)

    # Search for the code block
    match = pattern.search(llm_response)

    if match:
        # Extract the code
        code = match.group(1).strip()
        return code
    else:
        return "No Python code found in the response."

st.title("Scientific Method Visualization")

user_input = st.text_area("Paste your scientific method here:")

if st.button("Generate Visualization"):
    if user_input:
        prompt = generate_prompt(system_prompt_1, user_input)
        chain = prompt | chat
        llm_response = chain.invoke({})

        # Print the response content
        st.text_area("LLM Response", llm_response.content, height=200)

        code = extract_code(llm_response.content)
        exec(code)

        st.image(display(dot), caption='Generated Graph', use_column_width=True)
    else:
        st.error("Please paste your scientific method in the text area.")
