def muestra_ahorcado_0():
    print(' _____')
    print('|     |')
    print('|')        
    print('|')      
    print('|')        
    print('|')     
    print('|_____________ ')

def muestra_ahorcado_1():
    print(' _____')
    print('|     |')
    print('|     0')        
    print('|')      
    print('|')        
    print('|')     
    print('|_____________ ')


def muestra_ahorcado_2():
    print(' _____')
    print('|     |')
    print('|     0')        
    print('|     |')      
    print('|')        
    print('|')     
    print('|_____________ ')

def muestra_ahorcado_3():
    print(' _____')
    print('|     |')
    print('|     0')        
    print('|    /|')      
    print('|')        
    print('|')     
    print('|_____________ ')

def muestra_ahorcado_4():
    print(' _____')
    print('|     |')
    print('|     0')        
    print('|    /|\\')      
    print('|')        
    print('|')     
    print('|_____________ ')

def muestra_ahorcado_5():
    print(' _____')
    print('|     |')
    print('|     0')        
    print('|    /|\\')      
    print('|     |')        
    print('|')     
    print('|_____________ ')

def muestra_ahorcado_6():
    print(' _____')
    print('|     |')
    print('|     0')        
    print('|    /|\\')      
    print('|     |')        
    print('|    /')     
    print('|_____________ ')

def muestra_ahorcado_7():
    print(' _____')
    print('|     |')
    print('|     0')        
    print('|    /|\\')      
    print('|     |')        
    print('|    / \\')     
    print('|_____________ ')

'''
--------------------------------------------------------------------------------
'''
pal = 'thompson'
i = int(0)
letra = input('Letra: ')
lpos = int(-1)
lne = int(0)
while (i < 8):
    for j in range(len(pal)):
        if(pal[j] != letra):
            print('_', end=' ')
        else:
            print(letra, end=' ')
            lpos = j
    if(lpos == -1):
        lne +=1
        funcion = 'muestra_ahorcado_'+str(lne)+'()'
        exec(funcion)
    i += 1
    letra = input('\nLetra: ')
    lne = 0
    lpos = -1
'''
pal = 'thompson'
for lne in range(8):
    funcion = 'muestra_ahorcado_'+str(lne)+'()'
    exec(funcion)
    input()
'''
