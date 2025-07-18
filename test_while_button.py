import time
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def contador():
    if(cont[0] < 10):
        mensaje.configure(text=str(cont[0])+'\n')
        cont[0] += 1


cont=[int(0)]

app = Tk()
app.geometry('200x200')
app.title('Probando while de consola contra boton')

mensaje = Label(text=' ', width=50)
accion = Button(text='accion', command=contador)

mensaje.pack()
accion.pack()

app.mainloop()

