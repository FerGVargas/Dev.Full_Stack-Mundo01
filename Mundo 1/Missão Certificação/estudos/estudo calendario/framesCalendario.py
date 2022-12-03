from tkinter import ttk
from tkinter import *

master = Tk()

master.title("---Ferramentas---")
master.geometry('900x600+591+215')
master.wm_resizable(width=False,height=False) 
 
#Uma linha e abaixo tres colunas
frame1=Frame(master,width=900,height=200,bg='green') 
frame1.grid(row=0,column=0,columnspan=3)

frame2=Frame(master,width=300,height=200,bg='blue') 
frame2.grid(row=1,column=0,sticky='nsew')


#OU É PACK PARA TODOS OU E GRID


my_label2 = Label(frame2, text='teste',background='AntiqueWhite2')
my_label2.grid(row=0,column=0,padx=10,pady=5)
#my_label2.pack(fill='both',pady=10)

my_label1 = Label(frame2, text='teste',background='AliceBlue')
my_label1.grid(row=1,column=0,padx=10,pady=15)
#my_label1.pack(fill='both',pady=10)
my_buttonReturn1 = Button(frame2, text='Return', command='')
my_buttonReturn1.grid(row=1,column=1) 
#my_buttonReturn1.pack(fill='both',pady=10)

my_label3 = Label(frame2, text='teste',background='AntiqueWhite3')
my_label3.grid(row=2,column=0,padx=10,pady=15)

frame3=Frame(master,width=300,height=200,bg='white') 
frame3.grid(row=1,column=1,sticky='nsew')


my_buttonReturn = Button(frame3, text='Return', command='')
my_buttonReturn.grid(row=0,column=0) 

my_label = Label(frame3, text='teste',background='AliceBlue')
my_label.grid(row=0,column=1,padx=10,pady=135)


frame4=Frame(master,width=300,height=200,bg='yellow') 
frame4.grid(row=1,column=2,sticky='nsew')
 
master.mainloop()
