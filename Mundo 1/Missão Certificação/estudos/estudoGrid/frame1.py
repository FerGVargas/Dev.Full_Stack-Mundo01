 
    
from tkinter import ttk
from tkinter import *

master = Tk()

master.title("---Ferramentas---")
master.geometry('900x600+591+215')
master.wm_resizable(width=False,height=False) 
"""
#horizontal
frame1=Frame(master,width=900,height=200,bg='green') 
frame1.grid(row=0,column=0)
frame2=Frame(master,width=900,height=200,bg='blue') 
frame2.grid(row=1,column=0)
frame3=Frame(master,width=900,height=200,bg='white') 
frame3.grid(row=2,column=0)


#tres colunas
frame1=Frame(master,width=300,height=200,bg='green') 
frame1.grid(row=0,column=0)
frame2=Frame(master,width=300,height=200,bg='blue') 
frame2.grid(row=0,column=1)
frame3=Frame(master,width=300,height=200,bg='white') 
frame3.grid(row=0,column=2)
#todas as colunas
frame4=Frame(master,width=900,height=400,bg='yellow') 
frame4.grid(row=1,column=0,columnspan=3)
"""

#Uma linha e abaixo tres colunas
frame1=Frame(master,width=900,height=200,bg='green') 
frame1.grid(row=0,column=0,columnspan=3)
frame2=Frame(master,width=300,height=200,bg='blue') 
frame2.grid(row=1,column=1)
frame3=Frame(master,width=300,height=200,bg='white') 
frame3.grid(row=1,column=2)
frame4=Frame(master,width=300,height=200,bg='yellow') 
frame4.grid(row=1,column=0)

"""   
frame1=Frame(master,width=900,height=100,bg='green') 
frame1.grid(row=0,column=0)
frame2=Frame(master,width=300,height=500,bg='blue') 
frame2.grid(row=1,column=0)
frame3=Frame(master,width=300,height=500,bg='white') 
frame3.grid(row=1,column=1)
frame4=Frame(master,width=300,height=500,bg='yellow') 
frame4.grid(row=1,column=2)  
"""
master.mainloop()
