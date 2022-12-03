from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from dadosXLSX import Dados
from cPrintTreeView import PrintTreeview


from funcionariosDetalhe import detalheFuncionario

cDados = Dados()

def consultarFuncionarios():

    global lsDetalhe
    lsDetalhe = []



    # PONTO DE CONFIGURAÇÃO / CABEÇARIO DO TREEVIEW
    Cab = [
        'Nome',
        'Cpf',
        'Telefone',
        'Turno.',
        'Equipe'
    ]

    #PONTO DE CONFIGURAÇÃO PDF / nome arquivo e titulo
    arqRelPdf='ListaFuncionarios.pdf'
    tituloRel='Lista de Funcionários'

    # PONTO DE CONFIGURAÇÃO / INDICES DOS FILTROS / 1
    listaFiltros = {'nome': 0, 'cpf': 1, 'turno': 3, 'equipe': 4}

    # FUNÇÃO DE FILTROS
    # função usada dentro da CARGATREEVIEW

    # PONTO DE CONFIGURAÇÃO FILTRO
    def limparFiltros():
        _sNome.set('')
        _sCpf.set('')
        _sTurno.set('')
        _sEquipe.set('')

    def getFilterTreeView(listaTodos):
        def contains(s, other):
            return s.__contains__(other)
            

        def getFilter(lsTodos, conteudo, indice):
            lsFilter = []
            strItem = ''
            for item in lsTodos:
                l1 = item.split(',')
                print('l1[0]====>,', l1[indice])
                print('_scodigo ------------>>>', conteudo)
                if contains(l1[indice], conteudo):
                    strItem = item
                    lsFilter.append(strItem)

            # print('FILTRO----------------->>>',lsFilter)
            return lsFilter

        lsReturnAll = []

        # PONTO DE CONFIGURAÇÃO FILTRO
        nome = _sNome.get().upper()
        cpf = _sCpf.get().upper()
        turno = _sTurno.get().upper()
        equipe = _sEquipe.get().upper()
        # PONTO DE CONFIGURAÇÃO / INDICES DOS FILTROS / 1
        if nome != '':
            #print('tulipa ------',listaFiltros['codigo'])
            lsReturnAll = getFilter(listaTodos, nome, listaFiltros['nome'])

        if len(lsReturnAll) == 0:
            lsReturnAll = getFilter(listaTodos, cpf, listaFiltros['cpf'])
        else:
            lsReturnAll = getFilter(
                lsReturnAll, cpf, listaFiltros['cpf'])

        if len(lsReturnAll) == 0:
            lsReturnAll = getFilter(
                listaTodos, turno, listaFiltros['turno'])
        else:
            lsReturnAll = getFilter(
                lsReturnAll, turno, listaFiltros['turno'])
        
        if len(lsReturnAll) == 0:
                lsReturnAll = getFilter(
                listaTodos, equipe, listaFiltros['equipe'])
        else:
            lsReturnAll = getFilter(
                lsReturnAll, equipe, listaFiltros['equipe'])
        return lsReturnAll

    # ROTINAS DE TREEVIEW
    def cargaTreeView(ls, filtro=False):
        # REMOVE TUDO
        def remove_all():
            x = tv.get_children()
            print('tv.get_children() ==>>>', x)
            if x != '()':
                for child in x:
                    tv.delete(child)

        lsLocal = []
        remove_all()
        # se a chamada não for do filtro
        # carrega a lista vinda da planilha
        # caso contrario usa a lista do filtro
        if filtro == False:
            lsLocal = ls
            limparFiltros()
        else:
            lsLocal = getFilterTreeView(ls)
            
        #print('carga tree <<==>>>',lsLocal)

        if (len(ls) > 0):
            for row in lsLocal:
                # DEBUG
                #print('row ==>',row)

                tv.insert("", "end", values=row.split(","))

    # CLICK NA LINHA DO TREEVIEW
    def obterLinhaTv(e):
        import sys

        try:

            itemSelecionado2 = tv.selection()
            item = tv.item(itemSelecionado2)

            comp = len(Cab)

            # retorna um dicionario
            print('item==>>', item)
            print('item[0]==>>', item['values'][0])
            # valores=tv.item(itemSelecionado,'values')

            linha = item['values']
            lsDetalhe = linha
            cDados.saveFileTemp(lsDetalhe)
            print('obterLinhaTv -->>', lsDetalhe)

        except:
            print(sys.exc_info()[0])

    # Tratamento da chamada a tela de detalhe da ferramenta
    def callDetConsulta():
        try:
            with open('newfileLista.txt', 'r') as f:
                detalheFuncionario()
        except IOError:
            messagebox.showinfo('Aviso', 'Necessário selecionar uma linha')
    
    #IMPRIME TREEVIEW
    def listarTreeView(lsCabs):
        ls=[]
        for item in tv.get_children():
           item2=tv.item(item) 
           valores=tv.item(item,'values')
           print(item2) # aki reconheco um dicionario 
           print(item2['values']) #aki reconheço a lista contendo info
           print(valores) # esse e  o usado na impressao
           ls.append(valores)
      
        #print(ls)

        if len(ls)>0:
          cPrint=PrintTreeview()
 
        cPrint.printTv(ls,tituloRel,arqRelPdf,lsCabs)

    # remover arq temp da lista usada na tela de detalhe da ferramenta
    def sairDetalhe():
        import os
        try:
          os.remove('newfileLista.txt')
        except:
          pass  
        master.destroy()


    #Cores
    btn = '#EB6440'
    btn_ef = '#ed8468'
    backGR = '#497174'

    # Cor de fundo filtros
    bgColor = backGR   

    
    #fonte
    fontP =('calibri', 12, 'normal')
    fontTxt=('calibri', 12, 'normal')

    # AKI PRODUCAO
    master = Toplevel()
    # AKI DEBUG
    #master = Tk()

    master.configure(bg=bgColor)
    #master.title("Consultar Solicitações")
    master.geometry('1000x600+591+215')

    photo = PhotoImage(file='imagens/report-48.png')
    master.iconphoto(False, photo)

    master.wm_resizable(width=False, height=False)

    # Nome planilha'
    nomePlanilhaDeConsulta = 'funcionarios.xlsx'

    #FRAME1 / ESPAÇAMENTO
    frame1 = Frame(master, width=900, bg=bgColor)  # ,bg='green'
    frame1.grid(row=0, column=0, sticky='nsew', pady=40)

    #FRAME1 / LABELS
    frame1 = Frame(master, width=900, bg=bgColor)  # ,bg='green'
    frame1.grid(row=1, column=0, sticky='nsew')
    Label(frame1, text="FILTROS", padx=15, font= ("Calibri",25, "bold"),
          bg=bgColor ).grid(row=0, column=0, pady=10)

    #FRAME2 / FILTROS

    frame2 = Frame(master, width=900, height=100,
                   bg=bgColor, pady=10)  # ,bg='blue'
    frame2.grid(row=2, column=0, sticky='nsew')

    # AKI CONFIGURAÇÂO LABELS FILTROS
    Label(frame2, text="Nome", bg=bgColor,font=("calibri", 14)).grid(row=0, column=0)
    Label(frame2, text="Cpf", bg=bgColor,font=("calibri", 14)).grid(row=0, column=1)
    Label(frame2, text="Turno", bg=bgColor,font=("calibri", 14)
          ).grid(row=0, column=2)
    Label(frame2, text="Equipe", bg=bgColor,font=("calibri", 14)
           ).grid(row=0, column=3)

    # PONTO DE CONFIGURAÇÃO VARs ENTRIES FILTROS // use 2
    _sNome = StringVar()
    _sCpf = StringVar()
    _sTurno = StringVar()
    _sEquipe = StringVar()

    # PONTO DE CONFIGURAÇÃO ENTRIES FILTROS
    Entry(frame2, textvariable=_sNome).grid(row=1, column=0, padx=3)
    Entry(frame2, textvariable=_sCpf).grid(row=1, column=1, padx=3)
    Entry(frame2, textvariable=_sTurno).grid(row=1, column=2, padx=3)
    Entry(frame2, textvariable=_sEquipe).grid(row=1, column=3, padx=3)

    # CONFIG AKI / CARGA DADOS DA PLANILHA EM FUNÇÃO DOS CABs FORNECIDOS NA LISTA
    lsDados = cDados.OpenReadXLSX(nomePlanilhaDeConsulta, 'tecnicos', Cab)
    print('cont row ==>', len(lsDados))

    # BTNs FILTROS
    Button(frame2, text='filtrar', bg=btn,activebackground= btn_ef,
           command=lambda: cargaTreeView(lsDados, True)).grid(row=1, column=4, padx=10)

    Button(frame2, text='refresh', bg=btn,activebackground= btn_ef,
           command=lambda: cargaTreeView(lsDados)).grid(row=1, column=5, padx=1)

    #FRAME3 / TREEVIEW
    #
    frame3 = Frame(master, width=900, height=100)  # ,bg='blue'
    frame3.grid(row=3, column=0, sticky='nsew')
    tv = ttk.Treeview(frame3, columns=(Cab), show='headings')
    # evento tv
    tv.bind('<ButtonRelease-1>', obterLinhaTv)  # <Double-1>

    for item in Cab:
        tv.column(item, minwidth=0, width=200)
        tv.heading(item, text=item)

    cargaTreeView(lsDados)

    # FRAME BUTTONS
    frame4 = Frame(master, width=900, height=100, bg=bgColor)  # ,bg='white'
    frame4.grid(row=4, column=0, sticky='nsew')

    print('lsDetalhe --------->>', lsDetalhe)
    Button(frame4, text='detalhe', command=lambda: callDetConsulta(), 
           bg=btn,activebackground= btn_ef, width=10).grid(row=3, column=4, padx=10)  # fg=forecolorBtn

    Button(frame4, text='listar', command=lambda:listarTreeView(Cab),
           bg=btn,activebackground= btn_ef, width=10).grid(row=3, column=5, padx=5)  # fg=forecolorBtn

    tv.grid(column=0, row=3, columnspan=3, pady=5, stick='w')

    #frame5 = Frame(master, width=900, height=100, bg=bgColor)  # ,bg='white'
    #frame5.grid(row=5, column=0, sticky='nsew')

    Button(master, text="retornar", width=16, height=2,
           bg=btn,activebackground= btn_ef,
           command=lambda: sairDetalhe()).place(x=800, y=544)
    # AKI DEBUG
    #master.mainloop()

# AKI DEBUG
#consultarFuncionarios()