from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4,landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.units import inch
import webbrowser

class PrintTreeview():

    def printTv(self,Lsvalores,titulo,arquivo_ext_pdf,lsCabs):

        c = canvas.Canvas(arquivo_ext_pdf)#,pagesize=landscape(letter)
        

            
        def mm2p(milimetros):
               return milimetros/0.352777



        nTabs=len(lsCabs)
        colTit=60
        rowTit=280
        
        colCab=20
        rowCab=rowTit- 40
        colItem=120
        rowItem=rowCab

        nPage=1
        colPage=180
        rowPage=20

        for valores in Lsvalores:

            c.setFont("Helvetica-Bold" , 18)
            c.drawString(mm2p(colTit), mm2p(rowTit), titulo)
            c.setFont("Helvetica-Bold", 14) 

            for j in range(0,nTabs): 
               c.setFont("Helvetica-Bold", 18)
               c.drawString(mm2p(colCab), mm2p(rowItem), lsCabs[j]+":" )
               c.setFont('Helvetica', 18)
               c.drawString(mm2p(colItem), mm2p(rowItem), valores[j]  )
               rowItem-=10
            c.drawString(mm2p(colPage), mm2p(rowPage), 'Page '+ str(nPage) ) 
            nPage+=1  
            rowItem=rowCab 
            c.showPage()
         
        c.save() 
        webbrowser.open(arquivo_ext_pdf)

ls=[('1', 'mmm', '888','endereco1','cep1','mae1'), ('2', 'bbbb', '9999','endereco2','cep2','mae2'), ('3', 'uuuu', '4444','endereco3','cep3','mae3')]
lsCabs=['id','nome','telefone','endereco','cep','mae']

#AKI DEBUG
#c=PrintTreeview()
#c.printTv(ls,'Lista de funcionários','funcionarios.pdf',lsCabs)