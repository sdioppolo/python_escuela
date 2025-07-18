def es_palindromo(cad):
    cc = int(0)
    for i in range (int(len(cad)/2)):
        if(cad[i] == cad[(len(cad)-1)-i]):
            cc += 1
    if(cc == int(len(cad)/2)):
        return True
    else:
        return False

def convertir(cad):
    aux = cad + cad[0]
    cl = int(0)
    while(not es_palindoma(aux)):
        cl += 1
        aux = cad + cad[cl::-1]
    return aux


    
