import os
from functions import create_nodes_and_edges, generate_graphviz_code, extract_code, toMarkdown

def main():
    debug_mode = False  # Set debug_mode to False by default, can be adjusted as needed

    # Placeholder for user input, replace with actual method section text input
    method_text = """Enter your method section text here."""

    if method_text:
        # Create nodes and edges
        method = toMarkdown(method_text)
        nande = create_nodes_and_edges(method)

        # Generate Graphviz code
        llm_response = generate_graphviz_code(nande)

        # Extract and execute the code
        code = extract_code(llm_response)
        
        # Display debug information if debug mode is on
        if debug_mode:
            print("Debug Information")
            print("Nodes and Edges Content:")
            print(nande)
            print("LLM Response Content:")
            print(llm_response)

        # Execute the code
        exec(code)
        
        # Look for the graph.png file
        if os.path.exists("graph.png"):
            print("Generated graph.png file found.")
        else:
            print("Unable to find the generated graph.png file.")
    else:
        print("Please enter the method section text.")

if __name__ == "__main__":
    main()
