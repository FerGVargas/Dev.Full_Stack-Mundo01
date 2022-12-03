from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4,landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.units import inch
import webbrowser

c = canvas.Canvas("hello2.pdf",pagesize=landscape(letter))
c.drawString(0.3*inch,0.3*inch,'Hello world')
c.showPage()
c.pageSize = 200,200 #Change that page size
c.drawString(0.3*inch,0.3*inch,'Hello world')
c.showPage()
c.save()

#serviu apenas para verifica sintaxe landscape