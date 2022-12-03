from tkinter import *
import tkinter as tk
import tkinter as tkk

from tkinter import messagebox
import time 


from ferramentasCadastro import cadastroFerramentas
from ferramentasConsultas import consultarFerramentas

from funcionariosCadastro import cadastroFuncionarios
from funcionariosConsultas import consultarFuncionarios

from solicitacoesCadastro import cadastroSolicitacoes
from solicitacoesConsultas import consultarSolicitacoes


# botão
btn = '#EB6440'
backGR = '#497174'

# Cores login -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#497174"  # branca / white
co2 = "#EB6440"  # verde / green 
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters


def telaMain():

    #janela
    master = tk.Tk()
    master.title("Controle de Ferramentas e Funcionários")
    master.geometry('995x643+491+115')
    master.wm_resizable(width=False,height=False)
    master['background'] = backGR
    #Ícone
    photo = PhotoImage(file='imagens/toolsIco-48.png')
    master.iconphoto(False, photo)
    #fonte
    fontP =('calibri', 12, 'normal')
    fontTxt=('calibri', 12, 'normal')
    #Responsividade
    top = Frame(master)
    bottom = Frame(master)
    top.pack(side=TOP, pady=30)
    bottom.pack(side=BOTTOM, pady=60)#, fill=BOTH, expand=True)
    top['background'] = backGR
    bottom['background'] = backGR

    #Seção de ferramentas
    #photoFer = PhotoImage(file="C:/Users/fabio.prado/Documents/GitHub/cerificacaoM1Estacio/imagens/fer.gif")
    titFerramentas = Label(top, text="Sessão de Ferramentas", font=fontTxt, bg=backGR)
    cadferramentas = tk.Button(top, text="Cadastro de Ferramentas", bg=btn, font=fontP, command=cadastroFerramentas)
    consferramentas = tk.Button(top, text="Consulta de Ferramentas", bg=btn, font=fontP, command=consultarFerramentas)

    #Funcionarios
    titFuncionarios = Label(top, text="Controle de Funcionários", font=fontTxt, bg=backGR)
    cadfuncionarios = tk.Button(top, text="Cadastrar Funcionário", bg=btn, font=fontP, command=cadastroFuncionarios)
    consfuncionarios = tk.Button(top, text="Consultar Funcionário", bg=btn, font=fontP, command=consultarFuncionarios)


    #solicitações
    titSolicitacoes = Label(bottom, text="Área de Solicitações", font=fontTxt, bg=backGR)
    bSCadastro = tk.Button(bottom, text="Cadastrar Solicitações", bg=btn, font=fontP, command=cadastroSolicitacoes)
    bSconsult = tk.Button(bottom, text="Consultar Solicitações", bg=btn, font=fontP, command=consultarSolicitacoes)

    titFerramentas.grid(row=0, column=0, padx=0, pady=0)
    titFuncionarios.grid(row=0, column=2, padx=10, pady=0)
    cadferramentas.grid(row=0, column=1, padx=50, pady=5)
    consferramentas.grid(row=1, column=1, padx=50, pady=5)
    cadfuncionarios.grid(row=0, column=3, padx=0, pady=0)
    consfuncionarios.grid(row=1, column=3, padx=0, pady=0)
    titSolicitacoes.grid(row=4, column=1, padx=0, pady=0)
    bSCadastro.grid(row=5, column=1, padx=5, pady=0)
    bSconsult.grid(row=5, column=2, padx=5, pady=0)


    img = PhotoImage(file='imagens/workers-g-256.png')
    label_image= Label(master,image=img).place(x=280,y=185) 
    #label_image.pack()

    master.mainloop()

def telaLogin():
    # Criando janelas ---------------------
    janela = Tk()
    janela.title('Tela de LOGIN')
    janela.geometry('280x320+891+315')
    photo = PhotoImage(file='imagens/toolsIco-48.png')
    janela.iconphoto(False, photo)
    janela.configure(background=co1)
    janela.resizable(width=FALSE,height=FALSE)

    # Dividindo janelas ---------------------
    frame_cima = Frame(janela,width=270,height=50,bg=co1,relief='flat')
    frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

    frame_baixo = Frame(janela,width=270,height=250,bg=co1,relief='flat')
    frame_baixo.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

    # Configurando o frame cima ---------------------
    l_nome = Label(frame_cima, text='LOGIN', anchor=NE,font=('calibri 25 normal'),bg=co1)
    l_nome.place(x=5,y=5)

    l_linha = Label(frame_cima, text='', width=150,anchor=NW,font=('calibri 12 normal'),bg=co2)
    l_linha.place(x=10,y=45)


    credenciais = ['xxx', '12345'] 

    # Função para verificar senha  ---------------------
    def verificar_senha():
        nome = e_nome.get()
        senha = e_pass.get()

        if nome =='admin' and senha =='admin':
            messagebox.showinfo('Login', 'Seja bem vindo admin!')
            janela.destroy()
            time.sleep(0.3)
            telaMain()
             
        elif credenciais[0] == nome and credenciais[1]==senha:
            messagebox.showinfo('Login', 'Seja bem vindo de volta! ' +credenciais[0])

            janela.destroy()
            time.sleep(0.3)
            telaMain()

        else:
            messagebox.showwarning('Erro', 'Verifique o nome e a senha!')

 
    # Configurando o frame baixo ---------------------
    l_nome = Label(frame_baixo, text='Nome ', anchor=NW,font=('calibri 12 normal'),bg=co1)
    l_nome.place(x=10,y=20)
    e_nome = Entry(frame_baixo, width=25,justify='left',font=("", 15))
    e_nome.place(x=14,y=50)

    l_pass = Label(frame_baixo, text='Senha ', anchor=NW,font=('calibri 12 normal'),bg=co1)
    l_pass.place(x=10,y=100)
    e_pass = Entry(frame_baixo, width=25,justify='left',show='*',font=("", 15))
    e_pass.place(x=14,y=130)

    b_confirmar = Button(frame_baixo,command=verificar_senha ,text='Entrar', width=25,height=2,font=('calibri 10 bold'),bg=co2)
    b_confirmar.place(x=15,y=180)

    janela.mainloop()

if __name__ == "__main__":
    telaLogin()
