def mostrar_info():
    for i in range(len(datos)):
        print(datos[i][0],datos[i][1],datos[i][2],datos[i][3])


def ordenar_nom():
    for i in range(len(datos) - 1):
        for j in range(i + 1, len(datos)):
            if(datos[i][0] < datos[j][0]):
                aux = datos[i]
                datos[i] = datos[j]
                datos[j] = aux


datos=[['María', '19540123', 71, 'F'],
      ['Roberto', '19640227', 61, 'M'],
      ['Martina', '19500312', 75, 'F'],
      ['Valeria', '19760424', 49, 'F'],
      ['Julio', '19370505', 88, 'M'],
      ['Sonia', '19420627', 83, 'F'],
      ['Marcelo', '19520730', 73, 'M']]

mostrar_info()
print('-'*60)
ordenar_nom()
print('-'*60)
mostrar_info()
