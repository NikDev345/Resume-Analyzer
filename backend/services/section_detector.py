import re

SECTION_HEADERS = {
    "experience": ["experience", "work experience", "employment"],
    "education": ["education", "academics"],
    "skills": ["skills", "technical skills"],
    "projects": ["projects", "personal projects"]
}

def detect_sections(text):
    sections = {}
    lines = text.lower().split("\n")

    current_section = None
    for line in lines:
        for section, keywords in SECTION_HEADERS.items():
            if any(k in line for k in keywords):
                current_section = section
                sections[current_section] = []
        if current_section:
            sections[current_section].append(line)

    return sections
