#creando la lista vacía
listaRegistro = []
suma = 0
clientes = 0

print("Ingrese la cantidad de clientes que desee. Una vez ya no quiera seguir introduciendo registros, digite un espacio cuando le pida el nombre del cliente. Inmediatamente le aparecerá un mensaje con el costo total ingresado")
while True:
    cliente = input("Nombre del cliente: ")
    if cliente != " ":
        producto = input("Producto: ")
        costo = float(input("Costo ($0.00):"))
        # punto de programa
        registro = dict(cliente=cliente, producto=producto, costo=costo)
        #como agrego un elemento nuevo a una lista?
        listaRegistro.append(registro)
        #dejar de ocupar la variable registro
        # #registro = None
        suma += (listaRegistro[clientes]["costo"])
        clientes+=1
    else:
        break

print("El costo obtenido hasta ahora es de: " , suma)