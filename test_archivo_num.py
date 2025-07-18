# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Escritura de matriz numérica a archivo de texto.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''
mat_num = [[10, 20, 30, 40], 
           [15, 25, 35, 45], 
           [50, 60, 70, 80], 
           [55, 65, 75, 85]]

mat_txt = open('matriz_num.txt', 'w', encoding='utf-8')

for fi in range(4):
    for co in range(4):
        if(co < 3):
            mat_txt.write(str(mat_num[fi][co]) + ', ')
        else:
            mat_txt.write(str(mat_num[fi][co]) + '\n')

mat_txt.close()
'''
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Lectura de archivo de texto a matriz numérica.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
mat_aux = [None] * 4
for fi in range(4):
    mat_aux[fi] = [None] * 4

mat_txt = open('matriz_num.txt', 'r', encoding='utf-8')

fi = int(0)
linea_mat = mat_txt.readline()
while (linea_mat != ''):
    aux_lin = linea_mat.split(',', 4)
    for co in range(4):
        mat_aux[fi][co] = int(aux_lin[co]) 
    fi += 1
    linea_mat = mat_txt.readline()

for fi in range(4):
    print(mat_aux[fi])

mat_txt.close()


