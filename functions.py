# functions.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from prompts import system_prompt_1, system_prompt_2
from input import method_1, method_2
import re

GROQ_API_KEY = "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"
def create_chat_groq(model_name, max_tokens=1024):
    return ChatGroq(
        temperature=0,
        model_name=model_name,
        max_tokens=max_tokens,
        groq_api_key=GROQ_API_KEY
    )

def create_chain(chat, system_prompt, text):
    prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", text)])
    return prompt | chat

def invoke_chain(chain):
    return chain.invoke({})

def extract_code(llm_response):
    pattern = re.compile(r'```python(.*?)```', re.DOTALL)
    match = pattern.search(llm_response)
    if match:
        return match.group(1).strip()
    else:
        return "No Python code found in the response."

def create_nodes_and_edges():
    chat = create_chat_groq("mixtral-8x7b-32768")
    chain = create_chain(chat, system_prompt_1, method_2)
    return invoke_chain(chain)

def generate_graphviz_code(nande_content):
    chat = create_chat_groq("mixtral-8x7b-32768")
    chain = create_chain(chat, system_prompt_2, nande_content)
    return invoke_chain(chain)

def main():
    # Create nodes and edges
    nande = create_nodes_and_edges()

    # Generate Graphviz code
    llm_response = generate_graphviz_code(nande.content)

    # Extract and execute the code
    code = extract_code(llm_response.content)
    exec(code)

if __name__ == "__main__":
    main()