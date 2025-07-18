# comienzo
def calcula_descuento(p, d):
    return(p - (p*d)/100)

prod = int(input("Ingrese cantidad de productos: "))
for cont_prod in range(1, prod+1):
    menor_precio = 99999999
    menor_prov = ""
    nom_prod = input("Nombre del producto: ")
    for cont_prov in range(1, 4+1):
        nom_prov = input("Nombre del Proveedor: ")
        precio = float(input("Precio: "))
        descuento = int(input("Descuento: "))
        precio_prov = calcula_descuento(precio, descuento)
        print("El producto ", nom_prod, " el proveedor ", nom_prov, " lo vende a ", precio_prov)
        if (menor_precio > precio_prov):
            menor_precio = precio_prov
            menor_prov = nom_prov
    print("El menor precio del producto ", nom_prod, " lo ofrece el proveedor ", menor_prov, " a ", menor_precio)
# fin
