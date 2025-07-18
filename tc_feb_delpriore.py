import math

def texto(text):
    aux=''
    for i in range(len(text)):
        if(text[i]!=" "):
            aux+=text[i]
    return aux

def raiz():
    long=len(text)
    
    for i in range(long, long+1):
        while(int(math.sqrt(long))):
                r=i
def crear_matriz(mat):
    mat=[None]*r
    for i in range(r):
        mat[i]=[None]*r
    return mat

def cargar_matriz(r, mat, text):
    i=0
    for f in range(r):
        for c in range(r):
            if(i<len(mat)):
                mat=text[i]
                if(len(mat[f])==r):
                    f+=1
                    c=0
    
                    

def mostrar_matriz():
    for f in range(r):
        for c in range(r):
            print(mat[f][c], end=" ")
        print()

def columnas():
    for i in range(len(mat[0])):
        print(mat[i], end=" ")
    print()

def al_reves():
    mat[::-1]



#--------------------------------------------------------------------------------------------------------

text=input("Ingresar texto")
aux=" "
long=len(text)
mat=[]
i=0
text=texto(text)
print(text)
raiz()
mat=crear_matriz(mat)
cargar_matriz(r, mat, text)
mostrar_matriz()
columnas()
al_reves()
mostrar_matriz()
        
