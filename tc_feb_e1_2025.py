import math

def saca_espacios(texto):
    t_aux = ''
    for i in range(len(texto)):
        if(texto[i] != ' '):
            t_aux += texto[i]
    return t_aux

def crea_matriz(t):
    d = int(1) + int(math.sqrt(len(t)-1))
    mat = [None] * d
    for f in range(d):
        mat[f] = [None] * d
    return mat

def carga_matriz(m, t):
    p = int(0)
    for f in range(len(m)):
        for c in range(len(m[f])):
            if(p < len(t)):
                m[f][c] = t[p]
                p+=1
            else:
                m[f][c] = ''

def mostrar_matriz(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            print(m[f][c], end=' ')
        print()

def cifrar_texto(m):
    txt_cfr = ''
    for f in range(len(m)):
        for c in range(len(m[f])):
            txt_cfr += m[c][f]
    return txt_cfr

#-------------------------------------------------------------
texto = input('Ingrese un texto: ')
print()
txt_se = saca_espacios(texto)

txt_mat = crea_matriz(txt_se)

carga_matriz(txt_mat, txt_se)

mostrar_matriz(txt_mat)
print()
print('El texto cifrado es: ', cifrar_texto(txt_mat))
print()
print('El texto final es: ', cifrar_texto(txt_mat)[::-1])
print('\n\nFIN...')


