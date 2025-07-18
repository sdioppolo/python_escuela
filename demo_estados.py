from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def click_uno():
    print('B1')
    b2.configure(state='normal')
    b1.configure(state='disable')
    app.update()

def click_dos():
    print('B2')
    b3.configure(state='normal')
    b2.configure(state='disable')
    app.update()

def click_tres():
    print('B3')
    b1.configure(state='normal')
    b3.configure(state='disable')
    app.update()


app = Tk()
app.geometry('300x300')
app.title('Demo estados y enter')

b1 = Button(text='Uno', command=click_uno)
b2 = Button(text='Dos', command=click_dos, state='disable')
b3 = Button(text='Tres', command=click_tres, state='disable')
e1 = Entry(width=40)

b1.pack()
b2.pack()
b3.pack()
e1.pack()

app.bind 
app.mainloop()
