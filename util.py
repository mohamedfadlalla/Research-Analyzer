import re

def extract_outline(file_path):
    outline = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            header_match = re.match(r'^(#+)\s+(.*)', line)
            if header_match:
                level = len(header_match.group(1))
                title = header_match.group(2)
                outline.append((header_match.group(1), title))
    return outline

def print_outline(file_path):
    lst = []
    outline = extract_outline(file_path)
    for hashes, title in outline:
        lst.append(hashes + ' ' + title)
    return lst
    

# file_path = 'manuscript.md'
# outline = extract_outline(file_path)
# print_outline(outline)


def extract_section(file_path, section_title):
    section_content = []
    inside_section = False
    section_level = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            header_match = re.match(r'^(#+)\s+(.*)', line)
            if header_match:
                level = len(header_match.group(1))
                title = header_match.group(2)

                if inside_section:
                    if level <= section_level:
                        break
                if header_match.group(1) + ' ' + title == section_title:
                    inside_section = True
                    section_level = level

            if inside_section:
                section_content.append(line)

    return ''.join(section_content)


from markdown_it import MarkdownIt
import pandas as pd

def split_into_sections_from_file(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        md_text = file.read()
    
    md = MarkdownIt()
    tokens = md.parse(md_text)
    
    sections = []
    current_section = {'title': None, 'content': ''}
    
    for i, token in enumerate(tokens):
        if token.type == 'heading_open':
            if current_section['title'] or current_section['content']:
                sections.append(current_section)
            level = int(token.tag[1])  # Get the heading level (e.g., 1 for h1, 2 for h2, etc.)
            title = next(tokens[i + 1].content for t in tokens if t.type == 'inline')
            current_section = {'title': f'{"#"*level} {title}', 'content': ''}
        elif token.type == 'inline' and token.content:
            current_section['content'] += token.content + '\n'
        elif token.type not in ('heading_close'):
            current_section['content'] += token.markup + '\n'
    
    if current_section['title'] or current_section['content']:
        sections.append(current_section)
    
    return sections

def create_dataframe_from_sections(file_path):
    sections = split_into_sections_from_file(file_path)
    df = pd.DataFrame(sections, columns=['title', 'content'])
    return df

def generate_summary(content):
    system = """
###instructions###
You are a sammarizer you job is to sammarize any input into a structured markdown sammary that is comberhencive.

## don't include a conclusion section

"""

    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", content)])
    
    chain = prompt | llm
    response = chain.invoke({})
    return response.content