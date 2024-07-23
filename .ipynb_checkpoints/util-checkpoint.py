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

    with open(file_path, 'r') as file:
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