from tkinter import ttk
from tkinter import *
from tkcalendar import *

def calendar():
   master = Tk()
   master.title("---Cadastro de técnicos---")
   master.geometry('900x600+591+215')
   master.wm_resizable(width=False,height=False)
   
   cal= Calendar(master,selectmode='day',year=2022,month=5,day=22)
   cal.pack(pady=20)

   def grab_date():
      my_label.config(text=cal.get_date())
    
   my_button= Button(master,text='Get date',command=grab_date)
   my_button.pack(pady=20)

   my_buttonOk= Button(master,text='Confirm',command='')
   my_buttonOk.pack(pady=20)

   my_buttonReturn = Button(master, text='Return', command='')
   my_buttonReturn.pack(pady=20)

   my_label = Label(master, text='')
   my_label.pack(pady=20)
   
   master.mainloop()


calendar()   

