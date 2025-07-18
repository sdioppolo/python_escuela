import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def genera_valores():
    for i in range(len(v_valores)):
        v_valores[i] = random.randint(0,9)
    muestra_colores()

def muestra_colores():
    for i in range(45):
        v_label[i].configure(background=v_colores[v_valores[i]],
                             text=str(v_valores[i]))
    app.update()

def ordenar_vector():
    for i in range(len(v_valores)-1):
        for j in range(i+1, len(v_valores)):
            if(v_valores[i] > v_valores[j]):
                aux = v_valores[i]
                v_valores[i] = v_valores[j]
                v_valores[j] = aux

    nuestra_ordenado()

def nuestra_ordenado():
    for i in range(45):
        v_label_ord.append(Label(text=str(v_valores[i]),
                                 activebackground=v_colores[v_valores[i]],
                                 background=v_colores[v_valores[i]],
                                 borderwidth=1,
                                 relief=GROOVE))
        v_label_ord[i].place(x=(40 * i)+10,
                             y = 40 + 90,
                             height = 40,
                             width = 40)

def muestra_frecuencia():
    for i in range(45):
        v_label_frq.append(Label(text=str(v_valores[i]),
                                 activebackground=v_colores[v_valores[i]],
                                 background=v_colores[v_valores[i]],
                                 borderwidth=1,
                                 relief=GROOVE))
        v_label_frq[i].place(x=(40 * i)+10,
                             y = 40 + 180,
                             height = 40,
                             width = 40)
    
def ordenar_freq():
    freq = []
    x = int(0)
    cr = int(1)
    
    freq.append(v_valores[0])
    for i in range(1,45):
        if (v_valores[i] == freq[x]):
            cr += 1
        else:
            freq.append(cr)
            freq.append(v_valores[i])
            cr = 1
            x += 2
    freq.append(cr)
    print(freq)

    for i in range(0,len(freq)-2, 2):
        for j in range(i+2, len(freq), 2):
            if(freq[i+1] < freq[j+1]):
                aux_n = freq[i]
                aux_f = freq[i+1]
                freq[i] = freq[j]
                freq[i+1] = freq[j+1]
                freq[j] = aux_n
                freq[j+1] = aux_f
    print(freq)

    x = int(0)
    for i in range(0,len(freq),2):
        for j in range(freq[i+1]):
            v_valores[x] = freq[i]
            x += 1

    print(v_valores)

    muestra_frecuencia()


v_colores = ['red',
             'blue',
             'green',
             'yellow',
             'gray',
             'orange',
             'cyan',
             'light blue',
             'violet',
             'magenta']

v_valores = [None] * 45

v_label = []
v_label_ord = []
v_label_frq = []
v_freq = []

app = Tk()
app.geometry('1820x400')
app.title('Vectores por Frecuencia')

generar = Button(text='Generar Valores', command=genera_valores)
generar.place(x=10, y=5, height=30, width=1800)
for i in range(45):
    v_label.append(Label(text='_',
                         activebackground='light gray',
                         background='light gray',
                         borderwidth=1,
                         relief=GROOVE))
    v_label[i].place(x=(40 * i)+10, y = 40, height = 40, width = 40)

ordenar = Button(text='Ordenar Vector', command=ordenar_vector)
ordenar.place(x=10, y=90, height=30, width=1800)

frecuencia = Button(text='Ordenar por Frecuencia', command=ordenar_freq)
frecuencia.place(x=10, y=180, height=30, width=1800)

app.mainloop()
