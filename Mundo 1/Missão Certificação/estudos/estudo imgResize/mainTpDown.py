
# importing only those functions
# which are needed
from tkinter import * 
from tkinter.ttk import *
from chidrenTpDown import telaBtn   
# creating tkinter window

def telaMain():
    master = Tk()
  
    # Adding widgets to the root window
    Label(master, text = 'GeeksforGeeks', font =(
    'Verdana', 15)).pack(side = TOP, pady = 10)
    
    # Creating a photoimage object to use image
    photo = PhotoImage(file = "imagens/img_cad_ferr.png")
    
    # here, image option is used to
    # set image on button
    Button(master, text = 'tela btn !', image = photo,command=lambda:telaBtn()).pack(side = TOP)
    
    mainloop()

telaMain()    