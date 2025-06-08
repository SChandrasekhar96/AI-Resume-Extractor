import pdfplumber
import re
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group() if match else "Not found"

def extract_phone(text):
    match = re.search(r"(\+91[\s\-]?)?[6-9]\d{9}", text)
    return match.group() if match else "Not found"

def extract_name(text):
    lines = text.strip().split('\n')
    for line in lines[:5]:
        if line and line.replace(" ", "").isalpha() and 1 <= len(line.split()) <= 4:
            return line.strip()
    return "Not found"

def extract_skills_section(text):
    lines = text.split('\n')
    skills_section = []
    capture = False
    for line in lines:
        if not capture and 'skill' in line.lower() and len(line) <= 60:
            capture = True
            continue
        if capture:
            if re.match(r'^[A-Z][A-Za-z\s&]{1,40}$', line.strip()):
                break
            skills_section.append(line.strip())
    return "\n".join(skills_section).strip() if skills_section else "Skills section not found"

def extract_experience_section(text):
    lines = text.split('\n')
    experience_section = []
    capture = False
    experience_keywords = ['experience', 'work history', 'internship', 'employment']
    stop_keywords = ['education', 'certifications', 'projects', 'skills', 'languages', 'contact']

    for line in lines:
        lower_line = line.lower().strip()
        if not capture and any(k in lower_line for k in experience_keywords) and len(lower_line) <= 60:
            capture = True
            continue
        if capture:
            if any(stop in lower_line for stop in stop_keywords) and len(lower_line) <= 60:
                break
            experience_section.append(line.strip())
    return "\n".join(experience_section).strip() if experience_section else "Experience section not found"

def extract_education_section(text):
    lines = text.split('\n')
    education_section = []
    capture = False
    edu_keywords = ['education', 'academic background']
    stop_keywords = ['experience', 'projects', 'skills', 'certifications', 'languages']

    for line in lines:
        lower_line = line.lower().strip()
        if not capture and any(k in lower_line for k in edu_keywords) and len(lower_line) <= 60:
            capture = True
            continue
        if capture:
            if any(stop in lower_line for stop in stop_keywords) and len(lower_line) <= 60:
                break
            education_section.append(line.strip())
    return "\n".join(education_section).strip() if education_section else "Education section not found"

def prioritize_sections(text):
    priority_keywords = ["Skills", "Certifications", "Projects", "Education", "Achievements"]
    sections = text.split('\n')
    top, rest = [], []
    for line in sections:
        if any(k.lower() in line.lower() for k in priority_keywords):
            top.append(line)
        else:
            rest.append(line)
    return "\n".join(top + rest)

def summarize_text(text, max_length=500,min_length=120):
    if not text.strip():
        return "No content to summarize."
    try:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return re.sub(r'\.\s*\.+', '.', summary[0]['summary_text']) 
    except Exception as e:
        return f"Summarization failed: {str(e)}"

def extract_info_from_pdf(pdf_file):
    text = extract_text_from_pdf(pdf_file)
    prioritized_text = prioritize_sections(text)
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Education Section": extract_education_section(text),
        "Skills Section": extract_skills_section(text),
        "Experience Section": extract_experience_section(text),
        "Full Resume Summary": summarize_text(prioritized_text)
    }

# if __name__ == "__main__":
#     path = r"D:\New Downloads\S_Chandra_Sekhar_Resume (3).pdf"
#     data = extract_info_from_pdf(path)
#     for k, v in data.items():
#         print(f"\n{k}:\n{v}")
