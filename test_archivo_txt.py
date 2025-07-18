'''
 Archivos Secuenciales.

 Modos de apertura de los archivos son:

 w ---> write  (Escribe en el archivo borrando los existentes
 a ---> append (Agrega datos en un archivo existente o crea el archivo si no existe)
 r ---> read   (Leer los datos del archivo)
 
'''
vec_nom = []
aux_nom = ''

while(aux_nom != 'CHAU!'):
    aux_nom = str(input('Nombre: ')).upper()
    if(aux_nom != 'CHAU!'):
        vec_nom.append(aux_nom)

''' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 Escritura desde vector de cadenas a archivo de texto.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - '''

nom_txt = open('nombres.txt', 'a', encoding='utf-8')

for i in range(len(vec_nom)):
    nom_txt.write(vec_nom[i]+'\n')

nom_txt.close()

vec_nom.clear()

''' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 Lectura de archivo de texto a vector de cadena.
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'''
nom_txt = open('nombres.txt', 'r', encoding='utf-8')

for linea in nom_txt:
    aux_nom = linea[:-1]
    vec_nom.append(aux_nom)
    print(aux_nom)

nom_txt.close()

print(vec_nom)
