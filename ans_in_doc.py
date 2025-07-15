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
    bottom_margin = 50

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
            if y_position < bottom_margin + 150:
                c.showPage()
                y_position = height - top_margin
                c.setFont("Helvetica-Bold", 16)
                c.drawString(left_margin, y_position, "")
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
# generate_qna_pdf("questions.csv", "questions_answers.pdf")
