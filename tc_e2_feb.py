def ingresar_texto():
    txt=str(input('Texto a codificar: '))
    real_txt=str('')
    for i in range(len(txt)):
        if(txt[i]!=' '):
            real_txt+=str(txt[i])
    return(real_txt)

def invertir_cadena(cad):
    print[::-1]
    
def crea_matriz(cad):
    largo=len(cad)
    dimensiones=0
    while(dimensiones*dimensiones<largo):
        dimensiones+=1
    mat=[None]*dimensiones
    for i in range(dimensiones):
        mat[i]=[None]*dimensiones

    pos_cad=0
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            if(pos_cad<len(cad)):
                mat[f][c]=cad[pos_cad]
                pos_cad+=1

    print('\n')
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            print(str(mat[f][c]), end=' ')
        print()
    print('\n')
    return(mat)

def decodificar_matriz(mat):
    f=0
    c=0
    cad_aux=str('')
    while(c<len(mat[0])):
        while(f<len(mat)):
            if(str(mat[f][c])!='None'):
                cad_aux+=str(mat[f][c])
            f+=1
        f=0
        c+=1
    return(cad_aux)
           


texto=ingresar_texto()
matriz=crea_matriz(texto)
print(decodificar_matriz(matriz))
cad=invertir_cadena

        
