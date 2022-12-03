import tkinter as tk
# https://www.youtube.com/watch?v=OPUSBBD2OJw&t=645s
from tkinter import ttk

tkwindow = tk.Tk()

cbox = ttk.Combobox(tkwindow, values=[1,2,3], state='readonly')
cbox.grid(column=0, row=0)


def callback(event):
    print('Foiii')


def callback2(event):
    print('Foiii2')
cbox.bind("<<ComboboxSelected>>", callback2)

tkwindow.mainloop()