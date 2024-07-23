import streamlit as st
import os
import base64
from functions import create_nodes_and_edges, generate_graphviz_code, extract_code, toMarkdown

def main():
    st.title("Scientific Paper Method Visualizer")

    # Debug mode toggle at the top
    debug_mode = st.checkbox("Debug Mode", value=False)

    # User input
    method_text = st.text_area("Enter the method section of your scientific paper:", height=200)

    if st.button("Generate Visualization"):
        if method_text:
            with st.spinner("Processing..."):
                # Create nodes and edges
                method = toMarkdown(method_text)

                nande = create_nodes_and_edges(method)

                # Generate Graphviz code
                llm_response = generate_graphviz_code(nande)

                # Extract and execute the code
                code = extract_code(llm_response)
                
                # Display debug information if debug mode is on
                if debug_mode:
                    st.subheader("Debug Information")
                    st.text("Nodes and Edges Content:")
                    st.code(nande)
                    st.text("LLM Response Content:")
                    st.code(llm_response)

                
                # Execute the code
                exec(code)
                
                # Look for the graph.png file
                if os.path.exists("graph.png"):
                    # Display the PNG image
                    st.image("graph.png", caption="Generated Graph", use_column_width=True)
                else:
                    st.error("Unable to find the generated graph.png file.")

        else:
            st.warning("Please enter the method section text.")

if __name__ == "__main__":
    main()