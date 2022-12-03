
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

app=Tk()
app.title("teste")
app.geometry('550x350+591+215')

def imprimir(value):
    print('foi ----->>>',value) 

  
Button(app, text='consultar',
           command= lambda: imprimir('123 testando')).grid(row=0,column=0) 
 
app.mainloop()

          