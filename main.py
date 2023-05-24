from tkinter import *
from tkinter import filedialog, messagebox
from pypdf import PdfWriter, PdfReader
import os


filepath = []  # getting filepath and storing in a list
split_file = "" # storing filepath into string

def Open_file():
    '''For Opening File and save the path of that opened file into a list'''
    global filepath,split_file
    file = filedialog.askopenfilename(initialdir="E:\\", title="Choose File", filetypes=(
        ("PDF files", "*.pdf"), ("Word files", "*.docx")))
    filepath.append(file)
    split_file = file

def Merge_pdf():
    '''Creating Merging Page'''
    windows.destroy()
    merge_windows = Tk()
    merge_windows.geometry("350x150")
    merge_windows.title("Merge PDF")

    label = Label(
        merge_windows, text="Click the Button to browse the Files", font=('Georgia 13'))
    label.pack()
    btn = Button(merge_windows, text="Choose First File",
                 width=25, command=Open_file)
    btn1 = Button(merge_windows, text="Choose Second File",
                  width=25, command=Open_file)
    btn.pack()
    btn1.pack()

    def Merge():
        '''Get two file path and merge them and store in third file'''
        try:
            merger = PdfWriter()
            merger.append(fileobj=filepath[0])
            merger.append(fileobj=filepath[1])
            value = 1
            if os.path.exists(f"Merged_{filepath[0].split('/')[-1]}"):
                output = open(
                    f"{value}_Merged_{filepath[0].split('/')[-1]}", "wb")
                value = value + 1
            else:
                output = open(f"Merged_{filepath[0].split('/')[-1]}", "wb")
            merger.write(output)
            output.close()
            merger.close()
            merge_windows.destroy()
        except FileNotFoundError:
            messagebox.showerror("Error", "File Not Uploaded")
        except IndexError:
            messagebox.showerror("Error", "File Not Uploaded")

    merge_btn = Button(merge_windows, text="Merge", width=25, command=Merge)
    merge_btn.pack(pady=20)

    merge_windows.mainloop()


def Split_pdf():
    '''Creating Split Page'''
    windows.destroy()
    split_windows = Tk()
    split_windows.geometry("450x200")
    split_windows.title("Split PDF")

    label = Label(
        split_windows, text="Click the Button to browse the Files", font=('Georgia 13'))
    label.grid(row=0, column=1, pady=2)
    btn = Button(split_windows, text="Choose First File",width=25, command=Open_file)
    btn.grid(row=2, column=1)

    def split():
        '''Getting one file path and split into a part and save into an another file'''
        def check_length():
            reader = PdfReader(filepath[0])
            pages = len(reader.pages)
            return pages + 1
        
        try:
            a = int(item1.get()) 
        except:
            a = 0 
        try:
            b = int(item2.get())
        except:
            b = check_length()

        if a > b:
            messagebox.showerror("Error", "Choose Appropriate Ending Index")

        else:
            try:
                splitter = PdfWriter()
                splitter.append(fileobj=split_file, pages=(a-1, b-1))

                value = 1
                if os.path.exists(f"Splitted_{split_file.split('/')[-1]}"):
                    output = open(
                        f"{value}_Splitted_{split_file.split('/')[-1]}", "wb")
                    value = value + 1
                else:
                    output = open(
                        f"Splitted_{split_file.split('/')[-1]}", "wb")
                splitter.write(output)
                output.close()
                splitter.close()
                split_windows.destroy()
            except FileNotFoundError:
                messagebox.showerror("Error", "No File Loaded")
            except IndexError:
                messagebox.showerror("Error", f"Index Number Out Of Bound Length of file is {check_length()}")

    item1 = IntVar()
    item2 = IntVar()

    label_btn = Label(split_windows, text="Starting Index : ")
    label_btn.grid(row=3, column=0)
    label_btn1 = Label(split_windows, text="Ending Index  : ")
    label_btn1.grid(row=4, column=0)
    item1 = Spinbox(split_windows, from_=1, to=1000, width=5)
    item1.grid(row=3, column=1)

    item2 = Spinbox(split_windows, from_=1, to=1000, width=5)
    item2.grid(row=4, column=1)

    split_btn = Button(split_windows, text="Split", width=25, command=split)
    split_btn.grid(row=5, column=1)
    split_windows.mainloop()


def Choose_Option():
    '''Created dictionary type function so we don't need to use if,else'''
    funcs: dict = {1: Merge_pdf, 2: Split_pdf}
    final = funcs.get(radio.get())
    final()


if __name__ == "__main__":
    '''Creating Main Page With Options'''
    windows = Tk()
    windows.geometry("350x140")

    label = Label(windows, text="Choose Option", font=('Georgia 13'))
    label.pack()
    radio = IntVar()
    options = ["Merge PDF", "Split PDF"]
    for value, text in enumerate(options, start=1):
        Radiobutton(windows, text=text, variable=radio,
                    value=value).pack(anchor=W)

    windows.title("PDF")
    Continue_btn = Button(windows, text="Continue",
                          width=25, command=Choose_Option, border=2)
    Continue_btn.pack()
    windows.mainloop()
