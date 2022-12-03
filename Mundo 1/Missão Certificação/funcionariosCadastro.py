from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cpfutil

from dadosXLSX import Dados
 
def cadastroFuncionarios():
    
    cData=Dados()

    def limparCampos():
         
        _snome.set('')
        _scpf.set('')
        _stelefone.set('')
        _sturno.set('')
        _snome_equipe.set('')
       

    def salvar():
        nome=_snome.get()
        cpf=_scpf.get()
        telefone=_stelefone.get()
        turno=  _sturno.get()
        equipe=_snome_equipe.get()

        def existeDuplicidade(valor,nItens=0):
            bReturn= False  
            # se a planilha não existir ainda precisa de try
            try:
               #codigo esta na primeira coluna por isso não preciso das demais
               #nItens representa o numero colunas a serem acessadas, 1 vai procurar na 0 e 1  
               ls2=cData.OpenFindDateXLSX('funcionarios.xlsx','tecnicos',valor,nItens)
               if len(ls2)>0:
                  bReturn = True #vai bloquear
            except:
               pass   

            return bReturn        
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

           if campoStringInvalido(nome):
                msg='Nome não definido, verifique.'
                msgBox(msg)
                return False                
           elif existeDuplicidade(nome):
                msg='Nome já cadastrado, verifique.'
                msgBox(msg)
                return  False
           else:
               pass 
           if cpfutil.is_valid(cpf)!=True:
                msg='O cpf digitado não é valido, verifique.'
                msgBox(msg)
                return False    
           elif existeDuplicidade(cpf,1):
                msg='CPF já cadastrado, verifique.'
                msgBox(msg)
                return  False
           else:
               pass
           if campoStringInvalido(telefone):
                msg='telefone não definido, verifique.'
                msgBox(msg)
                return False

           if campoStringInvalido(turno):
                msg='turno não definido, verifique.'
                msgBox(msg)
                return False

           if campoStringInvalido(equipe):
                msg='equipe não definida, verifique.'
                msgBox(msg)
                return False
 
           return bReturn
           
        if camposValidos():  
            dadosCadastro=[
                        nome,
                        cpf,
                        telefone,
                        turno,
                        equipe,
                        ]
                
                
            cData.createInsertXLSX('funcionarios.xlsx','tecnicos',dadosCadastro)
            limparCampos()
        else :
            pass    

    #AKI PRODUCAO 
    master =  Toplevel()
    #AKI DEBUG
    #master = Tk()

    # Cores
    btn = '#EB6440'
    btn_ef = '#ed8468'
    backGR = '#497174'
    #fontes
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
    nWinfo=41
    nWinfoCombo=39
    nWcaption=21
    
    master.title("---Cadastro de técnicos---")
    master.geometry('900x600+591+215')
    master.wm_resizable(width=False,height=False)
    master.configure(background= backGR)
    photo = PhotoImage(file = 'imagens/toolsIco-48.png') 
    #toolsIco-48
    #funcIco-48
    master.iconphoto(False, photo)

    nomePlanilhaDeListas='listasFuncionarios.xlsx'

    #FRAME3 / TITULO
    frame1=Frame(master,width=900,height=100, bg=backGR)#,bg='green' 
    frame1.grid(row=0,column=0,columnspan=3,sticky='nsew')
    lblTit=Label(frame1, text="CADASTRO DE TÉCNICOS", font= ("Calibri",25, "bold"), bg=backGR)
    lblTit.grid(row=0,column=0,pady=40,padx=240)  
     
    #FRAME2 / LABELS------------------------
    frame2=Frame(master,width=300,height=500, bg=backGR)# 
    frame2.grid(row=1,column=0,sticky='nsew')

    #NOME 
    Label(frame2, text="NOME COMPLETO", font=("Calibri", 12),width=nWcaption, bg=backGR).grid(row=linElementos,
                                                           column=0,ipady=nIPADY,padx=nIPADX)
 
    _snome=StringVar() 
    Entry(frame2,bd=2,font=('Calibri',12),textvariable=_snome,width=nWinfo).grid(row=linElementos,
                                                                     column=1,pady=nPADY,
                                                                    padx=nPADX)    
    

    #CPF
    Label (frame2, text="CPF", font=("Calibri", 12),width=nWcaption, bg=backGR).grid(row=linElementos+1,
                                                                  column=0,ipady=nIPADY,padx=nIPADX) 

    _scpf=StringVar()
    Entry(frame2,bd=2,font=('Calibri',12),textvariable=_scpf,width=nWinfo).grid(row=linElementos+1,
                                                                     column=1,pady=nPADY,
                                                                    padx=nPADX)


    #TELEFONE
    Label ( frame2, text="TELEFONE", font=("Calibri", 12),width=nWcaption, bg=backGR).grid(row=linElementos+2,
                                                                  column=0,ipady=nIPADY,padx=nIPADX) 
 

    _stelefone=StringVar()
    Entry(frame2,bd=2,font=('Calibri',12),textvariable=_stelefone,width=nWinfo).grid(row=linElementos+2,
                                                                     column=1,pady=nPADY,
                                                                    padx=nPADX)

    #TURNOS
    Label ( frame2, text="TURNO", font=("Calibri", 12),width=nWcaption, bg=backGR).grid(row=linElementos+3,
                                                                     column=0,ipady=nIPADY,padx=nIPADX)  

    # get lista turnos
    lst=cData.getList(nomePlanilhaDeListas,'turno')
    _sturno=StringVar()
    ttk.Combobox ( frame2,value=lst,font=("Calibri", 12),state="readonly",width=nWinfo,textvariable=_sturno).grid(row=linElementos+3,
                                                                     column=1,pady=nPADY,
                                                                    padx=nPADX)

    #EQUIPES
    Label ( frame2, text="NOME DA EQUIPE", font=("Calibri", 12), bg=backGR).grid(row=linElementos+4,
                                                                     column=0,ipady=nIPADY,padx=nIPADX)  

    # get lista equipes
    lst=cData.getList(nomePlanilhaDeListas,'equipes')
    _snome_equipe=StringVar()
    ttk.Combobox ( frame2,value=lst,font=("Calibri", 12),width=nWinfo,state="readonly",textvariable=_snome_equipe).grid(row=linElementos+4,
                                                                     column=1,pady=nPADY,
                                                                    padx=nPADX)
   
   
    #FRAME3 / ENTRY------------------------
    #frame3=Frame(master,width=300,height=500)#,bg='white' 
    #frame3.grid(row=1,column=1,sticky='nsew')
   
 

    #FRAME4 / NECESSÁRIO PARA EQUILIBRAR------------------------
    #frame4=Frame(master,width=300,height=500)#,bg='yellow' 
    #frame4.grid(row=1,column=2)    

    #dadosCadastro=[] 

    Button(master, text="Confimar", width=14, height=2, bg=btn ,activebackground= btn_ef,font=fontP,command=salvar).place(x=509, y=544)
    Button(master, text="Retornar", width=14, height=2, bg=btn ,activebackground= btn_ef,font=fontP,command=master.destroy ).place(x=696, y=544)

        # Load the image
    image=Image.open('imagens/img_cad_ferr.png')
    #img_cad_ferr.png
    #img_cad_func.png
    # ico_ferr_func 


    # Resize the image in the given (width, height)
    img=image.resize((160, 250))

    # Conver the image in TkImage
    my_img=ImageTk.PhotoImage(img)


    lbel_imag=  Label(master, bd= 0,image=my_img).place(x=700,y=135) 
    lbel_imag.pack()
     
    #AKI DEBUG
    #master.mainloop()

 
#AKI DEBUG
#cadastroFuncionaros()
 
