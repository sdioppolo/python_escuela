f=int(1)
n = int(input('N: '))
a = n

for i in range(n):
    f *= a # f = f * a
    a -= 1 # a = a - 1

print('El factorial de ', n, ' es ', f)
