from pypdf import PdfWriter, PdfReader
import os

os.chdir('Merging_pdf')

reader = PdfReader('Example.pdf')
merger = PdfWriter()

input1 = open('Example.pdf', 'rb')
input2 = open('meta_pdf.pdf', 'rb')

# add the first 3 pages of input 1 document to output
merger.append(fileobj=input1, pages=(0, 3))

# insert the first page of input 2 into the output beginning after the second page
merger.merge(position=0, fileobj=input2, pages=(39, 40))


# merger.append(input1) we can also append entire file

output = open('merged_2_pdf.pdf', 'wb')
merger.write(output)

merger.close()
output.close()


writer = PdfWriter()
writer.append(reader, "1 to 10 pages", [0, 9])

with open("1_and_10.pdf", 'wb')as file:
    writer.write(file)
