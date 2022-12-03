import time
from tkinter import *
from tkinter import messagebox
#import tkinter


def janela1():
    def atualizaTime():
        now = time.strftime("%H:%M:%S")
        label.configure(text=now)
        print('atualizaTime')

    def atualizaTexto():
        msg=messagebox.showinfo('texto atual',text.get())

    jnl = Tk()
    jnl.title('teste janelas')
    jnl.geometry("500x500")
    label = Label(master=jnl,text="00:00:00")
    label.pack()


    btn = Button(master=jnl,text='hora certa',command = atualizaTime)
    btn.place(x=200, y=400)

    text = Entry(jnl)
    #text.grid(row=0,column=1)
    text.pack()
    btn2 = Button(master=jnl, text='aki escreve', command=atualizaTexto)
    #btn2.grid(row=0, column=2)
    btn2.pack()
    #btn.pack()

    jnl.mainloop()
