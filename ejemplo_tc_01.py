#Potencia con FOR
a = int(input('A: '))
b = int(input('B: '))

p = int(1)

for i in range(b):
    p *= a

print('El resultado de elevar ',a, ' a la ',b, ' es igual a: ', p)

#fin
