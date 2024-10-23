


import PyPDF2

pdfFlieObj = open('C:/Users/Dhayanidhi/Documents/Data_analyst_Steinbeis.pdf', 'rb')


pdfReader = PyPDF2.PdfFileReader(pdfFlieObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(5)

print(pageObj.extract_text()) 

pdfFlieObj.close()
