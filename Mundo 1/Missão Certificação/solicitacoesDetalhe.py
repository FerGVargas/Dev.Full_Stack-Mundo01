from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from dadosXLSX import Dados


def detalheSolicitacao():

    cData = Dados()
    # PRODUÇÃO
    lsDetalhe = cData.readFileTemp()

    print('lsDetalhe ------>>', lsDetalhe)
    # APENAS DEBUG
    #lsDetalhe=['MMEI-W45', 'FERRAMENTA2', 'BOSCH', '220', 'DIEOW-3', '44X9', 'PESAGEM', 'CHAVE PHILLIPS', 'AÇO RÁPIDO']

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
    photo = PhotoImage(file='imagens/toolsIco-48.png')
    master_ch.iconphoto(False, photo)

    #FRAME1 / TITULO
    frame1 = Frame(master_ch, width=900, height=100, bg= backGR) 
    frame1.grid(row=0, column=0, columnspan=3, sticky='nsew')

    lblTit = Label(frame1, text="DETALHE SOLICITAÇÃO",  font= ("Calibri",25, "bold"), 
    bg=backGR)
    lblTit.grid(row=0, column=0, pady=40, padx=300)

    # FRAME2 / LABELS------------------------
    frame2 = Frame(master_ch, width=300, height=500, bg=backGR)
    frame2.grid(row=1, column=0, sticky='nsew')

    # essa dicionario serve apenas para saber o indice
    dadosDetalhe = {
        'cpf': 0,
        'nome': 1,
        'equipe': 2,
        'codigo da ferramenta': 3,
        'data saida': 4,
        'hora saida': 5,
        'data devolução': 6,
        'hora devolução': 7,
        'motivo': 8
    }

    # PONTO DE CONFIGURAÇÃO / LABELs CONSULTA DETALHE

    # CPF caption
    Label(frame2, text="CPF", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    # CPF info
    Label(frame2, text=lsDetalhe[0], relief=SUNKEN, width=nWinfo,
          font=("Calibri", 12), bg=lbbr).grid(row=linElementos,
                                     column=1, pady=nPADY,
                                     padx=nPADX)

    # reserva
    """
    NÃO CONSEGUI ENTENDER PORQUE NÃO FUNCIONA
    VAI LABEL MESMO !!!

    _sReservado = StringVar()
    chkReserva = IntVar()
    
     
    def atualizaCheck():
       if lsDetalhe[9] == 'SIM':
           chkReserva.set(1)
       else:
           chkReserva.set(0)
 
    Checkbutton(frame2, text='RESERVA', font=('Calibri', 12), variable=chkReserva, 
                             onvalue=1, 
                             offvalue=1, command='').grid(row=linElementos, 
                             column=2,
                             pady=nPADY, padx=nPADX)
    #atualizaCheck()                         
    """
    # NOME caption
    Label(frame2, text="NOME", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+1,
                                              column=0, ipady=nIPADY, padx=nIPADX)

    # NOME info
    Label(frame2, text=lsDetalhe[1], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+1, column=1,
                                           pady=nPADY, padx=nPADX)

    # EQUIPE label
    Label(frame2, text="EQUIPE", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+2,
                                              column=0, ipady=nIPADY,
                                              padx=nIPADX)

    # EQUIPE info
    Label(frame2, text=lsDetalhe[2], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+2,
                                           column=1, pady=nPADY, padx=nPADX)

    # CODIGO DA FERRAMENTA caption
    Label(frame2, text="CODIGO DA FERRAMENTA", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+3,
                                              column=0, ipady=nIPADY,
                                              padx=nIPADX)

    # CODIGO DA FERRAMENTA info
    Label(frame2, text=lsDetalhe[3], relief=SUNKEN,
          font=("Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+3,
                                                   column=1,
                                                   pady=nPADY,
                                                   padx=nPADX)

    # DATA SAIDA caption
    Label(frame2, text="DATA DA SAIDA", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+4,
                                              column=0,
                                              ipady=nIPADY,
                                              padx=nIPADX)

    # DATA SAIDA info
    Label(frame2, text=lsDetalhe[4], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+4,
                                           column=1,
                                           pady=nPADY,
                                           padx=nPADX)
    # HORA SAIDA caption
    Label(frame2, text="HORA DA SAIDA",
          font=("Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+5,
                                                      column=0, ipady=nIPADY,
                                                      padx=nIPADX)

    # HORA SAIDA info
    Label(frame2, text=lsDetalhe[5], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+5,
                                           column=1,
                                           pady=nPADY,
                                           padx=nPADX)

    # DATA DEVOLUÇÃO caption
    Label(frame2, text="DATA DA DEVOLUÇÃO", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+6, column=0,
                                              ipady=nIPADY, padx=nIPADX)

    # DATA DEVOLUÇÃO info
    Label(frame2, text=lsDetalhe[6], relief=SUNKEN,
          font=("Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+6,
                                                   column=1, pady=nPADY, padx=nPADX)

    # HORA DEVOLUÇÃO caption
    Label(frame2, text="HORA DA DEVOLUÇÃO", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+7, column=0,
                                              ipady=nIPADY, padx=nIPADX)

    # HORA DEVOLUÇÃO info
    Label(frame2, text=lsDetalhe[7], relief=SUNKEN,
          font=("Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+7,
                                                   column=1, pady=nPADY,
                                                   padx=nPADX)

    # MOTIVO caption
    Label(frame2, text="MOTIVO", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+8, column=0, ipady=nIPADY, padx=nIPADX)

    # MOTIVO info
    Label(frame2, text=lsDetalhe[8], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+8,
                                           column=1,
                                           pady=nPADY,
                                           padx=nPADX)

    # RESERVADO caption
    Label(frame2, text="RESERVADO", font=(
        "Calibri", 12), width=nWcaption, bg= backGR).grid(row=linElementos+9, column=0, ipady=nIPADY, padx=nIPADX)

    # RESERVADO  info
    Label(frame2, text=lsDetalhe[9], relief=SUNKEN, font=(
        "Calibri", 12), width=nWinfo, bg=lbbr).grid(row=linElementos+9,
                                           column=1,
                                           pady=nPADY,
                                           padx=nPADX)

    # FRAME3 / INFO------------------------
    # frame3 = Frame(master_ch, width=300, height=500)  # ,bg='white'
    #frame3.grid(row=1, column=1, sticky='nsew')

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
    # master_ch.mainloop()
# AKI DEBUG
# detalheConsulta()
# consultarSolicitacoes()
