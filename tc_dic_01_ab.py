import random

def crea_vector(e):
    vec = [None] * e
    return vec

def carga_vector(e):
    for i in range(e):
        vec[i] = random.randint(0,9)

def crea_matriz():
    mat = []
    return mat

def carga_matriz(e):
    v_cont=[0,0,0,0,0,0,0,0,0,0]
    v_aux=[0,0,0,0,0,0,0,0,0,0]

    for r in range(len(vec)):
        v_cont[vec[r]] += 1
        v_aux[vec[r]] += 1

    for f in range(max(v_cont)):
        fila = [' '] * 10
        for i in range(len(v_cont)):
            if(v_cont[i] > 0):
                fila[i] = i
                v_cont[i] -= 1
        mat.append(fila)

    return v_aux

def muestra_resultados():
    print('-'*100)
    
    for i in range(len(vec)):
        print(vec[i], end=' ')

    print()

    print('-'*100)
    for i in range(10):
        print(i, end=' ')
    print()
    print('-'*100)
            
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end=' ')
        print()

    print('-'*100)

    for i in range(len(v_c)):
        print(v_c[i], end = ' ')
    print()

    print('-'*100)


vec = []
mat = []
v_c = []

opc = int(input('1) Crear Vector\n2) Cargar Vector\n3) Crear Matriz\n4) Cargar Matriz\n5) Mostrar Resultados\n0) Salir.\nIngrese Opción: '))

while(opc != 0):
    if(opc == 1):
        vec = crea_vector(50)
    elif(opc == 2):
        carga_vector(50)
    elif(opc == 3):
        mat = crea_matriz()
    elif(opc == 4):
        v_c = carga_matriz(50)
    elif(opc == 5):
        muestra_resultados()

    opc = int(input('1) Crear Vector\n2) Cargar Vector\n3) Crear Matriz\n4) Cargar Matriz\n5) Mostrar Resultados\n0) Salir.\nIngrese Opción: '))

print('F I N')
