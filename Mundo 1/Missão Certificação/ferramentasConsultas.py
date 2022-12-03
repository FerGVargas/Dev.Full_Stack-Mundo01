from tkinter import *
from tkinter import ttk
from tkinter import messagebox


from dadosXLSX import Dados
from cPrintTreeView import PrintTreeview

from ferramentasDetalhe import detalheFerramenta
cDados = Dados()


def consultarFerramentas():

    global lsDetalhe
    global lsDados
    lsDetalhe = []
    lsDados=[]

    # PONTO DE CONFIGURAÇÃO / CABEÇARIO DO TREEVIEW
    Cab = [
        'ind',
        'Codigo',
        'Descricao',
        'Fabricante',
        'Voltagem',
        'PartNumber',
        'Tamanho',
        'Unidade',
        'TpFerramenta',
        'Material'
    ]

    # PONTO DE CONFIGURAÇÃO PDF / nome arquivo e titulo
    arqRelPdf = 'ListaFerramentas.pdf'
    tituloRel = 'Lista de ferramentas'

    # PONTO DE CONFIGURAÇÃO / INDICES DOS FILTROS
    listaFiltros = {'codigo': 1, 'descricao': 2,
                    'fabricante': 3, 'material': 9}

    # PONTO DE CONFIGURAÇÃO FILTRO
    def limparFiltros():
        _scodigo.set('')
        _sdescricao.set('')
        _sfabricante.set('')
        _smaterial.set('')

    # FUNÇÃO DE FILTROS
    # função usada dentro da CARGATREEVIEW

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
        codigo = _scodigo.get().upper()
        descricao = _sdescricao.get().upper()
        fabricante = _sfabricante.get().upper()
        material = _smaterial.get().upper()

        if codigo != '':
            #print('tulipa ------',listaFiltros['codigo'])
            lsReturnAll = getFilter(listaTodos, codigo, listaFiltros['codigo'])

        if len(lsReturnAll) == 0:
            lsReturnAll = getFilter(
                listaTodos, descricao, listaFiltros['descricao'])
        else:
            lsReturnAll = getFilter(
                lsReturnAll, descricao, listaFiltros['descricao'])

        if len(lsReturnAll) == 0:
            lsReturnAll = getFilter(
                listaTodos, fabricante, listaFiltros['fabricante'])
        else:
            lsReturnAll = getFilter(
                lsReturnAll, fabricante, listaFiltros['fabricante'])

        if len(lsReturnAll) == 0:
            lsReturnAll = getFilter(
                listaTodos, material, listaFiltros['material'])
        else:
            lsReturnAll = getFilter(
                lsReturnAll, material, listaFiltros['material'])

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
    
    def refresh():
        lsDados = cDados.OpenReadXLSX(nomePlanilhaDeConsulta, 'ferramentas', Cab, 1)
        cargaTreeView(lsDados)        
    # Tratamento da chamada a tela de detalhe da ferramenta
    def deletarItem(lsDados):

        def FerramentaAlocada(codFerr):
           bReturn=False
           nItensCabSolicitacoes=9
           ls2=cDados.OpenFindDateXLSX('solicitacoes.xlsx','solicitacoes',codFerr,nItensCabSolicitacoes)

           #verificar data da entrega maior q data atual
           if len(ls2)>0:
               print('dados ferr==>>>',ls2)
               #['827.177.323.91', 'Marco', 'NOITE', 'DJS-IW-90', '13/11/2022', '09:00:00', '14/11/2022', '10:00:00', 'TRABALHO', 'SIM']
            
               if ls2[9]!='SIM':
                 msg='Ferramenta não pode ser removida devido a estar alocada com ' + ls2[1] + ', com previsão de entrega para ' + ls2[6] + ' as ' + ls2[7]
               else:   
                 msg='Ferramenta não pode ser removida devido a estar reservada para ' + ls2[1] + ', com previsão de saida para ' + ls2[4] + ' as ' + ls2[5]+' a ser confirmada'  

               messagebox.showinfo('Erro',msg,parent=master)

               bReturn=True
           
           return bReturn 
        
        lsDetalhe=cDados.readFileTemp()
        print('lsDetalhe delete==>>',lsDetalhe)
        
        if FerramentaAlocada(lsDetalhe[1])== False:
           resposta =messagebox.askokcancel(title='Confirme',message='confirma a remoção da ferramenta '+lsDetalhe[1]+' ?',parent=master)

           if resposta:
              cDados.DeleteOneXLSX('ferramentas.xlsx','ferramentas',lsDetalhe[0]) 
              lsDados = cDados.OpenReadXLSX(nomePlanilhaDeConsulta, 'ferramentas', Cab, 1)
              print('lsDados remover-->>',lsDados)
              cargaTreeView(lsDados)  

    def callDetFerramenta():
        try:
            with open('newfileLista.txt', 'r') as f:
                detalheFerramenta()
        except IOError:
            messagebox.showinfo('Aviso', 'Necessário selecionar uma linha')

    # IMPRIME TREEVIEW
    def listarTreeView(lsCabs):
        ls = []
        for item in tv.get_children():
            item2 = tv.item(item)
            valores = tv.item(item, 'values')
            print(item2)  # aki reconheco um dicionario
            print(item2['values'])  # aki reconheço a lista contendo info
            print(valores)  # esse e  o usado na impressao
            ls.append(valores)

        # print(ls)

        if len(ls) > 0:
            cPrint = PrintTreeview()

        cPrint.printTv(ls, tituloRel, arqRelPdf, lsCabs)

    # remover arq temp da lista usada na tela de detalhe da ferramenta
    def sairDetalhe():
        import os
        try:
            os.remove('newfileLista.txt')
        except:
            pass
        master.destroy()

    # Cores
    btn = '#EB6440'
    btn_ef = '#ed8468'
    backGR = '#497174'

    # Cor de fundo filtros
    bgColor = backGR  # cyan,azure

    # Cor btns
    bgColorbtn = 'green'  # cyan,azure
    forecolorBtn = 'white'

    # fonte
    fontP = ('calibri', 12, 'normal')
    fontTxt = ('calibri', 12, 'normal')

    # AKI PRODUCAO
    master = Toplevel()
    # AKI DEBUG
    #master = Tk()

    master.configure(bg=bgColor)
    # master.title("---Ferramentas---")
    master.geometry('950x600+591+215')

    photo = PhotoImage(file='imagens/report-48.png')
    master.iconphoto(False, photo)

    master.wm_resizable(width=False, height=False)

    # Nome planilha'
    nomePlanilhaDeConsulta = 'ferramentas.xlsx'

    #FRAME1 / ESPAÇAMENTO
    frame1 = Frame(master, width=900, bg=bgColor)  # ,bg='green'
    frame1.grid(row=0, column=0, sticky='nsew', pady=40)

    #FRAME1 / LABELS
    frame1 = Frame(master, width=900, bg=bgColor)  # ,bg='green'
    frame1.grid(row=1, column=0, sticky='nsew')
    Label(frame1, text="FILTROS", padx=390, font=("Calibri", 25, "bold"),
          bg=bgColor).grid(row=0, column=0, pady=10)

    #FRAME2 / FILTROS

    frame2 = Frame(master, width=900, height=100,
                   bg=bgColor, pady=10)  # ,bg='blue'
    frame2.grid(row=2, column=0, sticky='nsew')

    Label(frame2, text="Código", bg=bgColor, font=("calibri", 14)
          ).grid(row=0, column=0)
    Label(frame2, text="Descrição", bg=bgColor, font=("calibri", 14)
          ).grid(row=0, column=1)
    Label(frame2, text="Fabricante", bg=bgColor, font=("calibri", 14)
          ).grid(row=0, column=2)
    Label(frame2, text="Material", bg=bgColor, font=("calibri", 14)
          ).grid(row=0, column=3)

    # PONTO DE CONFIGURAÇÃO VARs ENTRIES FILTROS
    _scodigo = StringVar()
    _sdescricao = StringVar()
    _sfabricante = StringVar()
    _smaterial = StringVar()

    # PONTO DE CONFIGURAÇÃO textvariable= <variaveis acima>
    Entry(frame2, textvariable=_scodigo).grid(row=1, column=0, padx=3)
    Entry(frame2, textvariable=_sdescricao).grid(row=1, column=1, padx=3)
    Entry(frame2, textvariable=_sfabricante).grid(row=1, column=2, padx=3)
    Entry(frame2, textvariable=_smaterial).grid(row=1, column=3, padx=3)

    # CARGA DADOS DA PLANILHA EM FUNÇÃO DOS CABs FORNECIDOS NA LISTA
    lsDados = cDados.OpenReadXLSX(
        nomePlanilhaDeConsulta, 'ferramentas', Cab, 1)

    # BTNs FILTROS
    Button(frame2, font=fontTxt, text='filtrar', bg=btn, activebackground=btn_ef,
           command=lambda: cargaTreeView(lsDados, True)).grid(row=1, column=4, padx=10)

    Button(frame2, font=fontTxt, text='refresh', bg=btn, activebackground=btn_ef,
           command=lambda: refresh()).grid(row=1, column=5, padx=1)

    #FRAME3 / TREEVIEW
    #
    frame3 = Frame(master, width=900, height=100)  # ,bg='blue'
    frame3.grid(row=3, column=0, sticky='nsew')
    tv = ttk.Treeview(frame3, columns=(Cab), show='headings')
    # evento tv
    tv.bind('<ButtonRelease-1>', obterLinhaTv)  # <Double-1>

    for item in Cab:
        if item == 'ind':
            tv.column(item, minwidth=0, width=30)
        else:
            tv.column(item, minwidth=0, width=100)
        tv.heading(item, text=item)

    print('cargaTreeView lsDados--->>', lsDados)
    cargaTreeView(lsDados)

    # FRAME BUTTONS
    frame4 = Frame(master, width=900, height=100, bg=bgColor)  # ,bg='white'
    frame4.grid(row=4, column=0, sticky='nsew')

    print('lsDetalhe --------->>', lsDetalhe)
    Button(frame4, font=fontTxt, text='detalhe', command=lambda: callDetFerramenta(), bg=btn,
           activebackground=btn_ef, width=10).grid(row=3, column=4, padx=10)  # fg=forecolorBtn

    Button(frame4, font=fontTxt, text='listar', command=lambda: listarTreeView(Cab), bg=btn,
           activebackground=btn_ef, width=10).grid(row=3, column=5, padx=5)  # fg=forecolorBtn

    Button(frame4, font=fontTxt, text='deletar', command=lambda: deletarItem(lsDados), bg=btn,
           activebackground=btn_ef, width=10).grid(row=3, column=6, padx=5)  # fg=forecolorBtn

    tv.grid(column=0, row=3, columnspan=3, pady=5, stick='w')

    Button(master, font=fontTxt, text="retornar", width=16, height=2, bg=btn,
           activebackground=btn_ef, command=lambda: sairDetalhe()).place(x=696, y=544)
    # AKI DEBUG
    #master.mainloop()


#consultarFerramentas()
