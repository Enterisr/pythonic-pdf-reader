import PyPDF2
from gtts import gTTS
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

def FormatToVoice(string_to_read,file_dest):
    tts = gTTS(string_to_read)
    tts.save(file_dest)

