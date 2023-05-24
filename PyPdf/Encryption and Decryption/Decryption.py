from pypdf import PdfReader, PdfWriter
from os import chdir

reader = PdfReader('Example.pdf')
writer = PdfWriter()

chdir('Encryption and Decryption')

if reader.is_encrypted:
    reader.decrypt('keval')

    for page in reader.pages:
        writer.add_page(page)

    with open('Decrypted_pdf.pdf', 'wb')as file:
        writer.write(file)

else:
    print("File is already decrypted".center(50, '-'))
