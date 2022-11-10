from docx import Document
doc = Document()

text = doc.add_paragraph('teste')
doc.save('test.docx')