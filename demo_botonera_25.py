import time
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial

def click_comenzar():
    v_jugadas.append(random.randint(0,3))
    for i in range(len(v_jugadas)):
        v_botones[v_jugadas[i]].configure(background=v_colores[v_jugadas[i]])
        time.sleep(0.30)
        app.update()
        
        v_botones[v_jugadas[i]].configure(background=v_colores[4])
        time.sleep(0.30)
        app.update()


def click_botonera(i):
    print('hola'+' '+str(i))
    v_botones[i].configure(text=v_colores[i],background=v_colores[i])
    time.sleep(0.30)
    app.update()

    v_botones[i].configure(text=str(i),background=v_colores[4])
    time.sleep(0.30)
    app.update()

    v_jugador.append(i)
    v_cont_click[0]+=1


v_botones = []
v_colores = ['red','yellow','blue','green','lightgray']
v_jugadas = []
v_jugador = []
v_cont_click = [0]

app = Tk()
app.title('Demo Botonera')
app.geometry('340x130')

comienzo = Button(text='Comenzar', command=click_comenzar)
comienzo.place(x=10, y=10, height=30, width=320)

for i in range(4):
    v_botones.append(Button(text=str(i),
                            command=partial(click_botonera,i),
                            activebackground=v_colores[i],
                            background=v_colores[4]))
    v_botones[i].place(x=(80*i)+10, y=42, height=80, width=80)


app.mainloop()
