from tkinter import *
from tkinter import ttk
from tkinter import messagebox, PhotoImage

app = Tk()
app.geometry('500x500')
app.title('Imágenes en Tkinter')

v_img = []
v_img.append(PhotoImage(file='x_wing.png'))
v_img.append(PhotoImage(file='tie_fighter.png'))

m_num = [[0,1,0,1],[1,1,0,1],[0,1,0,0],[1,0,0,1]]

m_bot = [None] * 4
for i in range(4):
    m_bot[i] = [None] * 4
    
for f in range(len(m_num)):
    for c in range(len(m_num[f])):
        m_bot[f][c] = Button(image=v_img[m_num[f][c]])
        m_bot[f][c].place(x=(100 * f)+80, y=(100 * c)+80, width=80, height=80)


app.mainloop()
