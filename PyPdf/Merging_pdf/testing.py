import argparse
import random
from pypdf import PdfWriter


def merge(self,first,second,output):
  if output == None:
    pass
  merger = PdfWriter()

  for pdf in [first,second]:
    merger.append(pdf)

  merger.write(output)
  merger.close()

parser = argparse.ArgumentParser()

parser.add_argument("First_file","Give first pdf file to merge")
parser.add_argument("Second_file","Give Second pdf file to merge")
parser.add_argument("-o","-optional","Merged file name",default=None)

args = parser.parse_args()

print(args.first_file)
print(args.second_file)
print(args.o)

merge(args.first_file,args.second_file,args.o)