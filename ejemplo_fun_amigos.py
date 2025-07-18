''' Declaración de Funciones '''
def verifica_amigos(num, a):
    sd = int(0)
    for d in range(1, num):
        if (num % d == 0):
            sd+=d
    if (sd == a):
        return True

    return False

''' Programa Principal '''
a = int(input('A: '))
b = int(input('B: '))

if(verifica_amigos(a, b) and verifica_amigos(b, a)):
    print('Los números son Amigos')
else:
    print('Los números no son amigos')

''' FIN '''
