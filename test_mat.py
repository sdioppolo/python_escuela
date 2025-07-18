import random
from tkinter import *
from tkinter import ttk

def clk_crear():
    for f in range(10):
        mat.append([None] * 10)

def clk_carga():
    for f in range(10):
        for c in range(10):
            mat[f][c] = random.randint(10,90)

def clk_muestra():
    for f in range(10):
        for c in range(10):
            salida.insert(END, str(mat[f][c]) + ' ')
        salida.insert(END,'\n')
    salida.insert(END, '-'*50+'\n')

def clk_ordena():
    for f in range(10):
        for c in range(10):
            for fc in range(10):
                for cc in range(10):
                    if(mat[f][c] > mat[fc][cc]):
                        aux = mat[f][c]
                        mat[f][c] = mat[fc][cc]
                        mat[fc][cc] = aux

mat = []
app = Tk()
app.geometry('600x600')

crear = Button(text='Crear Matriz', command=clk_crear)
carga = Button(text='Carga Matriz', command=clk_carga)
muestra = Button(text='Muestra Matriz', command=clk_muestra)
ordena = Button(text='Ordena Matriz', command=clk_ordena)
salida = Text(width=30, height=30)

crear.pack(side=TOP, expand=True, fill=X)
carga.pack(side=TOP, expand=True, fill=X)
muestra.pack(side=TOP, expand=True, fill=X)
ordena.pack(side=TOP, expand=True, fill=X)
salida.pack(side=TOP, expand=True, fill=BOTH)

app.mainloop()
