# functions.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import re

GROQ_API_KEY = ""

# ChatGroq initialization
chat = ChatGroq(
    temperature=0,
    model_name="gemma2-9b-it",
    max_tokens=1024,
    groq_api_key=GROQ_API_KEY  # Optional if not set as an environment variable
)

# Importing the prompts
from prompts import system_prompt_1, system_prompt_2

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
