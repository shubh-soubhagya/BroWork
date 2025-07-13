from pdf_text import extract_text_from_pdf
from question_extraction import extract_questions


pdf_text = extract_text_from_pdf("Question.pdf")  # You can use this instead of load_text()
questions_extracted = extract_questions(pdf_text)