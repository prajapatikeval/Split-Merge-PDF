from pypdf import PdfReader, PdfWriter
import os
reader = PdfReader('Example.pdf')
writer = PdfWriter()

os.chdir('Encryption and Decryption')

# add all pages in writer
for page in reader.pages:
    writer.add_page(page)

# encrypt pdf with password
writer.encrypt("Keval")

# save the new pdf to a file
with open('Encrypted_pdf.pdf', 'wb')as file:
    writer.write(file)
