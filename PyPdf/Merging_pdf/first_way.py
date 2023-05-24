from pypdf import PdfWriter
from os import chdir
merger = PdfWriter()

chdir("Merging_pdf")

# we are simply merging with the help of list
for pdf in ['Example.pdf', 'meta_pdf.pdf']:
    merger.append(pdf)

merger.write("Merged_pdf.pdf")
merger.close()
