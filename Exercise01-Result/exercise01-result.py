#creando lista vacía
listaRegistro = []
suma = 0
clientes = 0

#Indicacioens
print("Ingrese la cantidad de clientes que desee. Una vez ya no quiera seguir introduciendo registros, digite un espacio cuando le pida el nombre del cliente. Inmediatamente le aparecerá un mensaje con el costo total ingresado")

#Inicio del bucle
while True:
    cliente = input("Nombre del cliente: ")
    if cliente != " ":
        producto = input("Producto: ")
        costo = float(input("Costo ($0.00):"))
        # Crea directorio
        registro = dict(cliente=cliente, producto=producto, costo=costo)
        #Agrega nuevo elementos a la lista
        listaRegistro.append(registro)
        #suma cada costo que se agrega
        suma += (listaRegistro[clientes]["costo"])
        #aumenta el número de cliente registrado
        clientes+=1
    else:
        #termina el bucle
        break
#Imprime total del costo
print("El costo obtenido hasta ahora es de: " , suma)