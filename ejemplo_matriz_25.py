import random
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from functools import partial

def crea_matriz():
    for f in range (int(e_fil.get())):
        mat.append([None] * int(e_col.get()))

def carga_matriz():
    ini = int(e_ini.get())
    fin = int(e_fin.get())
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c] = random.randint(ini, fin)

def muestra_matriz():
    for f in range(len(mat)):
        fila = ''
        for c in range(len(mat[f])):
            fila += str(mat[f][c]) + ' '
        salida.insert(END, fila + '\n')



mat = []
app = Tk()
app.geometry('600x600')
app.title('Ejemplo Matriz')

frm_crea = Frame(app)
l_fil = Label(frm_crea, text='Filas: ')
e_fil = Entry(frm_crea, width=10)
l_col = Label(frm_crea, text='Columnas: ')
e_col = Entry(frm_crea, width=10)
crear = Button(frm_crea, text='Crear Matriz', command=crea_matriz)
l_fil.grid(row=0, column=0)
e_fil.grid(row=0, column=1)
l_col.grid(row=1, column=0)
e_col.grid(row=1, column=1)
crear.grid(row=2, column=0, columnspan=2)
frm_crea.pack(padx=5, pady=5, expand=True, fill=X)

frm_carga = Frame(app)
l_ini = Label(frm_carga, text='Rango Inicial: ')
e_ini = Entry(frm_carga, width=10)
l_fin = Label(frm_carga, text='Rango Final: ')
e_fin = Entry(frm_carga, width=10)
carga = Button(frm_carga, text='Carga Matriz', command=carga_matriz)
l_ini.grid(row=0, column=0)
e_ini.grid(row=0, column=1)
l_fin.grid(row=1, column=0)
e_fin.grid(row=1, column=1)
carga.grid(row=2, column=0, columnspan=2)
frm_carga.pack(padx=5, pady=5, expand=True, fill=X)

frm_salida = Frame(app)
muestra = Button(frm_salida, text='Muestra Matriz', command=muestra_matriz)
salida = Text(frm_salida, height=30, width=40, font=('DejaVu Sans Mono',14,'normal'))
muestra.grid(row=0, column=0, columnspan=2)
salida.grid(row=1, column=0, columnspan=2)
frm_salida.pack(padx=5, pady=5, expand=True, fill=X)

app.mainloop()
