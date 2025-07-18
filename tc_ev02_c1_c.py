from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def nuevo_producto():
    pass

def menor_precio():
    pass

# ----------------------------------------------------------------------------
productos = []
contadores = [0,0]

app = Tk()
app.geometry('340x600')

l_prod = Label(text='Producto: ', width=20)
e_prod = Entry(width=20)
l_prov = Label(text='Proveedor: ', width=20)
e_prov = Entry(width=20)
l_prec = Label(text='Precio: ', width=20)
e_prec = Entry(width=20)
l_desc = Label(text='Descuento: ', width=20)
e_desc = Entry(width=20)
b_newp = Button(text='Nuevo Producto', command=nuevo_producto)
b_mpre = Button(text='Menor Precio', command=menor_precio)
t_salida = Text(width=40, height=25)

l_prod.grid(row=0, column=0)
e_prod.grid(row=0, column=1)
l_prov.grid(row=1, column=0)
e_prov.grid(row=1, column=1)
l_prec.grid(row=2, column=0)
e_prec.grid(row=2, column=1)
l_desc.grid(row=3, column=0)
e_desc.grid(row=3, column=1)
b_newp.grid(row=4, column=0)
b_mpre.grid(row=4, column=1)
t_salida.grid(row=5, column=0, columnspan=4)

app.mainloop()
