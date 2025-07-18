# comienzo
alu = int(input("Ingrese cantidad de alumnos: "))
mayor_prom = float(0.0)
mayor_nom = ""
for cont_alu in range(1,alu+1):
    prom_alu = float(0.0)
    nom_alu = input("Ingrese Nombre: ")
    for cont_notas in range(1, 5+1):
        nota = int(input("Ingrese nota "+ str(cont_notas) + ": "))
        prom_alu += nota
    prom_alu /= 5
    print("El alumno ", nom_alu, " promedió: ", prom_alu)
    if(prom_alu > mayor_prom):
        mayor_prom = prom_alu
        mayor_nom = nom_alu
print("El alumno ", mayor_nom, " obtuvo el mayor promedio con: ", mayor_prom)
# fin
