from pypdf import PdfReader

reader = PdfReader('Example.pdf')

for name, content_list in reader.attachments:
    for i, content in enumerate(content_list):
        with open(f"{name}--{i}", 'wb')as file:
            file.write(content)
