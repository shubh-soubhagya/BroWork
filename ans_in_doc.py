# import csv
# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch

# def generate_qna_pdf(csv_file, output_pdf):
#     # Setup PDF
#     c = canvas.Canvas(output_pdf, pagesize=A4)
#     width, height = A4
#     margin = 50
#     y_position = height - margin

#     c.setFont("Helvetica-Bold", 16)
#     c.drawString(margin, y_position, "Question & Answer Sheet")
#     y_position -= 40

#     c.setFont("Helvetica", 12)

#     # Read CSV
#     with open(csv_file, mode="r", encoding="utf-8") as file:
#         reader = csv.DictReader(file)
#         count = 1
#         for row in reader:
#             question = row["questions_extracted"].strip()
#             answer = row["answers"].strip()

#             q_text = f"Q{count}: {question}"
#             a_text = f"Answer: {answer}"

#             # Handle page break
#             if y_position < margin + 100:
#                 c.showPage()
#                 c.setFont("Helvetica", 12)
#                 y_position = height - margin

#             # Write Question
#             c.setFont("Helvetica-Bold", 12)
#             c.drawString(margin, y_position, q_text)
#             y_position -= 20

#             # Write Answer (with basic word wrap)
#             c.setFont("Helvetica", 12)
#             for line in split_text(answer, 100):
#                 c.drawString(margin + 20, y_position, line)
#                 y_position -= 15

#             y_position -= 15  # Space between Q&A
#             count += 1

#     c.save()
#     print(f"\n✅ PDF generated successfully: {output_pdf}")

# def split_text(text, max_chars):
#     """Utility function to wrap text at max_chars length."""
#     words = text.split()
#     lines, line = [], ""
#     for word in words:
#         if len(line) + len(word) + 1 <= max_chars:
#             line += " " + word if line else word
#         else:
#             lines.append(line)
#             line = word
#     if line:
#         lines.append(line)
#     return lines

# # Example usage:
# generate_qna_pdf("questions.csv", "questions_answers.pdf")

# import csv
# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch

# def generate_qna_pdf(csv_file, output_pdf):
#     # Setup PDF
#     c = canvas.Canvas(output_pdf, pagesize=A4)
#     width, height = A4
#     left_margin = 50
#     right_margin = 50
#     usable_width = width - left_margin - right_margin
#     y_position = height - left_margin

#     c.setFont("Helvetica-Bold", 16)
#     c.drawString(left_margin, y_position, "Question & Answer Sheet")
#     y_position -= 40

#     c.setFont("Helvetica", 12)

#     # Read CSV
#     with open(csv_file, mode="r", encoding="utf-8") as file:
#         reader = csv.DictReader(file)
#         count = 1
#         for row in reader:
#             question = row["questions_extracted"].strip()
#             answer = row["answers"].strip()

#             q_text = f"Q{count}: {question}"
#             a_text = f"Answer: {answer}"

#             # Handle page break
#             if y_position < left_margin + 100:
#                 c.showPage()
#                 c.setFont("Helvetica", 12)
#                 y_position = height - left_margin

#             # Write Question
#             c.setFont("Helvetica-Bold", 12)
#             c.drawString(left_margin, y_position, q_text)
#             y_position -= 20

#             # Write Answer (with word wrap respecting margins)
#             c.setFont("Helvetica", 12)
#             for line in split_text(answer, usable_width, c):
#                 c.drawString(left_margin + 20, y_position, line)
#                 y_position -= 15

#             y_position -= 15  # Space between Q&A
#             count += 1

#     c.save()
#     print(f"\n✅ PDF generated successfully: {output_pdf}")

# def split_text(text, usable_width, canvas_obj):
#     """Splits text into lines that fit within usable_width based on text width."""
#     words = text.split()
#     lines = []
#     line = ""

#     for word in words:
#         temp_line = f"{line} {word}".strip()
#         if canvas_obj.stringWidth(temp_line, "Helvetica", 12) <= usable_width:
#             line = temp_line
#         else:
#             lines.append(line)
#             line = word
#     if line:
#         lines.append(line)
#     return lines

# # Example usage:
# generate_qna_pdf("questions.csv", "questions_answers.pdf")

# import csv
# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch

# def generate_qna_pdf(csv_file, output_pdf):
#     # Setup PDF
#     c = canvas.Canvas(output_pdf, pagesize=A4)
#     width, height = A4
#     left_margin = 50
#     right_margin = 50
#     usable_width = width - left_margin - right_margin
#     y_position = height - left_margin

#     c.setFont("Helvetica-Bold", 16)
#     c.drawString(left_margin, y_position, "Question & Answer Sheet")
#     y_position -= 40

#     c.setFont("Helvetica", 12)

#     # Read CSV
#     with open(csv_file, mode="r", encoding="utf-8") as file:
#         reader = csv.DictReader(file)
#         count = 1
#         for row in reader:
#             question = row["questions_extracted"].strip()
#             answer = row["answers"].strip()

#             q_text = f"Q{count}: {question}"
#             a_text = f"Answer: {answer}"

#             # Handle page break
#             if y_position < left_margin + 100:
#                 c.showPage()
#                 c.setFont("Helvetica-Bold", 16)
#                 c.drawString(left_margin, height - left_margin, "Question & Answer Sheet (Continued)")
#                 y_position = height - left_margin - 40
#                 c.setFont("Helvetica", 12)

#             # Write Question with wrapping
#             c.setFont("Helvetica-Bold", 12)
#             for line in split_text(q_text, usable_width, c, "Helvetica-Bold", 12):
#                 c.drawString(left_margin, y_position, line)
#                 y_position -= 15

#             # Write Answer with wrapping
#             c.setFont("Helvetica", 12)
#             for line in split_text(a_text, usable_width, c, "Helvetica", 12):
#                 c.drawString(left_margin + 20, y_position, line)
#                 y_position -= 15

#             y_position -= 20  # Space between Q&As
#             count += 1

#     c.save()
#     print(f"\n✅ PDF generated successfully: {output_pdf}")

# def split_text(text, usable_width, canvas_obj, font_name="Helvetica", font_size=12):
#     """Splits text into lines fitting within usable_width using font measurements."""
#     words = text.split()
#     lines = []
#     line = ""

#     canvas_obj.setFont(font_name, font_size)

#     for word in words:
#         test_line = f"{line} {word}".strip()
#         if canvas_obj.stringWidth(test_line, font_name, font_size) <= usable_width:
#             line = test_line
#         else:
#             lines.append(line)
#             line = word
#     if line:
#         lines.append(line)
#     return lines

# # Example usage:
# generate_qna_pdf("questions.csv", "questions_answers.pdf")

import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_qna_pdf(csv_file, output_pdf):
    # Setup PDF with margins
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    # Margins
    left_margin = 50
    right_margin = 50
    top_margin = 50
    bottom_margin = 100

    usable_width = width - left_margin - right_margin
    y_position = height - top_margin  # start after top margin

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(left_margin, y_position, "Question & Answer Sheet")
    y_position -= 40

    c.setFont("Helvetica", 12)

    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        count = 1
        for row in reader:
            question = row["questions_extracted"].strip()
            answer = row["answers"].strip()

            q_text = f"Q{count}: {question}"
            a_text = f"Answer: {answer}"

            # Page break handling before writing question
            if y_position < bottom_margin + 100:
                c.showPage()
                y_position = height - top_margin
                c.setFont("Helvetica-Bold", 16)
                c.drawString(left_margin, y_position, "Question & Answer Sheet (Continued)")
                y_position -= 40
                c.setFont("Helvetica", 12)

            # Draw Question with word wrap
            c.setFont("Helvetica-Bold", 12)
            for line in split_text(q_text, usable_width, c, "Helvetica-Bold", 12):
                c.drawString(left_margin, y_position, line)
                y_position -= 15

            # Draw Answer with word wrap
            c.setFont("Helvetica", 12)
            for line in split_text(a_text, usable_width, c, "Helvetica", 12):
                c.drawString(left_margin + 20, y_position, line)
                y_position -= 15

            y_position -= 20  # spacing between questions
            count += 1

    c.save()
    print(f"\n✅ PDF generated successfully: {output_pdf}")

def split_text(text, usable_width, canvas_obj, font_name="Helvetica", font_size=12):
    """Splits text based on visual width to respect margins."""
    words = text.split()
    lines = []
    line = ""
    canvas_obj.setFont(font_name, font_size)

    for word in words:
        test_line = f"{line} {word}".strip()
        if canvas_obj.stringWidth(test_line, font_name, font_size) <= usable_width:
            line = test_line
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines

# Example usage
generate_qna_pdf("questions.csv", "questions_answers.pdf")
