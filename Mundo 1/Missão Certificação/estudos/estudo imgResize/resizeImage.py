# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Load the image
image=Image.open('imagens/img_cad_ferr.png')

# Resize the image in the given (width, height)
img=image.resize((150, 250))

# Conver the image in TkImage
my_img=ImageTk.PhotoImage(img)

# Display the image with label
label=Label(win, image=my_img)
label.pack()

win.mainloop()