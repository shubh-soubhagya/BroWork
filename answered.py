import csv
import os
from dotenv import load_dotenv
from groq import Groq
import re

# Load API key from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=groq_api_key)


def clean_markdown(answer):
    # Remove **bold**, *italics*, `code`, > quotes, and unnecessary markdown syntax
    cleaned = re.sub(r'[*`>#]+', '', answer)
    # Remove extra spaces and newlines
    cleaned = re.sub(r'\n+', '\n', cleaned).strip()
    return cleaned


# Function to generate answer using Groq
def get_answer_from_groq(question, model="compound-beta-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful technical assistant. Answer concisely and clearly in 100 words."},
            {"role": "user", "content": f"{question}"}
        ]
    )
    raw_answer = response.choices[0].message.content.strip()
    cleaned_answer = clean_markdown(raw_answer)
    return cleaned_answer

# Load questions, generate answers, and overwrite same file
def answer_questions_inplace(input_file="questions.csv"):
    updated_rows = []

    # Read existing questions
    with open(input_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames + ["answers"] if "answers" not in reader.fieldnames else reader.fieldnames

        for row in reader:
            question = row["questions_extracted"]
            print(f"🧠 Answering: {question}")
            answer = get_answer_from_groq(question)
            row["answers"] = answer
            updated_rows.append(row)

    # Write back to the same file with answers column
    with open(input_file, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    print(f"\n✅ Answers added to {input_file}")

answer_questions_inplace("questions.csv")
