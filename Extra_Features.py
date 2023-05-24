'''
def Word_to_pdf():
    convert()


def pdf_to_word():
    def convert():
        old_file = "Sem 5 DE Report.pdf"
        new_file = "new.docx"

        cv = Converter(old_file)
        cv.convert(new_file)
        cv.close()

    windows.destroy()
    pdf_to_word_windows = Tk()
    pdf_to_word_windows.geometry("450x200")
    pdf_to_word_windows.title("PDF TO WORD")

    label = Label(pdf_to_word_windows, text="Click the Button to browse the Files", font=('Georgia 13'))
    label.place(x=100, y=0)
    btn = Button(pdf_to_word_windows, text="Choose File", width=25, command=Open_file)
    btn.place(x=135, y=50)

    convert_btn = Button(
        pdf_to_word_windows, text="Convert Pdf Into Word", width=25, command=convert)
    convert_btn.place(x=135, y=100)
    pdf_to_word_windows.mainloop()

'''

