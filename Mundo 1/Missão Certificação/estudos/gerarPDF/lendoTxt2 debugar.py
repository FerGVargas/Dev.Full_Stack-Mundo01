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
   lsValores=[('1', 'wwww', '5555'), ('2', 'ggggg', '3333'), ('3', 'eeeee', '77777')]  
   for valor in lsValores:
         print(valor[0])
         #ERRO
         #doc.append(Paragraph())
         #doc.append(Paragraph('''XXXXXXXXXXXXXX'''))
         doc.append(Spacer(1,20))
   return(doc) 

document= addTitle(document)

SimpleDocTemplate('nomeDoc.pdf',pagesize=letter,rightMargin=12,
                      leftMargin=12,
                      bottomMargin=6).build(addParagraphs(document))        