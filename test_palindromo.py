def es_palindromo(cad):
    cc = int(0)
    for i in range(int(len(cad)/2)):
        if(cad[i] == cad[(len(cad)-1)-i]):
            cc += 1
    if(cc == int(len(cad)/2)):
        return True
    return False

pal = input('Ingrese cadena: ')

cl = int(0)
aux = pal

while(not es_palindromo(aux)):
    aux = pal + pal[cl::-1]
    cl += 1

print(aux)
