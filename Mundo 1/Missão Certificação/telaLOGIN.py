from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

from time import *
# Cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#497174"  # branca / white
co2 = "#EB6440"  # verde / green 
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

# Criando janelas ---------------------
janela = Tk()
janela.title('Tela de LOGIN')
janela.geometry('280x320+491+115')
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
        #nova_janela()
    elif credenciais[0] == nome and credenciais[1]==senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta! ' +credenciais[0])

        janela.destroy()
        time.sleep(0.3)
        #nova_janela()

    else:
        messagebox.showwarning('Erro', 'Verifique o nome e a senha!')

# Função de verificação ---------------------
def nova_janela():
    # Configurando o frame cima
    l_nome = Label(frame_cima, text='Usuario : ' +credenciais[0], anchor=NE,font=('calibri 10'),bg=co1)
    l_nome.place(x=5,y=5)

    l_linha = Label(frame_cima, text='', width=275,anchor=NW,font=('calibri 1'),bg=co2)
    l_linha.place(x=10,y=45)

    l_nome = Label(frame_baixo, text='Seja bem vindo ' +credenciais[0], anchor=NE,font=('calibri 10'),bg=co1)
    l_nome.place(x=5,y=105)




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
