from pypdf import PdfReader
import os
reader = PdfReader('Example.pdf')

page = reader.pages[31]
count = 1

os.chdir('Extracted_images')
for image in page.images:

    with open(str(count) + image.name, 'wb')as file:
        file.write(image.data)
        count += 1
