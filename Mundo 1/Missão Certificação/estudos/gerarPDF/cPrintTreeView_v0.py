from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4,landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.units import inch
import webbrowser



class PrintTreeview():

    def printTv(self,Lsvalores,titulo,arquivo_ext_pdf):

        c = canvas.Canvas(arquivo_ext_pdf,pagesize=landscape(letter))
        
        #linha mais acime é a mais alta
        colTit=100
        rowTit=190
        
        colCab=20
        rowCab=rowTit- 20
        
        rowItens=rowCab-20

            
        def mm2p(milimetros):
               return milimetros/0.352777

        c.setFont("Helvetica-Bold" , 18)
        c.drawString(mm2p(colTit), mm2p(rowTit), titulo)
         
        c.setFont("Helvetica-Bold", 14)
        c.drawString(mm2p(colCab), mm2p(rowCab), "ID:" )
        c.drawString(mm2p(colCab+20), mm2p(rowCab), "NOME:"   )
        c.drawString(mm2p(colCab+70), mm2p(rowCab,), "TELEFONE:"  )

        print('rowCab-->>>',mm2p(rowCab))

        for valores in Lsvalores:

           print('rowItens->',rowItens)
           c.setFont('Helvetica', 16)
           c.drawString(mm2p(colCab), mm2p(rowItens), valores[0]  )
           c.drawString(mm2p(colCab+20), mm2p(rowItens), valores[1]  )
           c.drawString(mm2p(colCab+70), mm2p(rowItens), valores[2] )

           print('rowItens-->>>',mm2p(rowItens))  
           rowItens-=10
          
        c.showPage()
        c.save() 
        webbrowser.open(arquivo_ext_pdf)

ls=[('1', 'mmm', '888'), ('2', 'bbbb', '9999'), ('3', 'uuuu', '4444')]

c=PrintTreeview()
c.printTv(ls,'Lista de funcionários','funcionarios.pdf')