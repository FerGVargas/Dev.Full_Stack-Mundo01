from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import  A4

my_Style=ParagraphStyle('My Para style',
fontName='Times-Roman',
backColor='#F1F1F1',
fontSize=16,
borderColor='#FFFF00',
borderWidth=2,
borderPadding=(20,20,20),
leading=20,
alignment=0
)

width,height=A4
my_path='my_pdf.pdf' 
c = canvas.Canvas(my_path, pagesize=A4)

p1=Paragraph('''<b>About this online classes </b><BR/>\
     Welcome to our online classes.<BR/> \
	 You can learn Python, PHP, database like MySQL \
SQLite and many more \
<font face="times" color="blue">We are creating \
PDF by using ReportLab</font> \
<i>This is part of our Final report.</i>''',my_Style)

p1.wrapOn(c,300,50)
p1.drawOn(c,width-450,height-350)
c.save()