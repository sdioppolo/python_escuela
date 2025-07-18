import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def genera_notas():
    random.seed(None)
    for f in range(10):
        for c in range(20):
            notas[f][c] = random.randint(1,9)

def mostrar_notas():
    fila='{0:25}'.format('')
    for i in range(20):
        fila += '{0:8}'.format(alumnos[i])
    out.insert(END, fila + '\n')
    out.insert(END, '-'*190 + '\n')
    
    for f in range(10):
        fila = '{0:24}|  '.format(materias[f])
        for c in range(20):
            fila += '{0:8}'.format(str(notas[f][c]))
        out.insert(END, fila + '\n')
    out.insert(END, '-'*190 + '\n')
    
def calcula_resultados():
    v_may=[None] * 10
    v_men=[None] * 10
    v_pro=[0] * 10
    for i in range(10):
        v_may[i]=notas[i][0]
        for j in range(1, 20):
            if(v_may[i] < notas[i][j]):
                v_may[i] = notas[i][j]
                
    for i in range(10):
        v_men[i]=notas[i][0]
        for j in range(1, 20):
            if(v_men[i] > notas[i][j]):
                v_men[i] = notas[i][j]

    for i in range(10):
        for j in range(20):
            v_pro[i]+=notas[i][j]
        v_pro[i] = int(v_pro[i] / 20)

    for f in range(10):
        fila = '{0:25}{1:8}{2:8}{3:8}'.format(materias[f], v_may[f], v_men[f], v_pro[f])
        out.insert(END, fila + '\n')
    out.insert(END, '-'*190 + '\n')


def genera_graficos():
    v_por = [0] * 10
    m_lbl = [None] * 10
    for i in range(10):
        m_lbl[i] = [None] * 20
    
    for i in range(10):
        for j in range(20):
            v_por[i] += notas[i][j]
        v_por[i] = int(v_por[i] / 20)

    for i in range(10):
        for j in range(v_por[i]):
            m_lbl[i][j]=Label(fgr, text='', background=colores[i])
            m_lbl[i][j].place(x=(20*j)+10, y=(20*i)+10, height=20, width=20)

    app.update()       

'''--------------------------------------------------------------------------'''
alumnos = ['1001','1002','1003','1004','1005','1006','1007','1008','1009','1010','1011','1012','1013','1014','1015','1016','1017','1018','1019','1020']
materias = ['Matemática',
            'Lengua y Literatura',
            'Geografía',
            'Historia',
            'Educación Física',
            'Taller',
            'Química',
            'Física',
            'Educación Ciudadana',
            'Dibujo Técnico']
colores = ['red',
           'blue',
           'green',
           'yellow',
           'white',
           'cyan',
           'magenta',
           'light blue',
           'gray',
           'dark gray']
notas = [None] * 10
for i in range(10):
    notas[i] = [None] * 20

app = Tk()
app.geometry('1550x900')
app.title('Evaluación PIA C1 Grupo A')

fbt = Frame(app, borderwidth=1, relief=GROOVE, bg='dark gray')
fgr = Frame(app, borderwidth=1, relief=GROOVE, bg='dark gray')

bgn = Button(fbt, text='Genera Notas',command=genera_notas)
bmn = Button(fbt, text='Mostrar Notas', command=mostrar_notas)
bcr = Button(fbt, text='Calcula Resultados',command=calcula_resultados)
bgg = Button(fbt, text='Genera Gráficos',command=genera_graficos)
out = Text(fbt, width=190, height=28)

bgn.grid(row=0, column=0, columnspan=3)
bmn.grid(row=0, column=4, columnspan=3)
bcr.grid(row=0, column=7, columnspan=3)
bgg.grid(row=0, column=10, columnspan=3)
out.grid(row=1, column=0, columnspan=13)

fbt.pack(side=TOP, expand=True, fill=Y, pady=5, padx=5)
fgr.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

app.mainloop()
