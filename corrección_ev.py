from tkinter import *
from tkinter import messagebox
import tkinter as tk

def calc_resu():
    prom_gas1 = []
    prom_gas2 = []
    for i in range(5):
        nota1 = int(ent_gas1[i][0].get())
        nota2 = int(ent_gas1[i][0].get())
        nota3 = int(ent_gas1[i][0].get())
        prom1 = (nota1 + nota2 + nota3)/3
        prom_gas1.append(prom1)

        nota4 = int(ent_gas2[i][0].get())
        nota5 = int(ent_gas2[i][0].get())
        nota6 = int(ent_gas2[i][0].get())
        prom2 = (nota4 + nota5 + nota6)/3
        prom_gas2.append(prom2)

    resultado= ""
    for i in range(5):
        resultado += f"persona {i+1}:/n"
        resultado += f"gaseosa 1: promedio {prom_gas1[i]:.2f}-"
        if (prom_gas1 > 6):
            resultado += "aprobada\n"
        else:
            resultado += "no aprobada\n"
        resultado += f"gaseosa 2: promedio {prom_gas1[i]:.2f}-"
        if (prom_gas1 > 6):
            resultado += "aprobada\n"
        else:
            resultado += "no aprobada\n"

        mejor_g1= max(prom_gas1)
        mejor_g2= max(prom_gas2)

        resultado += f"mejor promedio gaseosa 1 {mejor_g1:.2f}\n"
        resultado += f"mejor promedio gaseosa 2 {mejor_g2:.2f}\n"

        messagebox.showinfo("resultados", resultado)

ventana = tk.Tk()
ventana.title("encuesta de gaseosa")

etiquetas = ["presentacion", "sabor", "precio"]

ent_gas1 = []
ent_gas2 = []

for i in range(5):
    tk.Label(ventana, text=f"persona {i+1}").grid(row=i*2, column=0, pady=5)

    fila1= []
    fila2= []

    for e in range(3):
        tk.Label(ventana, text=f"gaseosa 1 - {etiquetas[e]}").grid(row=i*2,column=e+1)
        entrada1 = tk.Entry(ventana, width=5)
        entrada1.grid(row=i*2+1, column=e+1)
        fila1.append(entrada1)

        tk.Label(ventana, text=f"gaseosa 2 - {etiquetas[e]}").grid(row=i*2,column=e+5)
        entrada2 = tk.Entry(ventana, width=5)
        entrada2.grid(row=i*2+1, column=e+5)
        fila2.append(entrada2)

        ent_gas1.append(fila1)
        ent_gas2.append(fila2)

tk.Button(venta, tex="calcular resultados",command=cal_resu).grid(row=10, column=0,columnspan=10, pady=10)

ventana.mainloop()

        


        



        
