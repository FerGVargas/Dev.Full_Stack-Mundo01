from tkinter import ttk
from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from PIL import Image, ImageTk 

import cpfutil
from dadosXLSX import Dados

import datetime 

def cadastroSolicitacoes():
    
    current_time = datetime.datetime.now()
    diaDisponivel=current_time.day
    
    cData=Dados()

    def limparCampos():
         
        _sCpf.set('')
        _sNome.set('')
        _sEquipe.set('')
        _sCodFerramenta.set('')
        _sDataSaida.set('')
        _sHoraSaida.set('')
        _sDataDevolucao.set('')
        _sHoraDevolucao.set('')
        _Motivo.set('')

        chkReserva.set(0)
        _sReservado.set('NÃO')
    
    def salvar():
        cpf=_sCpf.get()
        nome=_sNome.get()
        equipe=_sEquipe.get() 
        codFerramentas=_sCodFerramenta.get()
        dataSaida=_sDataSaida.get()
        horaSaida=_sHoraSaida.get()
        dataDevolucao=_sDataDevolucao.get()
        horaDevolucao=_sHoraDevolucao.get()
        motivo=_Motivo.get()
 
        reservado=_sReservado.get()

        def campoStringInvalido(valor):
            if len(valor)==0:
                return True
            else:
                return False 

        def msgBox(msg):
              messagebox.showerror('Erro',msg,parent=master)


        def camposValidos():

            #se não cair em nenhuma critica sai como true
            bReturn=True
              
            #Critica CPF
            if cpfutil.is_valid(cpf)!=True:
                msg='O cpf digitado não é valido, verifique.'
                msgBox(msg)
                return False    
         
            #Critica nome vazio
            if campoStringInvalido(nome) :
                msg='Nome não definido, verifique.'
                msgBox(msg)
                return False

            #Critica equipe vazio
            if campoStringInvalido(equipe):
                msg='Equipe não definida, verifique.'
                msgBox(msg)
                return  False 

            #Critica codFerramentas vazio
            if campoStringInvalido(codFerramentas):
                msg='Código da ferramenta não definido, verifique.'
                msgBox(msg)
                return  False  

            #Critica dataSaida vazio
            if campoStringInvalido(dataSaida):
                msg='Data saida não definida, verifique.'
                msgBox(msg)
                return  False  

            #Critica horaSaida vazio
            if campoStringInvalido(horaSaida):
                msg='Hora saida não definida, verifique.'
                msgBox(msg)
                return  False 

            #Critica dataDevolucao vazio
            if campoStringInvalido(dataDevolucao):
                msg='Data de devolução não definida, verifique.'
                msgBox(msg)
                return  False 

            #Critica horaDevolucao vazio
            if campoStringInvalido(horaDevolucao):
                msg='Hora de devolução não definida, verifique.'
                msgBox(msg)
                return  False 

            #Critica horaDevolucao vazio
            if campoStringInvalido(horaDevolucao):
                msg='Hora de devolução não definida, verifique.'
                msgBox(msg)
                return  False 


            #Critica motivo vazio
            if campoStringInvalido(motivo):
                msg='Motivo não definido, verifique.'
                msgBox(msg)
                return  False 

            return bReturn

        if camposValidos():         
           dadosCadastro=[
             cpf,
            nome,
            equipe,
            codFerramentas,
            dataSaida,
            horaSaida,
            dataDevolucao,
            horaDevolucao,
            motivo,
            reservado
            ]     

           cData.createInsertXLSX('solicitacoes.xlsx','solicitacoes',dadosCadastro)
           limparCampos()


    #AKI PRODUCAO 
    master =  Toplevel()
    #AKI DEBUG
    #master = Tk()

    #Cores
    btn = '#EB6440'
    btn_ef = '#ed8468'
    backGR = '#497174'

    #fonte
    fontP =('calibri', 12, 'normal')
    fontTxt=('calibri', 12, 'normal')
    
    #LABELS e ENTRYS Y
    nIPADY=8 #labels
    nPADY=8  # entrys

    nIPADX=8 #labels
    nPADX=8  #entrys
    
    #linha elementos
    linElementos=5

   #width campos info
    nWinfo=40
    nWinfoCombo=39
    nWcaption=21


    #master.title("Cadastro de Solicitações")
    master.geometry('900x600+591+215')
    master.wm_resizable(width=False,height=False)
    master.configure(background= backGR)
    
    photo = PhotoImage(file = 'imagens/solicitacoes-48.png')   
    master.iconphoto(False, photo) 
    
    #Planilhas usadas
    nomePlanilhaDeFuncionarios='funcionarios.xlsx'
    nomePlanilhaDeListas='listasSolicitacoes.xlsx'
    nomePlanilhaDeFerramentas='ferramentas.xlsx' #codigos
    nomePlanilhaDeListasFuncionarios='listasFuncionarios.xlsx'

    #FRAME1 / TITULO
    frame1=Frame(master,width=900,height=100,bg=backGR)#,bg='green' 
    frame1.grid(row=0,column=0,columnspan=3,sticky='nsew')
    lblTit=Label(frame1, text="CADASTRO DE SOLICITAÇÕES", font= ("Calibri",16),bg=backGR)
    lblTit.grid(row=0,column=0,pady=40,padx=300)  
     
    #FRAME2 / LABELS e ENTRIES------------------------
    frame2=Frame(master,width=600,height=500,bg=backGR)# 
    frame2.grid(row=1,column=0,sticky='nsew')
    
    
    #frame3=Frame(master,width=300,height=500,bg='white')# 
    #frame3.grid(row=1,column=1,sticky='nsew')

    
    # CPF label
    Label(frame2,font=('Calibri',12) ,text="CPF",width=nWcaption,bg=backGR).grid(row=linElementos,
                           column=0,ipady=nIPADY,padx=nIPADX) 
     
    # CPF info
    _sCpf=StringVar() 
    """
    Entry(frame2,bd=2,textvariable=_sCpf,font=('Calibri',12),
                                          width=nWinfo).grid(row=linElementos,
                                                         column=1,pady=nPADY,
                                                         padx=nPADX)
    """                                                     
    lst=cData.getList(nomePlanilhaDeFuncionarios,'tecnicos',1)
    cbCPF=ttk.Combobox ( frame2,value=lst,font=("Calibri", 12),width=nWinfoCombo,state="readonly",
                          textvariable=_sCpf)

    cbCPF.grid(row=linElementos,column=1,pady=nPADY,padx=nPADX) 
    
 

                      
    #reserva
    _sReservado=StringVar()
    chkReserva = IntVar()
    
    Checkbutton(frame2, text='RESERVA',font=('Calibri',12),bg=backGR,
                activebackground= backGR,command=lambda:setReserva(),
              variable= chkReserva, onvalue=1, offvalue=0).grid(row=linElementos,column=2,
                                       pady=nPADY,padx=nPADX)
    

    # NOME label
    Label (frame2, text="NOME", 
          font=("Calibri", 12),width=nWcaption,bg=backGR).grid(row=linElementos+1,
                                     column=0,ipady=nIPADY,padx=nIPADX) 
    # NOME info
    _sNome=StringVar()
    lst=cData.getList(nomePlanilhaDeFuncionarios,'tecnicos')
    cbNome=ttk.Combobox ( frame2,value=lst,font=("Calibri", 12),width=nWinfoCombo,state="readonly",
                          textvariable=_sNome)
    
    cbNome.grid(row=linElementos+1,column=1,pady=nPADY,padx=nPADX)
    
    """
    Entry(frame2,bd=2,font=('Calibri',12),
         textvariable=_sNome,width=nWinfo).grid(row=linElementos+1,column=1,
                                           pady=nPADY,padx=nPADX) 
    """

    # EQUIPES caption
    Label ( frame2, text="EQUIPE", font=("Calibri", 12),
                   width=nWcaption,bg=backGR).grid(row=linElementos+2,
                                        column=0,ipady=nIPADY,
                                        padx=nIPADX) 

    # EQUIPES info
    lst=cData.getList(nomePlanilhaDeListasFuncionarios,'equipes')
    _sEquipe=StringVar()
    ttk.Combobox ( frame2,value=lst,font=("Calibri", 12),width=nWinfoCombo,state="readonly",
                          textvariable=_sEquipe).grid(row=linElementos+2,
                          column=1,pady=nPADY,padx=nPADX)


    #codigo da ferramenta caption
    Label ( frame2, text="CODIGO DA FERRAMENTA", 
                    font=("Calibri", 12),width=nWcaption,bg=backGR).grid(row=linElementos+3,
                                               column=0,ipady=nIPADY,
                                               padx=nIPADX)

    #codigo da ferramenta info
    lst=cData.getList(nomePlanilhaDeFerramentas,'ferramentas') 
    _sCodFerramenta=StringVar()
    cdCodFerr=ttk.Combobox(frame2,value=lst,font=("Calibri", 12),state="readonly",
                        width=nWinfoCombo,textvariable=_sCodFerramenta)

    cdCodFerr.grid(row=linElementos+3,column=1,pady=nPADY,padx=nPADX)                                                                

    #data saida caption
    Label ( frame2, text="DATA DA SAIDA", 
                   font=("Calibri", 12),width=nWcaption,bg=backGR).grid(row=linElementos+4,
                                              column=0,
                                              ipady=nIPADY,
                                              padx=nIPADX)

    #data saida info    
    _sDataSaida=StringVar()
    Label(frame2,bd=2,font=('Calibri',12),textvariable=_sDataSaida,
                 relief=SUNKEN,anchor="w",
                 background='white',width=nWinfo).grid(row=linElementos+4,
                                                   column=1,
                                                   pady=nPADY,
                                                   padx=nPADX) 

    #BUTTON data calendario
    photo= PhotoImage(file='imagens/calendar-24.png')
    #image=photo 
    btnDt1= Button(frame2, text='data',image=photo,
                 command=lambda:callCalendario(1))
                 #.grid(row=linElementos+4,column=2,padx=2) 
    btnDt1.place(x=680,y=165)
    

    #hora saida caption
    Label ( frame2, text="HORA DA SAIDA", 
                  font=("Calibri", 12),width=nWcaption,bg=backGR).grid(row=linElementos+5,
                                             column=0,ipady=nIPADY,
                                             padx=nIPADX)

    #hora saida info
    _sHoraSaida=StringVar()
    lst=cData.getList(nomePlanilhaDeListas,'horarios')
    ttk.Combobox (frame2,value=lst,font=("Calibri", 12),state="readonly",
                        width=nWinfoCombo,
                        textvariable=_sHoraSaida).grid(row=linElementos+5,
                                                       column=1,
                                                       pady=nPADY,
                                                       padx=nPADX)

    _sHoraDevolucao=StringVar()

    
    #data devolucao caption
    Label ( frame2, text="DATA DA DEVOLUÇÃO", 
                   font=("Calibri", 13),
                   width=nWcaption,bg=backGR).grid(row=linElementos+6,column=0,
                                         ipady=nIPADY,padx=nIPADX)

    #data devolucao info
    _sDataDevolucao=StringVar()

    Label(frame2,bd=2,font=('Calibri',12),textvariable=_sDataDevolucao,
                 relief=SUNKEN,anchor="w",background='white',
                width=nWinfo).grid(row=linElementos+6,
                              column=1,pady=nPADY,padx=nPADX) 
    #BUTTON # data  
    btnDt2=Button(frame2, text='data', image=photo,
                  command=lambda:callCalendario(2))
                 #.grid(row=linElementos+6,column=2,padx=2)
    btnDt2.place(x=680,y=251) 

    #hora devolucao caption
    Label ( frame2, text="HORA DA DEVOLUÇÃO", 
                    font=("Calibri", 12),
                    width=nWcaption,bg=backGR).grid(row=linElementos+7,
                                          column=0,ipady=nIPADY,
                                          padx=nIPADX)

    #hora devolucao info
    lst=cData.getList(nomePlanilhaDeListas,'horarios')
    _sHoraDevolucao=StringVar()
    ttk.Combobox (frame2,value=lst,
                         font=("Calibri", 12),width=nWinfoCombo,state="readonly",
                         textvariable=_sHoraDevolucao).grid(row=linElementos+7,
                                                           column=1,pady=nPADY,
                                                           padx=nPADX)


    #motivo caption
    Label ( frame2, text="MOTIVO", 
                    font=("Calibri", 12),
                    width=nWcaption,bg=backGR).grid(row=linElementos+8,
                                          column=0,ipady=nIPADY,
                                          padx=nIPADX)

    #motivo info
    lst=cData.getList(nomePlanilhaDeListas,'motivo') 
    _Motivo=StringVar()  
    ttk.Combobox (frame2,value=lst,font=("Calibri", 12),state="readonly",
                         width=nWinfoCombo,
                         textvariable=_Motivo).grid(row=linElementos+8,
                                                    column=1,
                                                    pady=nPADY,
                                                    padx=nPADX)    

     
    limparCampos()

    Button(master, text="confimar", width=14, height=2, bg=btn ,activebackground= btn_ef,font=fontP,command=salvar).place(x=509, y=544)
    Button(master, text="retornar", width=14, height=2, bg=btn ,activebackground= btn_ef,font=fontP,command=master.destroy ).place(x=696, y=544)
    
    def setReserva():
        print('chkReserva -->>',chkReserva.get())
        
        _sDataSaida.set('')
        _sHoraSaida.set('')
        _sDataDevolucao.set('')
        _sHoraDevolucao.set('')

        if chkReserva.get() ==1:
            _sReservado.set('SIM')
            
        else:
            _sReservado.set('NÃO') 
  

    def callCalendario(valor):

        if chkReserva.get() ==1:
            diaDisponivel=current_time.day+1
        else:
            diaDisponivel=current_time.day 

        def print_sel():
            if valor==1:
               _sDataSaida.set(cal.get_date())
            else:
               _sDataDevolucao.set(cal.get_date())
 
        def quit1():
            top.destroy()



        top = Toplevel(master)
        top.configure(background= backGR) 
        photo = PhotoImage(file = 'imagens/calendar-48.png')   
        top.iconphoto(False, photo)
        top.geometry('450x500+1150+315')

        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=current_time.year, month=current_time.month, 
                       day=diaDisponivel)

        cal.pack(fill="both", expand=True)



        ttk.Button(top, text="ok", command=lambda:print_sel()).pack()
        ttk.Button(top, text="exit", command=lambda:quit1()).pack()

    
    #funções relacionadas aos eventos
    def FerramentaAlocada(event):
        nItensCabSolicitacoes=9
        codFerr=_sCodFerramenta.get()
        ls2=cData.OpenFindDateXLSX('solicitacoes.xlsx','solicitacoes',codFerr,nItensCabSolicitacoes)

        #verificar data da entrega maior q data atual
        if len(ls2)>0:
            print('dados ferr==>>>',ls2)
            #['827.177.323.91', 'Marco', 'NOITE', 'DJS-IW-90', '13/11/2022', '09:00:00', '14/11/2022', '10:00:00', 'TRABALHO', 'SIM']
            
            if ls2[9]!='SIM':
              msg='Ferramenta já esta alocada com ' + ls2[1] + ', com previsão de entrega para ' + ls2[6] + ' as ' + ls2[7]
            else:   
              msg='Ferramenta já reservada para ' + ls2[1] + ', com previsão de saida para ' + ls2[4] + ' as ' + ls2[5]+' a ser confirmada'  

            messagebox.showinfo('Erro',msg,parent=master)

            _sCodFerramenta.set('')

    def atualizaDadosFuncCpf(event):
        nItensCabFunc=4
        cpf=_sCpf.get()
        ls2=cData.OpenFindDateXLSX('funcionarios.xlsx','tecnicos',cpf,nItensCabFunc)
        _sNome.set(ls2[0])
        _sEquipe.set(ls2[4])
        print('dados func==>>>',ls2)
         
    def atualizaDadosFuncNome(event):
        nItensCabFunc=4
        nome=_sNome.get() 
        ls2=cData.OpenFindDateXLSX('funcionarios.xlsx','tecnicos',nome,nItensCabFunc) 
        _sCpf.set(ls2[1])
        _sEquipe.set(ls2[4])
        print('dados func==>>>',ls2)
        
 
    #EVENTOS COMBOS
    cbCPF.bind("<<ComboboxSelected>>",atualizaDadosFuncCpf)
    cbNome.bind("<<ComboboxSelected>>",atualizaDadosFuncNome)
    cdCodFerr.bind("<<ComboboxSelected>>",FerramentaAlocada)
    btnDt1.draw()
    btnDt2.draw()
    #AKI DEBUG
    #master.mainloop()
 
#AKI DEBUG
#cadastroSolicitacoes()
 
 
