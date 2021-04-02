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
        file_strio = Analyzer.read_pdf_text(file_name, returned_value)
        file_string =  file_strio.getvalue()
        if file_string:
            new_file_name = file_name.replace('.pdf', '.mp3')
            self.label.config(text=f"converting to mp3 in path {new_file_name}",fg="blue")
            Analyzer.FormatToVoice(file_string, new_file_name)
            self.label.config(text=f"done! you can hear the file now!",fg="green")
            os.startfile(new_file_name)
        else:
            self.label.config(text=f"Couldn't format file 😒",fg="red")

    

def build_gui():
    main_window = tkinter.Tk() 
    main_window.geometry("500x500")
    main_window.configure(bg="#fffeee")
    main_window.title('pdf to speech')
    label = tkinter.Label(text=" please drop the pdf you want to be converted!", height=20, bg="#fffeee")
    button_font = font.Font(size=12)
    open_file_dialog_button  =tkinter.Button(text="choose file!",fg="#fffeee",bg ="green",height=3,width=30,borderwidth = 0,command = lambda:Worker(label))
    label["font"] = button_font
    open_file_dialog_button["font"] = button_font
    label.pack()
    open_file_dialog_button.pack()
    main_window.mainloop()

build_gui()

