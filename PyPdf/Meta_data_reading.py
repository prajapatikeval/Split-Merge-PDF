from pypdf import PdfReader, PdfWriter


'''reading metadata'''
reader = PdfReader("Example.pdf")

meta = reader.metadata

print(len(reader.pages))

# all of the following could be none
print(meta.author)
print(meta.creator)
print(meta.producer)
print(meta.subject)
print(meta.title)
print(meta.modification_date)


'''Writing metadata'''

writer = PdfWriter()

# add all page to the writer
for page in reader.pages:
    writer.add_page(page)

# add the meta data
writer.add_metadata = {
    "/Author": "Keval",
    "/Producer": "Keval",
}

# save the new PDF to file
with open("meta_pdf.pdf", 'wb')as file:
    writer.write(file)
