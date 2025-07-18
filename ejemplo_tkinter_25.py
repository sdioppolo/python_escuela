from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def acciones():
    if(len(nombre.get()) > 0):
        lista.insert(END,nombre.get()+'\n')
        nombre.delete(0,END)
        if(len(vec_nombre_d) < 5):
            vec_nombre_d.append(nombre.get())
            vec_nombre_f[vec_cont[0]] = nombre.get()
            vec_cont[0] += 1
        else:
            messagebox.showerror(title='Error!!!',
                                 message='No hay más capacidad.')
            

#-------------------------------------------------------------------------
vec_nombre_d = []
vec_nombre_f = [None] * 5
vec_cont = [0]

ventana = Tk() # ventana principal
ventana.geometry('400x400')
ventana.title('Mi primer ventana')

cartel = Label(text='Hola Mundo Tkinter!!!', borderwidth=1,relief=GROOVE)
nombre = Entry(width=30)
entrada = Button(text='Aceptar', command=acciones)
lista = Text(height=10,width=30)

cartel.pack()
nombre.pack()
entrada.pack()
lista.pack()

nombre.focus()

ventana.mainloop()
