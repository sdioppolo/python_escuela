import time
import random
from tkinter import Tk
from tkinter import Button
from tkinter import ttk
from tkinter import IntVar
from tkinter import messagebox
from tkinter import PhotoImage

def crea_matriz_num():
    # ----------------------
    # 0 - camino
    # 1 - pared
    # 2 - caja movil
    # 3 - destino
    # 4 - caja fija
    # ----------------------
    m_n = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
           [1, 3, 0, 0, 0, 0, 0, 0, 0, 1], 
           [1, 0, 0, 0, 3, 1, 0, 4, 0, 1], 
           [1, 0, 4, 0, 1, 1, 0, 0, 0, 1], 
           [1, 0, 0, 0, 0, 0, 0, 2, 0, 1], 
           [1, 0, 2, 0, 4, 0, 0, 1, 1, 1], 
           [1, 0, 0, 0, 0, 2, 0, 0, 0, 1], 
           [1, 0, 1, 1, 0, 1, 0, 0, 0, 1], 
           [1, 0, 0, 0, 0, 0, 0, 3, 0, 1], 
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    return m_n

# --------------------------------------------------------------------
def crea_matriz_img(fi, co):
    m_i = [None] * fi
    for i in range(fi):
        m_i[i] = [None] * co

    return m_i

# --------------------------------------------------------------------
def crea_vector_img():
    v_i = ['green', 'blue', 'red', 'magenta', 'black', 'white']

    return v_i

# --------------------------------------------------------------------
def crea_tablero_img(f, c, mat_img, mat_num, vec_img):
    for i in range(f):
        for j in range(c):
            mat_img[i][j] = ttk.Label(background=vec_img[mat_num[i][j]])
            mat_img[i][j].place(x=(50*i), y=(50*j), width=50, height=50)


# --------------------------------------------------------------------
def mostrar_mat_num():
    for i in range(10):
        for j in range(10):
            print(mat_num[j][i], end=' ')
        print()

# --------------------------------------------------------------------
def mueve_jugador(event):
    if(event.keysym == 'Up' and mat_num[iv_fil.get()-1][iv_col.get()]!=1):
        iv_fil.set(iv_fil.get()-1)
    elif(event.keysym == 'Down' and mat_num[iv_fil.get()+1][iv_col.get()]!=1):
        iv_fil.set(iv_fil.get()+1)
    elif(event.keysym == 'Left' and mat_num[iv_fil.get()][iv_col.get()-1]!=1):
        iv_col.set(iv_col.get()-1)
    elif(event.keysym == 'Right' and mat_num[iv_fil.get()][iv_col.get()+1]!=1):
        iv_col.set(iv_col.get()+1)
    
    l_jugador.place(x=(50*iv_col.get()), y=(50*iv_fil.get()), width=50, height=50)
# --------------------------------------------------------------------
# Programa Principal
# --------------------------------------------------------------------
app = Tk()
app.geometry("500x500")
app.title("Demo Sokoban")

# declaro dos variable para almacenar la fila y la columna del personaje
iv_fil = IntVar()
iv_col = IntVar()
iv_pas = IntVar()
iv_des = IntVar()
iv_col.set(4)
iv_fil.set(4)
iv_pas.set(0)
iv_des.set(0)

mat_img = crea_matriz_img(10, 10)
mat_num = crea_matriz_num()
vec_img = crea_vector_img()
mostrar_mat_num()

crea_tablero_img(10, 10, mat_img, mat_num, vec_img)

l_jugador = ttk.Label(background=vec_img[5])
l_jugador.place(x=(50*iv_col.get()), y=(50*iv_fil.get()), width=50, height=50)

app.bind("<Key>", mueve_jugador)

app.mainloop()
