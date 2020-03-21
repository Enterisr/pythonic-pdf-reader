import PyPDF2
import pyttsx3
def read_pdf_text(path,retured_value):
    extracted_text = ""
    if path:
        with open(path,'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            for i in range(reader.numPages):
                page = reader.getPage(i)
                extracted_text = extracted_text + page.extractText()
                precent = int(round(((i+1)/reader.numPages)*100))
                print(f"reading at {precent}%")
            retured_value.put(extracted_text)

def onEnd(name, completed):
   print('finished!!!!')

def FormatToVoice(string_to_read,file_dest):
    engine = pyttsx3.init()  # object creation
    string_to_read.replace('/n', "")
    engine.setProperty('rate', 150)
    engine.connect('finished-utterance', onEnd)
    engine.save_to_file(string_to_read, file_dest)

    engine.runAndWait()
