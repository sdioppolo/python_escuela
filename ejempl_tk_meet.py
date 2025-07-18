from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def click_aceptar():
    if(len(entrada.get()) > 0):
        cartel.configure(text='Bienvenido '+entrada.get())
        lista.insert(END, entrada.get() + '\n')
        lista_nombres.append(entrada.get())
        cont_nombres[0]+=1
        entrada.delete(0,END)
        print(lista_nombres)
        print(cont_nombres)
    else:
        messagebox.showerror(title='ERROR!!!', message='Debe ingrresar su nombre.')


#-------------------------------------------------------------Programa principal
lista_nombres = []
cont_nombres =[0]

app = Tk()
app.geometry('400x400') # tamaño de la ventana
app.title('Mi Primera Ventana')

# instanciar componentes básicos
cartel = Label(text='Hola Mundo Tkinter!!!',
               borderwidth=1,
               relief=GROOVE,
               background='blue',
               foreground='white')

entrada = Entry(width=30)

aceptar = Button(text='Aceptar', command=click_aceptar)

lista = Text(height=10, width=30)

# ubicar el componente
cartel.pack()
entrada.pack()
aceptar.pack()
lista.pack()

entrada.focus()

app.mainloop()
