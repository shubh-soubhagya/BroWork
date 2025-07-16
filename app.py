from question_extraction import extract_text_from_pdf, extract_questions
from question_to_csv import save_questions_to_csv
from ans_in_doc import generate_qna_pdf
from answered import answer_questions_inplace
import csv
import os
from dotenv import load_dotenv
from groq import Groq
import re


# Load API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

file_path = input("Share the file path of the document containing questions: ")


#### Extracting Questions from the PDF files ####

pdf_text = extract_text_from_pdf(file_path)  # You can use this instead of load_text()
questions_extracted = extract_questions(pdf_text)

#### Add Questions to the CSV file ####

save_questions_to_csv(questions_extracted)

#### Answering the Extracted Questions ####

answer_questions_inplace("questions.csv")

#### Saving file in PDF ######

generate_qna_pdf("questions.csv", "questions_answers.pdf")


