import PyPDF2
from gtts import gTTS
def read_pdf_text(path):
    extracted_text = ""
    with open(path,'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        for i in range(reader.numPages):
            page = reader.getPage(i)
            extracted_text = extracted_text + page.extractText()
            precent = int(round(((i+1)/reader.numPages)*100))
            print(f"reading at {precent}%")
    return extracted_text

def FormatToVoice(string_to_read,file_dest):
    tts = gTTS(string_to_read)
    tts.save(file_dest)

