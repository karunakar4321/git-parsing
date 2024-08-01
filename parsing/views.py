from django.shortcuts import render
from django.http import HttpResponse


from django.http import JsonResponse

 


import pdfplumber
import re
from jinja2 import Template


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text
def separate_sections(text):
    sections = {
        "Contact Information": "",
        "Summary": "",
        "Education": "",
        "Work History": "",
        "Skills": "",
        "Certifications": "",
        "Training": "",
    }
    # Simple keyword-based separation
    contact_info_match = re.search(r'Contact Information:\n(.*?)(\n\n|$)', text, re.DOTALL)
    if contact_info_match:
        sections["Contact Information"] = contact_info_match.group(1).strip()
    summary_match = re.search(r'Summary:\n(.*?)(\n\n|$)', text, re.DOTALL)
    if summary_match:
        sections["Summary"] = summary_match.group(1).strip()
    education_match = re.search(r'Education\n(.*?)(\n\n|$)', text, re.DOTALL)
    if education_match:
        sections["Education"] = education_match.group(1).strip()
    work_experience_match = re.search(r'Work History\n(.*?)(\n\n|$)', text, re.DOTALL)
    if work_experience_match:
        sections["Work History"] = work_experience_match.group(1).strip()
    skills_match = re.search(r'Skills\n(.*?)(\n\n|$)', text, re.DOTALL)
    if skills_match:
        sections["Skills"] = skills_match.group(1).strip()
    return sections
def home(pdf_path):
    pdf_path = 'Awsresume.pdf'
    resume_text = extract_text_from_pdf(pdf_path)
    sections = separate_sections(resume_text)
    print("sections",sections)
    return JsonResponse(sections)
 