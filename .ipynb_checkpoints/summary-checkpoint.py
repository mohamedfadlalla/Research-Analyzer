from langchain.prompts import PromptTemplate
import util
import pandas as pd



Background = PromptTemplate.from_template("""
###instructions###
You will be provided with the Introduction section of a secentific paper your job is to  Briefly describe the context or background of the research and clearly state the objectives or research questions the study aims to address. 


###Introduction section###
{text}

###Output###
""")

get_section = PromptTemplate.from_template("""
###instructions###
You will receive an outline of a scientific paper in the format shown in the expected input. Extract and present only the highest level heading corresponding to the {section} section, with no other output.


###Example###
Extract the method section
**Expected Input:**
#abstract
#introduction
#method
##method 1
#results
#conclusion

**Expected Output:**
#method

###Input###
{text}

###Output###
""")

master = PromptTemplate.from_template("""
###instructions###
You will be provided with the {section} section of a secentific paper.
your *job* is to  {job} 

**Important** give the output directly don't be verbose

###{section}###
{text}

###Output###
""")

def get_target_outline(section, outline, llm):
    chain = get_section | llm
    response = chain.invoke({'section':section,'text':outline})
    return response.content

def summarize(file_path, llm):
    summary_prompts = pd.read_csv('summary_prompts.csv')
    outline = util.print_outline(file_path)
    
    def get_target_outline(section, outline, llm):
        chain = get_section | llm
        response = chain.invoke({'section':section,'text':outline})
        return response.content
        
    # Function to check if the title contains reference-related words and count DOI occurrences
    reference_keywords = ['References', 'Citation', 'Citations', 'Bibliography', 'References', 'Reference']
    
    # Check if the title contains any reference-related words
    def is_reference_title(title):
        return any(keyword.lower() in title.lower() for keyword in reference_keywords)
    
    def count_doi(content):
        return content.lower().count('doi')   
    
    results = ""
    for index, row in summary_prompts.iterrows():
        if is_reference_title(row['Typical Section']):
            Information = row['Information']
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            citations = count_doi(content)
            
            results += f"\n## {Information}\n"
            results += f"Number of citaiton: {citations}"


        else:
            section = row['Typical Section']
            job = row['Description']
            Information = row['Information']
            section_title = get_target_outline(section, outline, llm)
            content = util.extract_section(file_path, section_title)
            chain = master | llm
            response = chain.invoke({'section':section,'text':content, 'job':job})
            results += f"\n## {Information}\n"
            results += response.content
            break

    
    
    return results
 
