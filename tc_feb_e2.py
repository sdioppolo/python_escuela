import math

def cifrado_transposicion(texto):
    n = math.ceil(math.sqrt(len(texto)))
    matriz = [['' for _ in range(n)] for _ in range(n)]

    index = 0
    for i in range(n):
        for j in range(n):
            while index < len(texto) and texto[index] == ' ':
                index += 1
            if index < len(texto):
                matriz[i][j] = texto[index]
                index += 1

    mensaje_cifrado = ""
    for j in range(n):
        for i in range(n):
            if matriz[i][j] != '':
                mensaje_cifrado += matriz[i][j]

    return mensaje_cifrado, matriz

mensaje = input("Ingrese el mensaje: ")
cifrado, matriz_generada = cifrado_transposicion(mensaje)

print("\nMatriz generada:")
for fila in matriz_generada:
    print(" ".join(fila))

print("\nMensaje cifrado:", cifrado)

mensaje_reves = cifrado[::-1]

print("mensaje cifrado al reves:", mensaje_reves)
