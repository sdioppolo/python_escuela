def ordena_matriz_completa():
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            for fc in range(len(mat)):
                for cc in range(len(mat[fc])):
                    if(mat[f][c] > mat[fc][cc]):
                        aux = mat[f][c]
                        mat[f][c] = mat[fc][cc]
                        mat[fc][cc] = aux

def busca_repetidos_matriz():
    num = mat[0][0]
    rep = int(1)
    i = int(0)
    for f in range(len(mat)):
        if(f==0):
            i = 1
        else:
            i = 0
        for c in range(i, len(mat[f])):
            if(num == mat[f][c]):
                rep += 1
            else:
                v_rep.append(num)
                v_rep.append(rep)
                num = mat[f][c]
                rep = 1
    v_rep.append(num)
    v_rep.append(rep)
    
def muestra_matriz():
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end = ' ')
        print()

def muestra_repetidos():
    for i in range(0, len(v_rep), 2):
        print(v_rep[i], '--->', v_rep[i+1])


'''--------------------------------------------------------------------'''
v_rep = []
mat = [[10, 23, 45, 10, 34],
       [34, 67, 76, 10, 23],
       [11, 34, 23, 45, 98],
       [23, 90, 78, 56, 33],
       [45, 57, 58, 30, 12]]

print('-' * 50)
muestra_matriz()
ordena_matriz_completa()
print('-' * 50)
muestra_matriz()
busca_repetidos_matriz()
print('-' * 50)
muestra_repetidos()

print('\n\nF I N\n\n')
