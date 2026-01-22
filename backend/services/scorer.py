def score_resume(sections, skills):
    score = 0

    # Section presence
    if "experience" in sections:
        score += min(len(sections["experience"]) * 1.5, 30)

    if "projects" in sections:
        score += min(len(sections["projects"]) * 1.2, 20)

    if "education" in sections:
        score += 10

    # Skill depth
    score += min(len(skills) * 4, 40)

    return int(min(score, 100))
