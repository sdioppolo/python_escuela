from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def click_alta():
    pass

def click_baja():
    pass

def click_modi():
    pass

def click_list():
    pass

def menu():
    frm_menu = Frame(app, bg='dark gray', relief=FLAT)
    menu_alta = Button(frm_menu, text='Alta de Contactos', command=click_alta)
    menu_baja = Button(frm_menu, text='Baja de Contactos', command=click_baja)
    menu_modi = Button(frm_menu, text='Modificación de Contactos', command=click_modi)
    menu_list = Button(frm_menu, text='Listado de Contactos', command=click_list)
    menu_alta.grid(row=0, column=0, padx=5)
    menu_baja.grid(row=0, column=1, padx=5)
    menu_modi.grid(row=0, column=2, padx=5)
    menu_list.grid(row=0, column=3, padx=5)
    frm_menu.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)

def centro():
    frm_centro = Frame(app)
    resultados = Text(frm_centro, width=60, height=30)
    resultados.pack()
    frm_centro.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)


def tareas():
    pass

    
app = Tk()
app.geometry('600x800')
app.title('Agenda de Contactos')

menu()
centro()
tareas()

app.mainloop()
