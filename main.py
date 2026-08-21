#idk much coding just doing my best to get in this club
import json

SKILLS = [
    "machine learning",
    "ml",
    "deep learning",
    "artificial intelligence",
    "ai",
    "data science",
    "data analysis",
    "computer vision",
    "natural language processing",
    "nlp",
    "communication",
    "problem solving"
]

TECHNOLOGIES = [
    "tensorflow",
    "pytorch",
    "opencv",
    "pandas",
    "numpy",
    "scikit-learn",
    "sql",
    "cnn",
    "docker",
    "git",
    "github"
]
TECHNOLOGY_SKILL_MAP = {
    "cnn": "computer vision",
    "opencv": "computer vision",
    "tensorflow": "machine learning",
    "pytorch": "machine learning",
    "pandas": "data analysis",
    "numpy": "data analysis",
    "scikit-learn": "machine learning"
}
LANGUAGES = [
    "python",
    "java",
    "c++",
    "javascript",
    "html",
    "css"
]


def extract_information(text):

    text = text.lower()

    skills = []
    technologies = []
    languages = []
    for skill in SKILLS:
        if skill in text:
            if skill == "ml":
                skills.append("machine learning")
            elif skill == "ai":
                skills.append("artificial intelligence")
            elif skill == "nlp":
                skills.append("natural language processing")
            else:
                skills.append(skill)
    for technology in TECHNOLOGIES:
        if technology in text:
            technologies.append(technology)
        # Infer skills from technologies
    for technology, skill in TECHNOLOGY_SKILL_MAP.items():
        if technology in text:
            skills.append(skill)        
    for language in LANGUAGES:
        if language in text:
            languages.append(language)
    skills = (set(skills))
    skills=list(skills)
    technologies =(set(technologies))
    technologies=list(technologies)
    languages =(set(languages))
    languages=list(languages)

    result = {
        "skills": skills,
        "technologies": technologies,
        "languages": languages
    }

    return result



      
