from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os 
from prompts import system_prompt_1, system_prompt_2
from input import method_1, method_2
import re


# setup google gemini api keys
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

gem1 = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GOOGLE_API_KEY, temperature=0.4, convert_system_message_to_human=True)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GOOGLE_API_KEY, temperature=0.3, convert_system_message_to_human=True)

def create_nodes_and_edges(method):
    create_nodes = ChatPromptTemplate.from_messages([("system", system_prompt_1,),
                                               ("human", method),])
    chain = create_nodes | gem1
    response = chain.invoke({}).content
    return response


def extract_code(llm_response):
    pattern = re.compile(r'```python(.*?)```', re.DOTALL)
    match = pattern.search(llm_response)
    if match:
        return match.group(1).strip()
    else:
        return "No Python code found in the response."


def generate_graphviz_code(nande_content):
    create_nodes = ChatPromptTemplate.from_messages([("system", system_prompt_2,),
                                               ("human", nande_content),])
    chain = create_nodes | llm
    response = chain.invoke({}).content
    return response

def main():
    # Create nodes and edges
    nande = create_nodes_and_edges(method_1)

    # Generate Graphviz code
    llm_response = generate_graphviz_code(nande)

    # Extract and execute the code
    code = extract_code(llm_response)
    exec(code)

if __name__ == "__main__":
    main()