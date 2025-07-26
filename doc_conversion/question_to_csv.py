import csv
from agents.question_extraction import extract_questions
from extraction.pdf_text import extract_text_from_pdf

pdf_text = extract_text_from_pdf("Question.pdf")
questions_extracted = extract_questions(pdf_text)

import csv

def save_questions_to_csv(questions_extracted, output_file=r"data\questions.csv"):
    """
    Takes a multi-line string of questions and saves each question as a row in a CSV file. 
    Parameters:
    - questions_extracted (str): String with questions separated by newlines.
    - output_file (str): File name to save the questions to.
    """
    question_list = [q.strip() for q in questions_extracted.split('\n') if q.strip()]

    with open(output_file, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["questions_extracted"])  # Header
        for question in question_list:
            writer.writerow([question])

# save_questions_to_csv(questions_extracted)

