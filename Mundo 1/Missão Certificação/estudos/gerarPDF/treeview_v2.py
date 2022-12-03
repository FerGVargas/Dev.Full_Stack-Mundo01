from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from cPrintTreeView_v2 import PrintTreeview

def inserir():
    if vid.get()=="" or vnome.get()=="" or  vfone.get()=="":
        messagebox.showinfo(title='ERRO', message='Digite todos os dados')
        return

    tv.insert("","end",values=(vid.get(),vnome.get(),vfone.get()))
    vid.delete(0,'end')
    vnome.delete(0,'end')
    vfone.delete(0,'end')

def deletar():
   try:
      itemSelecionado=tv.selection()[0]
      tv.delete(itemSelecionado)
   except:
     messagebox.showinfo(title='ERRO',message='Selecione um elemento')


def obter():
  itemSelecionado=tv.selection()[0]
  valores=tv.item(itemSelecionado,'values')

   
  print('valores -->',valores) 


#preciso de todos para realizar a impressao
def lerTodos():
      ls=[]
      for item in tv.get_children():
          item2=tv.item(item) 
          valores=tv.item(item,'values')
          print(item2) # aki reconheco um dicionario 
          print(item2['values']) #aki reconheço a lista contendo info
          print(valores) # esse e  o usado na impressao
          ls.append(valores)
      
      print(ls)

      if len(ls)>0:
         cPrint=PrintTreeview()    
      
      cPrint.printTv(ls,'agenda','agenda.pdf',lsCabs)

app=Tk()
app.title("teste")
app.geometry('650x350+591+215')

lbid=Label(app,text="ID")
vid=Entry(app)

lbnome=Label(app,text="Nome")
vnome=Entry(app)

lbfone=Label(app,text="Fone")
vfone=Entry(app)

lsCabs=['id','nome','fone']

tv=ttk.Treeview(app,columns=('id','nome','fone'),show='headings')
 
tv.column('id', minwidth=0,width=50)
tv.column('nome',minwidth=0,width=250)
tv.column('fone',minwidth=0,width=100)
tv.heading('id',text='ID')
tv.heading('nome',text='NOME')
tv.heading('fone',text='TELEFONE')

btn_inserir=Button(app,text='Inserir',command=inserir)
btn_deletar=Button(app,text='Deletar',command=deletar)
btn_obter=Button(app,text='Obter',command= obter)
btn_todos=Button(app,text='todos',command= lerTodos)

lbid.grid(column=0,row=0,stick='w')
vid.grid(column=0,row=1 )

lbnome.grid(column=1,row=0,stick='w')
vnome.grid(column=1,row=1 )

lbfone.grid(column=2,row=0,stick='w')
vfone.grid(column=2,row=1   )

tv.grid(column=0,row=3,columnspan=3,pady=5,stick='w')

btn_inserir.grid(column=0,row=4 )
btn_deletar.grid(column=1,row=4 )
btn_obter.grid(column=2,row=4)
btn_todos.grid(column=3,row=4)

app.mainloop()




  
