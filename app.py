##################################################################################
#################### BROWORK: Your Bro to Solve Your Homework ####################
##################################################################################

# 1. Extract questions from a PDF
# 2. Save questions to a CSV
# 3. Use Groq LLM to answer questions
# 4. Save final Q&A into a formatted PDF

####################################################################################

from agents.question_extraction import extract_text_from_pdf, extract_questions
from doc_conversion.question_to_csv import save_questions_to_csv
from doc_conversion.ans_in_doc import generate_qna_pdf
from agents.answered import answer_questions_inplace
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
    answer_questions_inplace(r"data\questions.csv")

    print("📄 Generating final Q&A PDF...")
    generate_qna_pdf(r"data\questions.csv", "browork_answered.pdf")

    print("✅ Q&A PDF successfully generated as 'browork_answered.pdf'")

except Exception as e:
    print(f"❌ Unexpected error occurred during processing: {e}")
    exit(1)
