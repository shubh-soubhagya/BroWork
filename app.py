# # ─────────────────────────────────────────────────────────────────────────────
# # Business Q&A PDF Generator from Document
# # Steps:
# # 1. Extract questions from a PDF
# # 2. Save questions to a CSV
# # 3. Use Groq LLM to answer questions
# # 4. Save final Q&A into a formatted PDF
# # ─────────────────────────────────────────────────────────────────────────────

# # Imports
# from question_extraction import extract_text_from_pdf, extract_questions
# from question_to_csv import save_questions_to_csv
# from ans_in_doc import generate_qna_pdf
# from answered import answer_questions_inplace
# from dotenv import load_dotenv
# from groq import Groq
# import os

# # ───────────────────────────
# # Load API Key
# # ───────────────────────────
# load_dotenv()
# groq_api_key = os.getenv("GROQ_API_KEY")
# client = Groq(api_key=groq_api_key)

# # ───────────────────────────
# # Step 1: Input File Path
# # ───────────────────────────
# file_path = input("📄 Enter the file path of the document containing questions: ")

# # ───────────────────────────
# # Step 2: Extract Questions from PDF
# # ───────────────────────────
# pdf_text = extract_text_from_pdf(file_path)
# questions_extracted = extract_questions(pdf_text)

# # ───────────────────────────
# # Step 3: Save Extracted Questions to CSV
# # ───────────────────────────
# save_questions_to_csv(questions_extracted)

# # ───────────────────────────
# # Step 4: Answer Questions in CSV
# # ───────────────────────────
# answer_questions_inplace("questions.csv")

# # ───────────────────────────
# # Step 5: Generate Final Q&A PDF
# # ───────────────────────────
# generate_qna_pdf("questions.csv", "questions_answers.pdf")

# print("✅ Q&A PDF successfully generated as 'questions_answers.pdf'")

# ─────────────────────────────────────────────────────────────────────────────
# Business Q&A PDF Generator from Document (with Exception Handling)
# ─────────────────────────────────────────────────────────────────────────────

from question_extraction import extract_text_from_pdf, extract_questions
from question_to_csv import save_questions_to_csv
from ans_in_doc import generate_qna_pdf
from answered import answer_questions_inplace

import os
from dotenv import load_dotenv
from groq import Groq

# ───────────────────────────
# Load API Key Safely
# ───────────────────────────
try:
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables. Make sure it's defined in the .env file.")

    client = Groq(api_key=groq_api_key)

except Exception as e:
    print(f"❌ Error loading API Key: {e}")
    exit(1)

# ───────────────────────────
# Input File Path from User
# ───────────────────────────
file_path = input("📄 Enter the file path of the document containing questions: ")

if not os.path.isfile(file_path):
    print("❌ Error: File does not exist. Please check the path and try again.")
    exit(1)

# ───────────────────────────
# Main Q&A Pipeline
# ───────────────────────────
try:
    print("🔍 Extracting text from PDF...")
    pdf_text = extract_text_from_pdf(file_path)

    print("❓ Extracting questions...")
    questions_extracted = extract_questions(pdf_text)

    print("📁 Saving questions to CSV...")
    save_questions_to_csv(questions_extracted)

    print("🧠 Answering questions using Groq LLM...")
    answer_questions_inplace("questions.csv")

    print("📄 Generating final Q&A PDF...")
    generate_qna_pdf("questions.csv", "questions_answers.pdf")

    print("✅ Q&A PDF successfully generated as 'questions_answers.pdf'")

except Exception as e:
    print(f"❌ Unexpected error occurred during processing: {e}")
    exit(1)


