import random
from tkinter import *
from tkinter import ttk

def crea_matriz():
    for f in range(10):
        mat.append([None] * 10)

    for f in range(10):
        for c in range(10):
            mat[f][c] = random.randint(100,900)

    for f in range(10):
        fila = ''
        for c in range(10):
            fila += str(mat[f][c])+' '
        t1.insert(END, fila + '\n')
    
mat = []
app = Tk()
app.geometry('400x400')
app.title('Ejemplo Muestra Matriz en Text')

b1 = Button(text='Crear y Mostrar Matriz', command=crea_matriz)
t1 = Text(width=40, height=20)

b1.pack(side=TOP, expand=True, fill=X)
t1.pack(side=BOTTOM, expand=True, fill=BOTH)

app.mainloop()
