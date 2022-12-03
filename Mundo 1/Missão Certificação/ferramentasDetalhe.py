from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

from dadosXLSX import Dados

def detalheFerramenta():
    
    cData=Dados()
    
    #PRODUÇÃO
    lsDetalhe=cData.readFileTemp()
    #DEGUB
    #lsDetalhe=['MMEI-W45', 'FERRAMENTA2', 'BOSCH', 220, 'DIEOW-3', '44X9', 'PESAGEM', 'CHAVE PHILLIPS', 'AÇO RÁPIDO']
    print('detalheFerramenta-->>>',lsDetalhe)
    # AKI PRODUCAO
    master_ch = Toplevel()
    # AKI DEBUG
    #master_ch = Tk()

    # Cores
    btn = '#EB6440'
    btn_ef = '#ed8468'
    backGR = '#497174'
    lbbr= "#d8e2e3"
 
    # LABELS e ENTRYS Y
    nIPADY = 8  # labels
    nPADY = 8  # entrys

    nIPADX = 8  # labels
    nPADX = 8  # entrys

    # linha elementos
    linElementos = 5

    # width campos info
    nWinfo = 40
    nWcaption = 21

    master_ch.title("Consultar Ferramentas")
    master_ch.geometry('900x600+610+255')
    master_ch.wm_resizable(width=False, height=False)
    master_ch.configure(background= backGR)
    photo = PhotoImage(file = 'imagens/detFerrIco.png') 
    master_ch.iconphoto(False, photo)
    

    #nomePlanilhaDeListas = 'listasdeferramentas.xlsx'

    print('detalheFerramenta2 --->',lsDetalhe)
    #FRAME3 / TITULO
    frame1 = Frame(master_ch, width=900, height=100, bg= backGR)  
    frame1.grid(row=0, column=0, columnspan=3, sticky='nsew')

    lblTit = Label(frame1, text="DETALHE FERRAMENTA", font= ("Calibri",25, "bold"), 
    bg=backGR)
    lblTit.pack(fill='both', pady=40, padx=280)

    # FRAME2------------------------
    frame2 = Frame(master_ch, width=300, height=500, bg=backGR)
    frame2.grid(row=1, column=0, sticky='nsew')
    
    #CODIGO
    Label(frame2, text="CODIGO", width=nWcaption, font=(
        "Calibri", 12), bg=backGR).grid(row=linElementos,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    
    Label(frame2, text=lsDetalhe[0], relief=SUNKEN, width=nWinfo,
        font=("Calibri", 12), bg=lbbr).grid(row=linElementos,
                                     column=1, pady=nPADY,
                                     padx=nPADX)

   
    #DESCRICAO
    Label(frame2, text="DESCRICAO", width=nWcaption, font=(
        "Calibri", 12), bg=backGR).grid(row=linElementos+1,
                                              column=0, ipady=nIPADY, padx=nIPADX)

   
    Label(frame2, text=lsDetalhe[1], relief=SUNKEN,width=nWinfo, font=(
        "Calibri", 12), bg=lbbr).grid(row=linElementos+1,
                                     column=1, pady=nPADY,
                                     padx=nPADX)

    #FABRICANTE
    Label(frame2, text="FABRICANTE", width=nWcaption, font=(
        "Calibri", 12), bg=backGR).grid(row=linElementos+2,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    # combo box Fabricante
    Label(frame2, text=lsDetalhe[2], relief=SUNKEN,width=nWinfo, font=(
        "Calibri", 12), bg=lbbr).grid(row=linElementos+2,
                                     column=1, pady=nPADY,
                                     padx=nPADX)


    #VOLTAGEM DE USO
    Label(frame2, text="VOLTAGEM DE USO", width=nWcaption, font=(
        "Calibri", 12), bg=backGR).grid(row=linElementos+3,
                                              column=0, ipady=nIPADY, padx=nIPADX)
    
    Label(frame2, text=lsDetalhe[3], relief=SUNKEN,width=nWinfo,
        font=("Calibri", 12), bg=lbbr).grid(row=linElementos+3,
                                     column=1, pady=nPADY,
                                     padx=nPADX)
        
    #PART NUMBER    
    Label(frame2, text="PART NUMBER", width=nWcaption, font=(
        "Calibri", 12), bg=backGR).grid(row=linElementos+4,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    Label(frame2, text=lsDetalhe[4], relief=SUNKEN,width=nWinfo, font=(
        "Calibri", 12), bg=lbbr).grid(row=linElementos+4,
                                     column=1, pady=nPADY,
                                     padx=nPADX)

    #TAMANHO
    Label(frame2, text="TAMANHO", width=nWcaption, font=("Calibri", 12), bg=backGR).grid(row=linElementos+5,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    Label(frame2, text=lsDetalhe[5], relief=SUNKEN, width=nWinfo,font=(
        "Calibri", 12), bg=lbbr).grid(row=linElementos+5,
                                     column=1, pady=nPADY,
                                     padx=nPADX)

    

    #UNIDADE DE MEDIDA    
    Label(frame2, text="UNIDADE DE MEDIDA", width=nWcaption, font=(
        "Calibri", 13), bg=backGR).grid(row=linElementos+6,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    Label(frame2, text=lsDetalhe[6], relief=SUNKEN,width=nWinfo,
        font=("Calibri", 12), bg=lbbr).grid(row=linElementos+6,
                                     column=1, pady=nPADY,
                                     padx=nPADX)



    #TIPO DE FERRAMENTA    
    Label(frame2, text="TIPO DE FERRAMENTA", width=nWcaption, font=(
        "Calibri", 12), bg=backGR).grid(row=linElementos+7,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    Label(frame2, text=lsDetalhe[7], relief=SUNKEN,width=nWinfo,
        font=("Calibri", 12), bg=lbbr).grid(row=linElementos+7,
                                     column=1, pady=nPADY,
                                     padx=nPADX)



    #MATERIAL
    Label(frame2, text="MATERIAL", width=nWcaption, font=(
        "Calibri", 12), bg=backGR).grid(row=linElementos+8,
                                              column=0, ipady=nIPADY, padx=nIPADX)


    Label(frame2, text=lsDetalhe[8], relief=SUNKEN,width=nWinfo, font=(
        "Calibri", 12), bg=lbbr).grid(row=linElementos+8,
                                     column=1, pady=nPADY,
                                     padx=nPADX)

    # FRAME3 / INFO------------------------
    #frame3 = Frame(master_ch, width=300, height=500, bg= backGR)  # ,bg='white'
    #frame3.grid(row=1, column=1, sticky='nsew')

    
    #PONTO DE CONFIGURAÇÃO / LABELs CONSULTA DETALHE
    print('len lsDetalhe...',len(lsDetalhe))
    
    dadosDetalhe = {
        'Codigo':0,
        'Descricao':1,
        'Fabricante':2,
        'Voltagem':3,
        'PartNumber':4,
        'Tamanho':5,
        'Unidade':6,
        'TpFerramenta':7,
        'Material':8
    } 

    # FRAME4 / NECESSÁRIO PARA EQUILIBRAR------------------------
    #frame4 = Frame(master_ch, width=300, height=500, bg= backGR)  # ,bg='yellow'
    #frame4.grid(row=1, column=2)

    #Button(master, text="confimar", width=16, height=2, bg="orange",command='').place(x=509, y=544)
    Button(master_ch, text="retornar", width=16, height=2,
        bg=btn,activebackground= btn_ef, command=master_ch.destroy).place(x=696, y=544)


        # Load the image
    image=Image.open('imagens/img_cad_ferr_det.png')
                     #img_cad_ferr
                     #img_det_ferr

    # Resize the image in the given (width, height)
    img=image.resize((160, 250))

    # Conver the image in TkImage
    my_img=ImageTk.PhotoImage(img)


    lbel_imag=  Label(master_ch, bd= 0,image=my_img).place(x=750,y=135) 
    lbel_imag.pack()

    # AKI DEBUG
    #master_ch.mainloop()

# AKI DEBUG
#detalheFerramenta()
