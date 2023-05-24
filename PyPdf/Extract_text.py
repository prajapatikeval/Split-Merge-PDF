from pypdf import PdfReader, PdfWriter


reader = PdfReader("Example.pdf")
page = reader.pages[18]
# print(page.extract_text())


''''''
parts = []


def visitor_body(text, cm, tm, font_dict, font_size):
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)


page.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

# print(text_body)
