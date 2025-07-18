from tkinter import *
from tkinter import ttk
import mysql.connector

app = Tk()
app.geometry('800x500')
app.title('Ejemplo Treeview')

db = mysql.connector.connect(host='localhost',
                             user='root',
                             password='12341234',
                             database='ejemplo_qt')

db_crs = db.cursor()

db_crs.execute('SELECT * FROM star_wars_character_dataset;')

h_col = db_crs.column_names

estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure('Treeview.Heading', background='green3')

tbl_per = ttk.Treeview(columns=h_col, show='headings')
for i in range(len(h_col)):
    tbl_per.heading(str(h_col[i]), text=str(h_col[i]))

for reg in db_crs:
    tbl_per.insert('','end', values=reg)

tbl_per.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

db_crs.close()
db.close()

app.mainloop()
