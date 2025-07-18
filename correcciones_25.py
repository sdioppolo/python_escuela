import time
import random
from tkinter import *
from tkinter import messagebox
from functools import partial

v_botones = []
v_colores = ['red','yellow','blue','green']
v1_colores = ['IndianRed1','light yellow','light blue','light green']
v_sec = ['0','1', '2', '3']
sec_gen=[""]
sec=[""]
llamadas=[0]

def click_botonera(i):
    sec[0] += v_sec[i]
    
    v_botones[i].configure(text=v_colores[i])
    v_botones[i].configure(background=v_colores[i],activebackground=v_colores[i])
    co.configure(text=f'secuencia: {sec[0]}')
    
    app.update()
    time.sleep(0.30)
    
    v_botones[i].configure(text='',background=v1_colores[i], activebackground=v1_colores[i])

def generar_random():
    return random.randint(0,3)

def desactivar():
    for i in range(4):
        v_botones[i].configure(state=DISABLED)

def activar():
    for i in range(4):
        v_botones[i].configure(state=NORMAL)

def verificar():
    co.configure(text=f'secuencia: ')
    app.update()
    if(llamadas[0] == 0):
        desactivar()
        app.update()
        time.sleep(1.0)
        num = generar_random()
        sec_gen[0] += str(num)

        v_botones[num].configure(text=v_colores[num])
        v_botones[num].configure(background=v_colores[num],activebackground=v_colores[num])
        app.update()
        time.sleep(0.30)
    
        v_botones[num].configure(text='',background=v1_colores[num], activebackground=v1_colores[num])
        activar()
        llamadas[0] += 1

    else:
        if(sec[0] == sec_gen[0]):
            if(len(sec[0]) == 30):
                messagebox.showinfo("Ganaste!!", "LETS GO!! Presiona el boton 'verificar intento' para jugar otra vez.")
                sec_gen[0] = ""
                sec[0] = ""
                co.configure(text=f'secuencia: {sec[0]}')
                llamadas[0] = 0
                app.update()
            else:
                messagebox.showinfo("Bien!!", "Genial, sigue jugando!!!")
                time.sleep(1.0)

                desactivar()
                app.update()
                
                for i in range(len(sec_gen[0])):
                    num = int(sec_gen[0][i])
                    v_botones[num].configure(text=v_colores[num])
                    v_botones[num].configure(background=v_colores[num],activebackground=v_colores[num])
                    app.update()
                    time.sleep(0.30)
                    v_botones[num].configure(text='',background=v1_colores[num], activebackground=v1_colores[num])
                    app.update()
                    time.sleep(0.30)

                num = generar_random()
                sec_gen[0] += str(num)
                v_botones[num].configure(text=v_colores[num])
                v_botones[num].configure(background=v_colores[num],activebackground=v_colores[num])
                app.update()
                time.sleep(0.30)
                v_botones[num].configure(text='',background=v1_colores[num], activebackground=v1_colores[num])
                activar()
                llamadas[0] += 1
                sec[0] = ""

        else:
            messagebox.showerror("MAL!", "Perdiste. Presiona el boton 'verificar intento' para jugar otra vez")
            sec_gen[0] = ""
            sec[0] = ""
            co.configure(text=f'secuencia: {sec[0]}')
            llamadas[0] = 0
            app.update()

app = Tk()
app.title('Demo Botonera')
app.geometry('370x250')

co = Label(text='secuencia: ',background="LightBlue",height=3)
co.pack(fill=BOTH,side=TOP)

for i in range(4):
    btn = Button(app, command=partial(click_botonera,i))
    btn.configure(background=v1_colores[i])
    btn.configure(activebackground=v1_colores[i])
    btn.place(x=(80*i)+10*(i+1),y=70, height=80, width=80)
    v_botones.append(btn)

ver = Button(app,text="Verificar intento", command=verificar, padx=10)
ver.pack(side=BOTTOM,fill=X)

messagebox.showinfo("Bienvenido", "Presiona 'verificar intento' para comenzar a jugar")

app.mainloop()
