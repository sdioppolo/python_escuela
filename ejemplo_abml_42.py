from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def limpiar_entrys():
    e_id.delete(0,END)
    e_ape.delete(0,END)
    e_nom.delete(0,END)
    e_dom.delete(0,END)
    e_ema.delete(0,END)
    e_fdc.delete(0,END)
    e_tel.delete(0,END)
    
def clk_lista():
    db = mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='12341234',
                                 database='bdd_mysql_py')
    cs = db.cursor()
    cs.execute('select * from contactos')

    salida.insert(END,60*'-'+'\n')
    salida.insert(END,' Contactos\n')
    salida.insert(END,60*'-'+'\n')

    for res in cs:
        salida.insert(END, str(res) + '\n')

    salida.insert(END,60*'-'+'\n')

    cs.close()
    db.close()

def clk_altas():
    db = mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='12341234',
                                 database='bdd_mysql_py')
    cs = db.cursor()

    st = 'insert into contactos (apellido, nombre, domicilio, email, fecha_cumple, telefono) values (%s,%s,%s,%s,%s,%s)'
    
    cs.execute(st,(e_ape.get(),e_nom.get(),e_dom.get(),e_ema.get(),e_fdc.get(),e_tel.get()))
    db.commit()
    cs.close()
    db.close()

    limpiar_entrys()

def clk_bajas():
    db = mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='12341234',
                                 database='bdd_mysql_py')
    cs = db.cursor()
    st = 'delete from contactos where idcontactos = %s'
    val = (e_id.get(),)
    cs.execute(st, val)
    db.commit()
    cs.close()
    db.close()
    limpiar_entrys()

def clk_modif():
    db = mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='12341234',
                                 database='bdd_mysql_py')
    cs = db.cursor()
    st = 'update contactos set apellido=%s, nombre=%s, domicilio=%s, email=%s, fecha_cumple=%s, telefono=%s where idcontactos = %s'
    val = (e_ape.get(), e_nom.get(), e_dom.get(), e_ema.get(), e_fdc.get(), e_tel.get(), e_id.get())
    cs.execute(st, val)
    db.commit()
    cs.close()
    db.close()
    limpiar_entrys()

def clk_buscar():
    if(len(e_id.get())!=0):
        db = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='12341234',
                                     database='bdd_mysql_py')
        cs = db.cursor()
        st = 'select * from contactos where idcontactos = %s'
        val = (e_id.get(),)
        cs.execute(st, val)

        c_reg = cs.rowcount
        if(c_reg >= 0):
            for result in cs:
                e_ape.insert(0, str(result[1]))
                e_nom.insert(0, str(result[2]))
                e_dom.insert(0, str(result[3]))
                e_ema.insert(0, str(result[4]))
                e_fdc.insert(0, str(result[5]))
                e_tel.insert(0, str(result[6]))
        
        cs.close()
        db.close()


app = Tk()
app.geometry('600x800')
app.title('ABML Simple')

frm_menu = Frame(app)
altas = Button(frm_menu,text='Altas', command=clk_altas,width=15)
bajas = Button(frm_menu,text='Bajas', command=clk_bajas,width=15)
modif = Button(frm_menu,text='Modificaciones', command=clk_modif,width=15)
lista = Button(frm_menu,text='Listado', command=clk_lista,width=15)

altas.grid(row=0, column=0)
bajas.grid(row=0, column=1)
modif.grid(row=0, column=2)
lista.grid(row=0, column=3)

frm_buscar = Frame(app, borderwidth=1, relief=GROOVE, bg='dark gray')
l_id = Label(frm_buscar, text='Ingrese ID a buscar: ')
e_id = Entry(frm_buscar, width=20)
b_id = Button(frm_buscar, text='Buscar', command=clk_buscar)

l_id.grid(row=0, column=0)
e_id.grid(row=0, column=1)
b_id.grid(row=0, column=2)

frm_alta = Frame(app, borderwidth=1, relief=GROOVE)
l_ape = Label(frm_alta, text='Apellido:')
e_ape = Entry(frm_alta, width=30)
l_nom = Label(frm_alta, text='Nombre:')
e_nom = Entry(frm_alta, width=30)
l_dom = Label(frm_alta, text='Domicilio:')
e_dom = Entry(frm_alta, width=30)
l_ema = Label(frm_alta, text='Email:')
e_ema = Entry(frm_alta, width=30)
l_fdc = Label(frm_alta, text='Fecha Cumple:')
e_fdc = Entry(frm_alta, width=30)
l_tel = Label(frm_alta, text='Telefono:')
e_tel = Entry(frm_alta, width=30)

l_ape.grid(row=0, column=0)
e_ape.grid(row=0, column=1)
l_nom.grid(row=1, column=0)
e_nom.grid(row=1, column=1)
l_dom.grid(row=2, column=0)
e_dom.grid(row=2, column=1)
l_ema.grid(row=3, column=0)
e_ema.grid(row=3, column=1)
l_fdc.grid(row=4, column=0)
e_fdc.grid(row=4, column=1)
l_tel.grid(row=5, column=0)
e_tel.grid(row=5, column=1)


frm_cuerpo = Frame(app)
salida = Text(frm_cuerpo, height=20, width=70)
salida.pack(padx=5, pady=5, expand=True, fill=BOTH)

frm_menu.pack(side=TOP, expand=True, fill=X)
frm_buscar.pack(side=TOP, expand=True, fill=X)
frm_alta.pack(side=TOP, expand=True, fill=X)
frm_cuerpo.pack(side=BOTTOM, expand=True, fill=BOTH)


app.mainloop()
