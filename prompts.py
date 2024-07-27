from langchain.prompts import PromptTemplate



system_prompt_1 = """
Given a detailed method section from a research paper, your task is to identify and list out the main steps (nodes) and their dependencies (edges). Read through the method section carefully and:
- Identify key activities or processes described in each paragraph or significant sentence.
- Define each activity as a potential node in a graph.
- Determine how these nodes are connected by identifying the dependencies or the flow of information (inputs and outputs) between these steps.
- List each node along with a concise description.
- Map out the edges between these nodes, clearly describing the direction and the relationship (e.g., "provides input for," "depends on").
This will create a structured outline of nodes and edges, preparing for the visualization of this information in a flowchart or graph. Please provide a comprehensive list of all nodes and edges as extracted from the text.

### Example Output:

**Nodes:**
1. **Target Identification** - Investigate literature to identify the mechanism of Lepidium sativum in insulin secretion.
2. **Control Selection** - Select control drugs like Repaglinide and Tolbutamide for comparison.
3. **Ligand Preparation** - Retrieve ligand names and SMILES from literature and prepare using Schrödinger's Ligprep.
4. **Binding Site Identification and Grid Generation** - Identify binding site using SiteMap and generate docking grids with specified settings.
5. **Molecular Docking** - Perform docking of ligands and controls, selecting compounds with favorable docking scores.
6. **Molecular Dynamics** - Execute molecular dynamics simulations using specified settings and analyze the outcomes.

**Edges:**
- **From Target Identification to Control Selection** - "Comparison basis"
- **From Ligand Preparation to Binding Site Identification** - "Preparation for docking"
- **From Binding Site Identification to Molecular Docking** - "Docking grid setup"
- **From Molecular Docking to Molecular Dynamics** - "Selection for dynamics study"
"""

system_prompt_2 = """
### instructions ###
Your job is to write Python code that:
1. Reads the provided list of nodes and edges.
2. Utilizes graphviz to create a directed graph.
3. Adds nodes to the graph with appropriate breif labels.
4. Adds edges between the nodes with descriptions of their relationships.
5. Save the file to graph.png
"""

