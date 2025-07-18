def eliminar_espacios(texto):
    texto_sin_espacios=""
    for char in texto:
        if char !="":
            texto_sin_espacios+=char
    return texto_sin_espacios

def calcular_matriz(texto):
    n = 0
    while(n*n<len(texto)):
        n+=1
    return n

def llenar_matriz(texto,n):
    matriz=[]

    i=0
    for j in range(n):
        fila_act=[]
        for col in range(n):
            if(i<len(texto)):
                fila_act.append(texto[i])
                i += 1 
            else:
                fila_act.append("")
        print(matriz)                       
        matriz.append(fila_act)
                                
    return matriz

def texto_matriz(matriz,n):
    texto_codificado=""
    for i in range(n):
        for j in range(n):
            texto_codificado += matriz [j][i]

    return texto_codificado

def codificar_texto():
    texto_sin_espacios= eliminar_espacios(texto_entrada)
 
    n=calcular_matriz(texto_sin_espacios)

    matriz=llenar_matriz(texto_sin_espacios,n)

    texto_codificado=texto_matriz(matriz,n)
    
    return texto_codificado

texto_entrada=input("introduce el texto a codificar:")

texto_codificado=codificar_texto()
print("\nTexto codificado:",texto_codificado)
