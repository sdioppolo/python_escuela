import random

def crea_matriz(f, c):
    m = [None] * f
    for fi in range(f):
        m[fi] = [None] * c

    return m

def carga_matriz(f, c, ri, rf):
    for fi in range(f):
        for co in range(c):
            n = random.randint(ri, rf)
            while(esta(n)):
                n = random.randint(ri, rf)
            mat[fi][co] = n

def esta(n):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if(n == mat[i][j]):
                return True
    return False

def valida_rango(a, b):
    if((b - a) >= 100):
        return True
    return False

def mostrar_matriz(f, c):
    print()
    print('-'*60)
    for i in range(f):
        for j in range(c):
            print(mat[i][j], end=' ')
        print()
    print('-'*60)
    print()

def ordena_matriz(f, c):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            for a in range(len(mat)):
                for b in range(len(mat[a])):
                    if(mat[i][j] > mat[a][b]):
                        aux = mat[i][j]
                        mat[i][j] = mat[a][b]
                        mat[a][b] = aux
            
        
#----------------------------------------------------------------------
mat = []
opc = -1

while(opc != 0):
    opc = int(input('1) Crear Matriz\n2) Cargar Matriz\n3) Mostrar Matriz\n4) Ordenar Matriz\n0) Salir.\nIngrese Opción: '))

    if(opc == 1):
        mat = crea_matriz(10, 10)
    elif(opc == 2):
        ri = int(input('Rango Inicial: '))
        rf = int(input('Rango Final:   '))
        while(not valida_rango(ri, rf)):
            ri = int(input('Rango Inicial: '))
            rf = int(input('Rango Final:   '))
            
        carga_matriz(10, 10, ri, rf)
    elif(opc == 3):
        mostrar_matriz(10, 10)
    elif(opc == 4):
        ordena_matriz(10, 10)

print('F I N')

