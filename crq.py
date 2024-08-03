from langchain.prompts import PromptTemplate
import summary
import pandas as pd
import util


master = PromptTemplate.from_template("""
### Instructions ###
You will be provided with the method section and the abstract of my study. Your job is to critique them for clarity and reproducibility as follows: 

### Criticism Method ###
{job}

### Abstract ###
{abstract}

### Method Section ###
{method}

### Output Template ###
{template}

### Critique ###

""")




def Critique(file_path, llm):
    summary_prompts = pd.read_csv('Critique_prompts.csv', encoding='latin1')
    outline = util.print_outline(file_path)
    
    def get_target_outline(section, outline, llm):
        chain = get_section | llm
        response = chain.invoke({'section':section,'text':outline})
        return response.content

    results = ""
    for index, row in summary_prompts.iterrows():
        
        title_method = summary.get_target_outline('method', outline, llm)
        title_abstract = summary.get_target_outline('abstract', outline, llm)
        abstract = util.extract_section(file_path, title_abstract)
        method = util.extract_section(file_path, title_method)

        job = row['Method of Criticism']
        Information = row['Name of the Critique']
        template = row['Output Template']
        chain = master | llm
        response = chain.invoke({'job':job,    
                                 'abstract':abstract,
                                 'method':method,
                                 'template':template})
        results += f"\n## {Information}\n"
        results += response.content
        break

    
    
    return results














