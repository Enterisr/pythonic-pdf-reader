from tkinter import filedialog,messagebox
import tkinter 
import Analyzer
import threading
import queue
class Threader(threading.Thread):
####TODO: fix everything!
    def __init__(self, *args, **kwargs):

        threading.Thread.__init__(self, *args, **kwargs)
        self.daemon = True
        self.start()

    def run(self):
        file_name= tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select a pdf",filetypes = (("pdf","*.pdf"),("all files","*.*")))
        messagebox.showinfo("Title",f"analysing {file_name} this may take several minutes...")
        q = queue.Queue()
        Analyzer.read_pdf_text(file_name,q)
        file_string =  q.get()
        new_file_name = file_name.replace('.pdf','.mp3')
        Analyzer.FormatToVoice(file_string,new_file_name)
        tkinter.Label(text="analyzing pdf...",height=20).pack()


def build_gui():
    main_window = tkinter.Tk() 
    main_window.geometry("400x400")
    main_window.configure(bg="#fffeee")
    main_window.title('please stand by...')
    label = tkinter.Label(text=" please drop the pdf you want to be converted!",height=20)
    open_file_dialog_button  =tkinter.Button(text="choose file!",fg="white",bg ="#0366d6",command = lambda:Threader())
    label.pack()
    open_file_dialog_button.pack()
    main_window.mainloop()
def open_file_dialog(label): 
   ''' file_name= tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select a pdf",filetypes = (("pdf","*.pdf"),("all files","*.*")))
    messagebox.showinfo("Title",f"analysing {file_name} this may take several minutes...")
    label.config(text=f"file path:{file_name}")
    q = queue.Queue()
    Threader(file_name=file_name,q=q)
    file_string =  q.get()
    new_file_name = file_name.replace('.pdf','.mp3')
    Analyzer.FormatToVoice(file_string,new_file_name)
    tkinter.Label(text="analyzing pdf...",height=20).pack()

    return file_name
    '''
build_gui()