from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

def conectar():
    try:
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12341234',
            database='ejemplo_qt'
        )
        return cnx
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error al conectar a la base de datos: {err}')
        return None

def cerrar(cnx, crs):
    if crs:
        crs.close()
    if cnx:
        cnx.close()

def boton1():
    cnx = conectar()

    crs = cnx.cursor()
    crs.execute('SELECT * FROM star_wars_character_dataset;')

    rst = crs.fetchall()
    for reg in rst:
        trv.insert('', 'end', values=reg)
        
    cerrar(cnx, crs)

def boton2():
    cnx = conectar()

    crs = cnx.cursor()
    crs.execute('SELECT * FROM star_wars_character_dataset WHERE eye_color = "orange";')

    rst = crs.fetchall()
    for reg in rst:
        trv.insert('', 'end', values=reg)
        
    cerrar(cnx, crs)

def boton3():
    cnx = conectar()

    crs = cnx.cursor()
    crs.execute('SELECT * FROM star_wars_character_dataset WHERE species = "droid";')

    rst = crs.fetchall()
    for reg in rst:
        trv.insert('', 'end', values=reg)
        
    cerrar(cnx, crs)

def boton4():
    cnx = conectar()

    crs = cnx.cursor()
    crs.execute('SELECT * FROM star_wars_character_dataset WHERE films = "A New Hope";')

    rst = crs.fetchall()
    for reg in rst:
        trv.insert('', 'end', values=reg)
        
    cerrar(cnx, crs)

def boton5():
    cnx = conectar()

    crs = cnx.cursor()
    crs.execute('SELECT * FROM star_wars_character_dataset WHERE homeworld = "Naboo" AND gender = "feminine";')

    rst = crs.fetchall()
    for reg in rst:
        trv.insert('', 'end', values=reg)
        
    cerrar(cnx, crs)

def boton6():
    cnx = conectar()

    crs = cnx.cursor()
    crs.execute('SELECT * FROM star_wars_character_dataset WHERE sex = "hermaphroditic";')

    rst = crs.fetchall()
    for reg in rst:
        trv.insert('', 'end', values=reg)
        
    cerrar(cnx, crs)

#el resto

app = Tk()
app.geometry('800x600')
app.title('bdd_ev01_c2')

btn_1 = Button(app, text='Mostrar Personajes', command=boton1)
btn_2 = Button(app, text='Personajes con Ojos Naranja', command=boton2)
btn_3 = Button(app, text='Mostrar Personajes Droides', command=boton3)
btn_4 = Button(app, text='Personajes de A New Hope', command=boton4)
btn_5 = Button(app, text='Personajes Mujer de Naboo', command=boton5)
btn_6 = Button(app, text='Personajes Hermafroditas', command=boton6)

trv = ttk.Treeview(app, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), show='headings', height='7')
trv.heading(1, text='name')
trv.heading(2, text='height')
trv.heading(3, text='mass')
trv.heading(4, text='hair color')
trv.heading(5, text='skin color')
trv.heading(6, text='birth year')
trv.heading(7, text='sex')
trv.heading(8, text='gender')
trv.heading(9, text='homeworld')
trv.heading(10, text='sex')
trv.heading(11, text='species')
trv.heading(12, text='films')
trv.heading(13, text='vehicles')
trv.heading(14, text='starships')


btn_1.grid(column=0, row=0)
btn_2.grid(column=1, row=0)
btn_3.grid(column=0, row=1)
btn_4.grid(column=1, row=1)
btn_5.grid(column=0, row=2)
btn_6.grid(column=1, row=2)

trv.grid(column=0, row=3, columnspan=3)

app.mainloop()

"""
1)SELECT * FROM star_wars_character_dataset;

2)SELECT * FROM star_wars_character_dataset WHERE eye_color = "orange";

3)SELECT * FROM star_wars_character_dataset WHERE species = "droid";

4)SELECT * FROM star_wars_character_dataset WHERE films = "A New Hope";

5)SELECT * FROM star_wars_character_dataset WHERE homeworld = "Naboo" AND gender = "feminine";

6)SELECT * FROM star_wars_character_dataset WHERE sex = "hermaphroditic";
"""
