from tkinter import *
from tkinter import ttk
 
bgColor = 'azure3'  # cyan,azure

bgColorbtn = 'green'  # cyan,azure
forecolorBtn = 'white'


master = Tk()

master.configure(bg=bgColor)
master.title("---Ferramentas---")
master.geometry('900x600+591+215')

 
#pathImg+='ferramentas.jpg'

#imagem grande dá erro 
#pathImg='img/ferramentas.jpg'
#'img/toolsIco.png'

#photo = PhotoImage(file = 'img/toolsIco-48.png')
photo = PhotoImage(file = 'imagens/toolsIco-48.png')# es.ico
master.iconphoto(False, photo)
 
master.wm_resizable(width=False, height=False)

master.mainloop()