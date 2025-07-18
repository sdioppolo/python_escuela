import random

def verifica_num(nm, nj):
    cb=int(0)
    cm=int(0)
    cr=int(0)

    for i in range(len(nm)):
        j = int(0)
        while(nm[i] != nj[j] and j < len(nm)-1):
            j += 1
        if(nm[i] == nj[j]):
            if(i == j):
                cb += 1
            else:
                cr += 1
        else:
            cm +=1
    return (str(cb)+'B'+str(cm)+'M'+str(cr)+'R')   

    
def num_esta(n, m):
    r = False
    for i in range(len(m)):
        if (str(n) == m[i]):
            r = True
    return r

def genera_num():
    nm = ""
    for j in range(4):
        a = str(random.randint(0,9))
        while(num_esta(a, nm)):
            a = str(random.randint(0,9))
        nm += a
    return(nm)

for i in range(100):
    print(genera_num())

nj = input('Ingrese su Número: ')

print(verifica_num(nm, nj))
