import PyPDF2
from gtts import gTTS
import os
from tkinter import filedialog
import tkinter as tk

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF dosyaları", "*.pdf")])
    if not file_path:
        return
    with open(file_path, 'rb') as file:
        pdfReader = PyPDF2.PdfReader(file)
        num_pages = len(pdfReader.pages)
        if num_pages == 0:
            print("PDF dosyasında yeterli sayfa yok.")
            return
        text = ''
        for page_num in range(num_pages):
            page = pdfReader.pages[page_num]
            text += page.extract_text()
        language = 'tr'
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("output.mp3")
        os.system("start output.mp3")

root = tk.Tk()
root.title("PDF Seslendirme")

button = tk.Button(root, text="Dosya Seç", command=open_file)
button.pack(pady=20)

root.mainloop()
