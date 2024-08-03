import base64
import os
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import prompts


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


def analyze_local_image(image_path: str, model_name: str = "gemini-1.5-flash") -> str:
    """
    Analyze a local image using the specified AI model.

    Parameters:
        image_path (str): The path to the local image file.
        model_name (str): The name of the model to use for analysis. Default is "gemini-1.5-flash".

    Returns:
        str: The response from the AI model.
    """
    

    
    # Load local image and convert it to base64
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    # Create a base64 image string
    base64_image_string = f"data:image/jpeg;base64,{base64_image}"

    # Initialize the model
    llm = ChatGoogleGenerativeAI(model=model_name)

    # Create a message with the base64 image
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": prompts.graph_crq,
            },  # You can optionally provide text parts
            {"type": "image_url", "image_url": base64_image_string},
        ]
    )

    # Invoke the model
    response = llm.invoke([message])
    return response.content

def process_graphs_in_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter for image files (assuming JPEG and PNG only)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    results = ""
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        result = analyze_local_image(image_path)
        results += f"\n **image file:**\n***{image_file}*** \n\n"
        results += result

    with open('file.md', 'w', encoding='utf-8') as f:
        f.write(results)
    return results
