import streamlit as st
import os
import base64
from functions import create_nodes_and_edges, generate_graphviz_code, extract_code

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
                nande = create_nodes_and_edges()

                # Generate Graphviz code
                llm_response = generate_graphviz_code(nande.content)

                # Extract and execute the code
                code = extract_code(llm_response.content)
                
                # Execute the code
                exec(code)
                
                # Look for the graph.pdf file
                if os.path.exists("graph.pdf"):
                    # Display the PDF
                    with open("graph.pdf", "rb") as f:
                        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
                    st.markdown(pdf_display, unsafe_allow_html=True)
                else:
                    st.error("Unable to find the generated graph.pdf file.")

                # Display debug information if debug mode is on
                if debug_mode:
                    st.subheader("Debug Information")
                    st.text("Nodes and Edges Content:")
                    st.code(nande.content)
                    st.text("LLM Response Content:")
                    st.code(llm_response.content)

        else:
            st.warning("Please enter the method section text.")

if __name__ == "__main__":
    main()