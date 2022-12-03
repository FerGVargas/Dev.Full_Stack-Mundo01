from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter 
from reportlab.lib.enums import TA_CENTER,TA_JUSTIFY

document=[]
document.append(Image('tools-64.png',2.2*inch,2.2*inch))


def addTitle(doc):
       
   style = getSampleStyleSheet()    
   doc.append(Spacer(1,20))
   doc.append(Paragraph('Bla bla',ParagraphStyle('Name', alignment=TA_CENTER,
                  fontFamily='Helvetica',fontSize=36)))  
   
   doc.append(Spacer(1,50))
   return(doc)

def addParagraphs(doc):
   with open('text.txt') as txt:
      for line in txt.read().split('\n'):
         doc.append(Paragraph(line))
         doc.append(Spacer(1,20))
      return(doc) 

document= addTitle(document)

SimpleDocTemplate('nomeDoc.pdf',pagesize=letter,rightMargin=12,
                      leftMargin=12,
                      bottomMargin=6).build(addTitle(document))        