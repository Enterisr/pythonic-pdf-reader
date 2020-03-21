from tkinter import filedialog, messagebox
import tkinter.font as font
import tkinter 
import Analyzer
import threading
import queue
import os
class Worker(threading.Thread):
    def __init__(self,label):
        threading.Thread.__init__(self)
        self.daemon = True
        self.label = label
        self.start()

    def run(self):
        file_name= tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select a pdf",filetypes = (("pdf","*.pdf"),("all files","*.*")))
        returned_value = queue.Queue()
        self.label.config(text="analyzing pdf...",fg="#f5862f",height=20)
        Analyzer.read_pdf_text(file_name, returned_value)
        file_string =  returned_value.get()
        new_file_name = file_name.replace('.pdf', '.mp3')
        self.label.config(text=f"converting to mp3 in path {new_file_name}",fg="blue")
        Analyzer.FormatToVoice(file_string, new_file_name)
        self.label.config(text=f"done! you can hear the file now!",fg="green")
        os.startfile(new_file_name)
 

def build_gui():
    main_window = tkinter.Tk() 
    main_window.geometry("400x400")
    main_window.configure(bg="#fffeee")
    main_window.title('pdf to speech')
    label = tkinter.Label(text=" please drop the pdf you want to be converted!", height=20, bg="white")
    button_font = font.Font(size=10)
    open_file_dialog_button  =tkinter.Button(text="choose file!",fg="white",bg ="#0366d6",height=3,width=30,borderwidth = 0,command = lambda:Worker(label))
    label["font"] = button_font
    open_file_dialog_button["font"] = button_font
    label.pack()
    open_file_dialog_button.pack()
    main_window.mainloop()

build_gui()

