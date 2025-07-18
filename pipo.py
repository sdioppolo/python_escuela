from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def click_aceptar():
    if(len(e_ape.get())>0):
        messagebox.showinfo(title='Mensaje', message='Bienvenido\n'+e_ape.get())
        entrada.delete(0,END)


app = Tk() # componente ventana
app.geometry('410x400')
app.title('Agenda de Contactos')

frm_altas = Frame()
l_ape = Label(frm_altas,text='Apellido : ', justify=LEFT)
e_ape = Entry(frm_altas,width=40)
l_nom = Label(frm_altas,text='Nombre   : ', justify=LEFT)
e_nom = Entry(frm_altas,width=40)
l_dom = Label(frm_altas,text='Domicilio: ', justify=LEFT)
e_dom = Entry(frm_altas,width=40)
l_fec = Label(frm_altas,text='Fecha Nac: ', justify=LEFT)
e_fec = Entry(frm_altas,width=40)
l_ema = Label(frm_altas,text='Email    : ', justify=LEFT)
e_ema = Entry(frm_altas,width=40)
aceptar = Button(frm_altas,text='Insertar Contacto', command=click_aceptar)

l_ape.grid(row=0,column=0)
e_ape.grid(row=0,column=1)
l_nom.grid(row=1,column=0)
e_nom.grid(row=1,column=1)
l_dom.grid(row=2,column=0)
e_dom.grid(row=2,column=1)
l_fec.grid(row=3,column=0)
e_fec.grid(row=3,column=1)
l_ema.grid(row=4,column=0)
e_ema.grid(row=4,column=1)

aceptar.grid(row=5,column=0,columnspan=2)
frm_altas.pack()
app.mainloop()
