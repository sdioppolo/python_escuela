# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Escritura de matriz de caracteres a archivo de texto.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''
mat_nom = [['Sergio Daniel', 'Ioppolo', 'sdilabo@gmail.com', '12344321'], 
           ['Pablo', 'Della Paolera', 'pabdelpao@fmail.com', '23456543'], 
           ['María', 'Sánchez de Thompson', 'et3@dmail.com', '47717198'], 
           ['Domingo Faustino', 'Sarmiento', 'dmf@smail.com', '85326743']]


mat_txt = open('matriz_txt.txt', 'w', encoding='utf-8')

for fi in range(4):
    for co in range(4):
        if(co < 3):
            mat_txt.write(str(mat_nom[fi][co]) + ', ')
        else:
            mat_txt.write(str(mat_nom[fi][co]) + '\n')

mat_txt.close()
'''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Lectura de archivo de texto a matriz de caracteres.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
mat_aux = [None] * 4
for fi in range(4):
    mat_aux[fi] = [None] * 4

mat_txt = open('matriz_txt.txt', 'r', encoding='utf-8')

fi = int(0)
linea_mat = mat_txt.readline()
while (linea_mat != ''):
    aux_lin = linea_mat.split(', ', 4)
    for co in range(4):
        if (co < 3):
            mat_aux[fi][co] = aux_lin[co]
        else:
            mat_aux[fi][co] = str(aux_lin[co])[:-1]

    fi += 1
    linea_mat = mat_txt.readline()

for fi in range(4):
    print(mat_aux[fi])

mat_txt.close()
