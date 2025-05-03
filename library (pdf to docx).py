from pdf2docx import Converter

pdf_file = 'Updated FYP Idea evaluation schedule.pdf'
docx_file = 'Updated FYP Idea evaluation schedule.docx'
cv  = Converter(pdf_file)
cv.convert(docx_file)
cv.close()