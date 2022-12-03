# import tkinter module
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

# creating main tkinter window/toplevel

def janela2():

    def atualizaTexto():
        msg=messagebox.showinfo('texto atual',e1.get())

    master = Tk()

# this will create a label widget
    l1 = Label(master, text="First:")
    l2 = Label(master, text="Second:")

# grid method to arrange labels in respective
# rows and columns as specified
    l1.grid(row=0, column=0, sticky=W, pady=2)
    l2.grid(row=1, column=0, sticky=W, pady=2)

# entry widgets, used to take entry from user
    e1 = Entry(master)
    e2 = Entry(master)

# this will arrange entry widgets
    e1.grid(row=0, column=1, pady=2)
    e2.grid(row=1, column=1, pady=2)

# aki btn
    btn = Button(master=master, text='aki escreve', command=atualizaTexto)
    btn.grid(row=2, column=1, pady=100)

# infinite loop which can be terminated by keyboard
# or mouse interrupt
    master.mainloop()
    