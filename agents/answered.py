import csv
import os
from dotenv import load_dotenv
from groq import Groq
import re

# Load API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

def clean_markdown(answer):
    cleaned = re.sub(r'[*`>#]+', '', answer)
    cleaned = re.sub(r'\n+', '\n', cleaned).strip()
    return cleaned

# def get_answer_from_groq(question, word_limit, model="compound-beta-mini"):
#     response = client.chat.completions.create(
#         model=model,
#         messages=[
#             {"role": "system", "content": f"You are a helpful technical assistant. Answer concisely and clearly in {word_limit} words."},
#             {"role": "user", "content": question}
#         ]
#     )
#     raw_answer = response.choices[0].message.content.strip()
#     return clean_markdown(raw_answer)

def get_answer_from_groq(question, word_limit, model="compound-beta-mini"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": f"You are a helpful technical assistant. Answer concisely and clearly in exactly {word_limit} words. Not more than word limit. Don't give answers in points. Only in paragraphs."},
                {"role": "user", "content": question}
            ]
        )
        raw_answer = response.choices[0].message.content.strip()
        return clean_markdown(raw_answer)

    except Exception as e:
        # Check for common API error patterns
        error_message = str(e)

        if "Rate limit" in error_message or "Too many requests" in error_message:
            raise RuntimeError("❌ Rate limit exceeded. Please wait and try again later.")

        elif "maximum context length" in error_message or "maximum token limit" in error_message:
            raise RuntimeError("❌ Token limit exceeded. Try reducing the word limit or question size.")

        else:
            raise RuntimeError(f"❌ An error occurred while requesting the Groq API: {error_message}")

def answer_questions_inplace(input_file="questions.csv"):
    updated_rows = []

    # Step 1: Read all rows first
    with open(input_file, mode="r", encoding="utf-8") as file:
        reader = list(csv.DictReader(file))
        total_rows = len(reader)

    # Step 2: Take word limits for each question with A1, A2 prompt
    word_limits = []
    print(f"\n📌 Enter word limits for {total_rows} questions:\n")

    for idx in range(total_rows):
        while True:
            try:
                limit = int(input(f"A{idx+1} word limit: "))
                word_limits.append(limit)
                break
            except ValueError:
                print("❗ Invalid input. Please enter a valid number.")

    # Step 3: Process each question and generate answer
    fieldnames = reader[0].keys()
    if "answers" not in fieldnames:
        fieldnames = list(fieldnames) + ["answers"]

    for idx, row in enumerate(reader):
        question = row["questions_extracted"]
        word_limit = word_limits[idx]
        print(f"\n🧠 Answering A{idx+1} ({word_limit} words): {question}")
        answer = get_answer_from_groq(question, word_limit)
        row["answers"] = answer
        updated_rows.append(row)

    # Step 4: Save back to same CSV
    with open(input_file, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    print(f"\n✅ Answers saved to {input_file} with custom word limits.")

# answer_questions_inplace("questions.csv")
