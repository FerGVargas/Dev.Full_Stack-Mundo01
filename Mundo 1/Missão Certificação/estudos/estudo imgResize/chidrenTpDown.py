
# importing only those functions
# which are needed
from tkinter import * 
from tkinter.ttk import *
from PIL import Image, ImageTk 
import os.path

# creating tkinter window

def telaBtn():
    #root = Tk()
    root = Toplevel()
    root.geometry('350x200+1150+315')
    # Adding widgets to the root window
    Label(root, text = 'GeeksforGeeks', font =(
    'Verdana', 15)).pack(side = TOP, pady = 10)
    
    _sDataSaida=StringVar()
    Label(root, textvariable=_sDataSaida, font =(
    'Verdana', 15)).pack(side = TOP, pady = 10)
    

    img = Image.open("imagens/img_cad_ferr.png")
    imgNw=img.resize((48, 48))
    my_img=ImageTk.PhotoImage(imgNw)
 
    #photo = PhotoImage(file = r"imagens/img_cad_ferr.png")
    
    # here, image option is used to
    # set image on button
    my=Button(root, text = 'Click Me !', image = my_img,command=lambda:telaInterna(root)).pack(side = TOP)
    

    def telaInterna(root):
        rootIn = Toplevel(root)
        rootIn.geometry('450x500+1150+315')
            # Adding widgets to the root window
        Label(rootIn, text = 'Tela interna', font =(
                     'Verdana', 15)).grid(row=0,column=0)
        
        Button(rootIn, text = 'Click AKI !',command=lambda:imprimeStrng()).grid(row=2,column=0)
        Button(rootIn, text = 'VOLTAR !',command=lambda:quit1()).grid(row=3,column=0)
             

        def imprimeStrng():
            _sDataSaida.set('Foi !!!!') 
        
        def quit1():
            rootIn.destroy()
 
    my.draw()
    #mainloop()