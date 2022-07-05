from logging import root
import os
from tkinter import filedialog
import PyPDF2


root.directory = filedialog.askdirectory()

route = root.directory+'/'

constancias = os.listdir(route)

for constancia in constancias:
    if constancia[-3:] == 'pdf': # verifica Si el archivo es un pdf por si hay mas archivos o carpetas que no sean pdf
        pdfFileObject   = open(route+constancia,'rb')
        pdfReader       = PyPDF2.PdfFileReader(pdfFileObject)
        pageObject      = pdfReader.getPage(0)
        text            = pageObject.extractText()
        textLength      = len(text)
        
        for letter in range(textLength):
            accountNumber   = "" # reinicia account number
            if text[letter]=="C" and text[letter+1]=="t" and text[letter+2]=="a" and text[letter+3]==".":
                for i in range(letter+4,letter+20):# recorre los siguientes 20 caracteres
                    if text[i]==",": # si encuentra una coma, termina el account number
                        break
                    else:
                        accountNumber += text[i] # si no, agrega el caracter al account number
                accountNumber = accountNumber.strip()# quita los espacios al inicio y al final
                pdfFileObject.close()
                os.rename(route+constancia,route+accountNumber+'.pdf') # renombra el archivo
                break # termina el for para que no se siga buscando