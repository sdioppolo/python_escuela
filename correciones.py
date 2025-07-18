import random

def crear_matriz(filas=10, columnas=10):
    return[[0 for _ in range(columnas)] for _ in range(filas)]


def cargar_matriz(matriz, ran_min, ran_max):
    total_elementos = len(matriz) * len(matriz[0])
    if ran_max - ran_min + 1 < total_elementos:
        
        return

    valores_disponibles = list(range(ran_min, ran_max + 1))
    random.shuffle(valores_disponibles)

    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = valores_disponibles[contador]
            contador += 1

    
                    


def mostrar_matriz(matriz):
    for fila in matriz:
            print(" ".join(map(str, fila)))

def ordenar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    valores = []
    val=[]
    for i in range(filas):
        for j in range(columnas):
            valores.append(matriz[i][j])


    for i in range(len(valores)):
                   for j in range( i + 1, len(val)):
                       if valores[i] < valores[j]:
                           aux = valores[i]
                           valores[i] = valores[j]
                           valores[j] = aux

    contador = 0
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = valores[contador]
            contador += 1
                       


def menu():
    matriz= crear_matriz()
    while True:
        print("\nMenu:")
        print("1) crear matriz")
        print("2) cargar matriz")
        print("3) mostrar matriz")
        print("4) ordenar matriz de mayor a menor")
        print("0) sali")

        opc = input("ingresar opcion: ")


        if opc == "1":
            matriz = crear_matriz()
            print("matriz creada")

        elif opc == "2":
            ran_min = int(input("ingresar valor minimo"))
            ran_max = int(input("ingresar valor maximo"))
            cargar_matriz(matriz, ran_min, ran_max)
            print("matriz cargada")

        elif opc == "3":
            print("matriz: ")
            mostrar_matriz(matriz)

        elif opc =="4":
            ordenar_matriz(matriz)
            print("matriz ordenada de mayor a menor")

        elif opc == "0":
            print("saliendo...")
            return

menu()
            
                        
