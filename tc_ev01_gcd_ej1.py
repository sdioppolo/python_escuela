# comienzo
n = int(input("N: "))
f = int(1)
c = n
for i in range(1, n+1):
    f *= c
    c -= 1
print("El factorial de ", n, " es ", f)
#fin
print("Versión con REVERSED")
f = 1
for c in reversed(range(1, n+1)):
    f *= c
print("El factorial de ", n, " es ", f)
