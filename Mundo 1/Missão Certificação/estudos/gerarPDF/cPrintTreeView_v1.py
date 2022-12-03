from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4,landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.units import inch
import webbrowser

class PrintTreeview():

    def printTv(self,Lsvalores,titulo,arquivo_ext_pdf,lsCabs):

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

        nTabs=len(lsCabs)
        NwColCab=0
        nDistanciaCol=20
        for i in range(0,nTabs):
           if i==0: 
              c.drawString(mm2p(colCab), mm2p(rowCab), lsCabs[i] )
           else:
              NwColCab+=colCab+nDistanciaCol  
              c.drawString(mm2p(NwColCab), mm2p(rowCab), lsCabs[i]   )
  
        print('rowCab-->>>',mm2p(rowCab))
         
        c.setFont('Helvetica', 16)
        NwColCab=0

        for valores in Lsvalores:
            for j in range(0,nTabs): 
              if j==0:  
                 c.drawString(mm2p(colCab), mm2p(rowItens), valores[j]  )
              else:
                 NwColCab+=colCab+nDistanciaCol   
                 c.drawString(mm2p(NwColCab), mm2p(rowItens), valores[j]  )  
            rowItens-=10
            NwColCab=0
        
        c.showPage()
        c.save() 
        webbrowser.open(arquivo_ext_pdf)

ls=[('1', 'mmm', '888'), ('2', 'bbbb', '9999'), ('3', 'uuuu', '4444')]
lsCabs=['id','nome','telefone']

#AKI DEBUG
c=PrintTreeview()
c.printTv(ls,'Lista de funcionários','funcionarios.pdf',lsCabs)