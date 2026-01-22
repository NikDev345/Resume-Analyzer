import spacy

nlp = spacy.load("en_core_web_sm")

SKILL_MAP = {
    "python": ["python"," py"],
    "java": ["java"],
    "sql": ["sql", "mysql", "postgresql"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "nlp": ["nlp", "natural language processing"],
    "fastapi": ["fastapi"," fast api"],
    "django": ["django"],
    "docker": ["docker"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"]
}

def extract_skills(text):
    text = text.lower()
    doc = nlp(text)
    found = set()

    for canonical, variants in SKILL_MAP.items():
        for v in variants:
            if v in text:
                found.add(canonical)

    return sorted(found)
