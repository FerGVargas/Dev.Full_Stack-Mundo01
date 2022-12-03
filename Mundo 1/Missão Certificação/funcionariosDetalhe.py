from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from dadosXLSX import Dados


def detalheFuncionario():

    cData = Dados()
    # PRODUÇÃO
    lsDetalhe = cData.readFileTemp()

    print('lsDetalhe ------>>', lsDetalhe)
    # APENAS DEBUG
    # AKI DEBUG
    #lsDetalhe=['FULANO SILVA', '(21)99212912', '890.332.121.98', 'NOITE', 'BALADA']

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

    #master_ch.title("Detalhe Solicitação")
    master_ch.geometry('900x600+610+255')
    master_ch.wm_resizable(width=False, height=False)
    master_ch.configure(background= backGR)
    photo = PhotoImage(file = 'imagens/toolsIco-48.png') 
    master_ch.iconphoto(False, photo)

    #FRAME1 / TITULO
    frame1 = Frame(master_ch, width=900, height=100, bg= backGR)  # ,bg='green'
    frame1.grid(row=0, column=0, columnspan=3, sticky='nsew')

    lblTit = Label(frame1, text="DETALHE FUNCIONÁRIO",  font= ("Calibri",25, "bold"), 
    bg=backGR)
    lblTit.grid(row=0, column=0, pady=40, padx=300)

    # FRAME2 / LABELS------------------------
    frame2 = Frame(master_ch, width=300, height=500,bg=backGR)
    frame2.grid(row=1, column=0, sticky='nsew')

    # essa dicionario serve apenas para saber o indice
    dadosDetalhe = {
        'nome': 0,
        'cpf': 1,
        'telefone': 2,
        'turno': 3,
        'equipe': 4 
     }

    # PONTO DE CONFIGURAÇÃO / LABELs CONSULTA DETALHE

    # NOME caption
    Label(frame2, text="NOME", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    # NOME info
    Label(frame2, text=lsDetalhe[0], relief=SUNKEN, width=nWinfo,
          font=("Calibri", 12), bg=lbbr).grid(row=linElementos,
                                     column=1, pady=nPADY,
                                     padx=nPADX)

 
    # CPF label
    Label(frame2, text="CPF", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+1,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    # CPF info
    Label(frame2, text=lsDetalhe[1], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+1, column=1,
                                           pady=nPADY, padx=nPADX)

    # TELEFONE label
    Label(frame2, text="TELEFONE", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+2,
                                              column=0, ipady=nIPADY,
                                              padx=nIPADX)

    # TELEFONE
    Label(frame2, text=lsDetalhe[2], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+2,
                                           column=1, pady=nPADY, padx=nPADX)

    # TURNO label
    Label(frame2, text="TURNO", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+3,
                                              column=0, ipady=nIPADY,
                                              padx=nIPADX)

    # TURNO info
    Label(frame2, text=lsDetalhe[3], relief=SUNKEN,
          font=("Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+3,
                                                   column=1,
                                                   pady=nPADY,
                                                   padx=nPADX)

    # EQUIPE label
    Label(frame2, text="EQUIPE", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+4,
                                              column=0,
                                              ipady=nIPADY,
                                              padx=nIPADX)

    # EQUIPE info
    Label(frame2, text=lsDetalhe[4], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+4,
                                           column=1,
                                           pady=nPADY,
                                           padx=nPADX)
 
 
    Button(master_ch, text="retornar", width=16, height=2,
           bg=btn,activebackground= btn_ef, command=master_ch.destroy).place(x=696, y=544)

     # Load the image
    image=Image.open('imagens/img_cad_ferr.png')

    # Resize the image in the given (width, height)
    img=image.resize((160, 250))

    # Conver the image in TkImage
    my_img=ImageTk.PhotoImage(img)


    lbel_imag=  Label(master_ch, bd= 0,image=my_img).place(x=700,y=135) 
    lbel_imag.pack()

    # AKI DEBUG
    #master_ch.mainloop()
# AKI DEBUG
#detalheFuncionario()
 