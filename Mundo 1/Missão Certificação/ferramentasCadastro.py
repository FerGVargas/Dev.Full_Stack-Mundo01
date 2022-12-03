from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from dadosXLSX import Dados


def cadastroFerramentas():
    
    cData=Dados()

    def limparCampos():
         
        _sCodigo.set('')
        _sDescricao.set('')
        _sFabricante.set('')
        _sVoltagem.set('')
        _sPartNumber.set('')
        _sTamanho.set('')
        _sUnidade.set('')
        _sTpFerramenta.set('')
        _sMaterial.set('')

         
    def salvar():
        codigo=_sCodigo.get()
        descricao=_sDescricao.get()
        fabricante=_sFabricante.get()
        voltagem=_sVoltagem.get()
        partNumber=_sPartNumber.get()
        tamanho=_sTamanho.get()
        unidade=_sUnidade.get()
        tpFerramenta=_sTpFerramenta.get()
        material=_sMaterial.get()

        def campoStringInvalido(valor):
            if len(valor)==0:
                return True
            else:
                return False 
        
        def existeDuplicidade(codigo):
            bReturn= False  
            # se a planilha não existir ainda precisa de try
            try:
               #codigo esta na primeira coluna por isso não preciso das demais
               nItens=0 
               ls2=cData.OpenFindDateXLSX('ferramentas.xlsx','ferramentas',codigo,nItens)
               if len(ls2)>0:
                  bReturn = True #vai bloquear
            except:
               pass   

            return bReturn

        def msgBox(msg):
          messagebox.showerror('Erro',msg,parent=master)

        def camposValidos():
           #se não cair em nenhuma critica sai como true
           bReturn=True

           if campoStringInvalido(codigo):
                msg='codigo não definido, verifique.'
                msgBox(msg)
                return  False
           elif existeDuplicidade(codigo):
                msg='codigo já cadastrado, verifique.'
                msgBox(msg)
                return  False
           else:
               pass       

           if campoStringInvalido(descricao):
                msg='descricao não definida, verifique.'
                msgBox(msg)
                return  False 

           if campoStringInvalido(fabricante):
                msg='fabricante não definido, verifique.'
                msgBox(msg)
                return  False 

           if campoStringInvalido(voltagem):
                msg='voltagem não definida, verifique.'
                msgBox(msg)
                return  False

           if campoStringInvalido(partNumber):
                msg='partNumber não definido, verifique.'
                msgBox(msg)
                return  False

           if campoStringInvalido(tamanho):
                msg='tamanho não definido, verifique.'
                msgBox(msg)
                return  False

           if campoStringInvalido(unidade):
                msg='unidade não definida, verifique.'
                msgBox(msg)
                return  False

           if campoStringInvalido(tpFerramenta):
                msg='tipo de Ferramenta não definida, verifique.'
                msgBox(msg)
                return  False

           if campoStringInvalido(material):
                msg='material não definido, verifique.'
                msgBox(msg)
                return  False


           return bReturn

        if camposValidos():  
            dadosCadastro=[
                    codigo,
                    descricao,
                    fabricante,
                    voltagem,
                    partNumber,
                    tamanho,
                    unidade,
                    tpFerramenta,
                    material

                    ]
                    
            cData.createInsertXLSX('ferramentas.xlsx','ferramentas',dadosCadastro)
            limparCampos()

    #AKI PRODUCAO 
    master =  Toplevel()
    #AKI DEBUG
    #master = Tk()
    
    # Cores
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
    nWinfo=41
    nWinfoCombo=39
    nWcaption=21
    
    #master.title("---Ferramentas---")
    master.geometry('900x600+591+215')
    master.wm_resizable(width=False,height=False)
    photo = PhotoImage(file = 'imagens/toolsIco-48.png')   
    master.iconphoto(False, photo)
    master.configure(background= backGR)
    
    nomePlanilhaDeListas='listasFerramentas.xlsx'

    #FRAME1 / TITULO
    frame1=Frame(master,width=900,height=100, bg= backGR)#,bg='green' 
    frame1.grid(row=0,column=0,columnspan=3,sticky='nsew')
    lblTit=Label(frame1, text="CADASTRO DE FERRAMENTAS", font= ("Calibri",25, "bold"), bg=backGR)
    lblTit.grid(row=0,column=0,pady=40,padx=240) 
    
     
    #FRAME2 / LABELS e ENTRIES
    frame2=Frame(master,width=600,height=500, bg=backGR)
    frame2.grid(row=1,column=0,sticky='nsew')
    
    #CODIGO
    Label(frame2, text="CODIGO", font=("Calibri", 12),width=nWcaption,bg=backGR ).grid(row=linElementos,
                                                           column=0,ipady=nIPADY,padx=nIPADX)

    _sCodigo=StringVar() 
    Entry(frame2,bd=2,font=('Calibri',12),width=nWinfo,textvariable=_sCodigo).grid(row=linElementos,
                                                                     column=1,pady=nPADY,
                                                                    padx=nPADX)


    #DESCRICAO
    Label (frame2, text="DESCRICAO", font=("Calibri", 12),width=nWcaption, bg=backGR).grid(row=linElementos+1,
                                                                  column=0,ipady=nIPADY,padx=nIPADX)  
    _sDescricao=StringVar()
    Entry(frame2,bd=2,font=('Calibri',12),width=nWinfo,textvariable=_sDescricao).grid(row=linElementos+1,column=1,
                                                                         pady=nPADY,padx=nPADX)

    #FABRICANTE / combo box 
    Label ( frame2, text="FABRICANTE", font=("Calibri", 12),width=nWcaption,bg=backGR).grid(row=linElementos+2,
                                                                  column=0,ipady=nIPADY,
                                                                  padx=nIPADX) 
    
    # get lista 
    lst=cData.getList(nomePlanilhaDeListas,'fabricante')
    _sFabricante=StringVar()
    ttk.Combobox ( frame2,value=lst,font=("Calibri", 12),width=nWinfoCombo,state="readonly",textvariable=_sFabricante).grid(row=linElementos+2,column=1,pady=nPADY,padx=nPADX)
    
    #VOLTAGEM /combo box 
    Label ( frame2, text="VOLTAGEM DE USO", font=("Calibri", 12),width=nWcaption,bg=backGR).grid(row=linElementos+3,
                                                                       column=0,ipady=nIPADY,
                                                                        padx=nIPADX)
    
    # get lista 
    lst=cData.getList(nomePlanilhaDeListas,'voltagem')
    print('lst-->>',lst)
    _sVoltagem=StringVar()
    ttk.Combobox ( frame2,value=lst,font=("Calibri", 12),state="readonly",width=nWinfoCombo,
                          textvariable=_sVoltagem).grid(row=linElementos+3,
                                                         column=1,pady=nPADY,
                                                         padx=nPADX)
    
    
    #PART NUMBER
    Label ( frame2, text="PART NUMBER", font=("Calibri", 12),width=nWcaption,bg=backGR).grid(row=linElementos+4,
                                                                    column=0,
                                                                    pady=nIPADY,
                                                                    padx=nIPADX)
    _sPartNumber=StringVar()
    Entry(frame2,bd=2,font=('Calibri',12),width=nWinfo,textvariable=_sPartNumber).grid(row=linElementos+4,column=1,pady=nPADY,padx=nPADX)
    
    
    #TAMANHO
    Label ( frame2, text="TAMANHO", font=("Calibri", 12),width=nWcaption,bg=backGR).grid(row=linElementos+5,
                                                               column=0,pady=nIPADY,
                                                                padx=nIPADX)
    
    _sTamanho=StringVar() 
    Entry (frame2,bd=2,font=('Calibri',12),width=nWinfo,textvariable=_sTamanho,).grid(row=linElementos+5,
                                                                        column=1,pady=nIPADY,
                                                                        padx=nIPADX) 
    

    #UNIDADE DE MEDIDA
    Label ( frame2, text="UNIDADE DE MEDIDA", font=("Calibri", 12),width=nWcaption,bg=backGR).grid(row=linElementos+6,column=0,
                                                                         pady=nIPADY,padx=nIPADX)
    #combo box UNIDADE DE MEDIDA
    lst=cData.getList(nomePlanilhaDeListas,'unidade de medida')    
    _sUnidade=StringVar()
    ttk.Combobox (frame2,value=lst,font=("Calibri", 12),textvariable=_sUnidade,state="readonly",width=nWinfoCombo).grid(row=linElementos+6,column=1,
                                                                                                   pady=nIPADY,padx=nIPADX)    

    
    #TIPO DE FERRAMENTA 
    Label ( frame2, text="TIPO DE FERRAMENTA", font=("Calibri", 12),width=nWcaption,bg=backGR).grid(row=linElementos+7,
                                                                               column=0,pady=nIPADY,
                                                                               padx=nIPADX)
    #combo box 
    lst=cData.getList(nomePlanilhaDeListas,'tipo de ferramentas')
    _sTpFerramenta=StringVar()
    ttk.Combobox (frame2,value=lst,font=("Calibri", 12),width=nWinfoCombo,state="readonly",
                        textvariable=_sTpFerramenta).grid(row=linElementos+7,
                                                        column=1,pady=nIPADY,
                                                        padx=nIPADX)
    
    #MATERIAL
    Label ( frame2, text="MATERIAL", font=("Calibri", 12),width=nWcaption,bg=backGR).grid(row=linElementos+8,
                                                                column=0,pady=nIPADY,
                                                                padx=nIPADX)
    #combo box 
    lst=cData.getList(nomePlanilhaDeListas,'material') 
    _sMaterial=StringVar()  
    ttk.Combobox (frame2,value=lst,font=("Calibri", 12),width=nWinfoCombo,state="readonly",textvariable=_sMaterial).grid(row=linElementos+8,
                                                                                                 column=1,pady=nIPADY,
                                                                                                   padx=nIPADX)    
      
    #FRAME3 / ENTRY------------------------
    #frame3=Frame(master,width=300,height=500)#,bg='white' 
    #frame3.grid(row=1,column=1,sticky='nsew')
  
    Button(master, text="confimar", width=14, height=2, bg=btn,activebackground= btn_ef ,font=fontP,command=salvar).place(x=509, y=544)
    Button(master, text="retornar", width=14, height=2, bg=btn,activebackground= btn_ef ,font=fontP,command=master.destroy ).place(x=696, y=544)
    
    #,activebackground= btn_ef

    #img = PhotoImage(file='imagens/img_cad_ferr.png')
    # Load the image
    image=Image.open('imagens/img_cad_ferr.png')

    # Resize the image in the given (width, height)
    img=image.resize((260, 250))

    # Conver the image in TkImage
    my_img=ImageTk.PhotoImage(img)


    lbel_imag=  Label(master, bd= 0,image=my_img).place(x=650,y=135) 
    lbel_imag.pack()
    #AKI DEBUG
    #master.mainloop()
 

#AKI DEBUG
#cadastroFerramentas()
 
 
