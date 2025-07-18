def mostrar_info():
    for i in range(len(v_nom)):
        print(v_nom[i],'\t', v_fdn[i],'\t', v_edd[i],'\t', v_sex[i])

def ordenar_edad():
    for i in range(len(v_edd)-1):
        for j in range(i+1,len(v_edd)):
            if(v_edd[i] < v_edd[j]):
                aux_e = v_edd[i]
                v_edd[i] = v_edd[j]
                v_edd[j] = aux_e
                
                aux_n = v_nom[i]
                v_nom[i] = v_nom[j]
                v_nom[j] = aux_n
                aux_f = v_fdn[i]
                v_fdn[i] = v_fdn[j]
                v_fdn[j] = aux_f
                aux_s = v_sex[i]
                v_sex[i] = v_sex[j]
                v_sex[j] = aux_s


v_nom=['María', 'Roberto', 'Martina', 'Valeria', 'Julio', 'Sonia', 'Marcelo']
v_fdn=['19540123','19640227','19500312','19760424','19370505','19420627','19520730']
v_edd=[71, 61, 75, 49, 88, 83, 73]
v_sex=['F', 'M', 'F', 'F', 'M', 'F', 'M']


mostrar_info()
print('-'*60)
ordenar_edad()
print('-'*60)
mostrar_info()
