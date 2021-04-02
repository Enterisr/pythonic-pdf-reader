from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import resolve1

import pyttsx3
def read_pdf_text(path,retured_value):
    output_string = StringIO()
    if path:
        with open(path,'rb') as file:
            parser = PDFParser(file)
            fileDoc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            fileLen = resolve1(fileDoc.catalog['Pages'])['Count']
            counter = 0
            for page in PDFPage.create_pages(fileDoc):
                
                precent = int(round(((counter+1)/fileLen)*100))
                print(f"reading at {precent}%")
                interpreter.process_page(page)
                counter+=1    
    retured_value = output_string
    
    return retured_value

def onEnd(name, completed):
   print('done!')

def FormatToVoice(string_to_read,file_dest):
    engine = pyttsx3.init()  # object creation
    string_to_read.replace('/n', "")
    engine.setProperty('rate', 150)
    engine.connect('finished-utterance', onEnd)
    engine.save_to_file(string_to_read, file_dest)

    engine.runAndWait()
