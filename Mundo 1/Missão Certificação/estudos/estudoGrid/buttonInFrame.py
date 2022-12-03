from tkinter import ttk
from tkinter import *

master = Tk()

master.title("---Ferramentas---")
master.geometry('900x600+591+215')
master.wm_resizable(width=False,height=False) 

#Uma linha e abaixo tres colunas
frame1=Frame(master,width=450,height=200,bg='green') 
frame1.grid(row=0,column=0)
Button(frame1, text="confimar1", width=16, height=2, bg="orange",command='').pack(fill='both',pady=40,padx=30)#,ipady=3

frame2=Frame(master,width=450,height=200,bg='blue') 
frame2.grid(row=0,column=1)
Button(frame2, text="confimar2", width=16, height=2, bg="orange",command='').pack(fill='both',pady=40,padx=30)#,ipady=3

frame3=Frame(master,width=450,height=200,bg='white') 
frame3.grid(row=1,column=0)
Button(frame3, text="confimar3", width=16, height=2, bg="orange",command='').pack(fill='both',pady=40,padx=30)#,ipady=3

frame4=Frame(master,width=450,height=200,bg='yellow') 
frame4.grid(row=1,column=1)
Button(frame4, text="confimar4", width=16, height=2, bg="orange",command='').pack(fill='both',pady=40,padx=30)#,ipady=3

frame5=Frame(master,width=450,height=200,bg='orange') 
frame5.grid(row=2,column=0)
Button(frame5, text="confimar5", width=16, height=2, bg="orange",command='').pack(fill='both',pady=40,padx=30)#,ipady=3

frame6=Frame(master,width=450,height=200,bg='Turquoise') 
frame6.grid(row=2,column=1)
Button(frame6, text="confimar6", width=16, height=2, bg="orange",command='').pack(fill='both',pady=40,padx=30)#,ipady=3

master.mainloop()