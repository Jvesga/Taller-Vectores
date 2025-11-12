#Crea un programa para gestionar un inventario simple de productos. 
#El programa debe permitir al usuario:
#Agregar nuevos productos: Se solicitará el nombre del producto, 
#la cantidad en stock y el precio unitario.

#Mostrar el inventario completo: Se listarán todos los productos con su nombre, 
#cantidad y precio, 
#además de calcular y mostrar el valor total del inventario (suma de (cantidad * precio) 
#para cada producto).

#Buscar un producto por nombre: Se mostrarán los detalles del producto si existe.

N_producto= []
cantidad1= []
precio1= []

while True:
    print("---Opciones---")
    print("1. Agregar producto.")
    print("2. Mostrar inventario.")
    print("3. Buscar producto.")
    print("4. Salir.")
    opcion= input("Digite la opcion deseada:")

    if opcion=="1":
        nombre= input("Nombre del producto: ")
        cantidad2= int(input("Digite la cantidad del producto: "))
        precio2= float(input("Digite el precio del producto: "))
        N_producto.append(nombre)
        cantidad1.append(cantidad2)
        precio1.append(precio2)
        print("---Se agrego el producto---")

    elif opcion=="2":
        if len(N_producto)==0:
            print("---El inventario se encuentra vacio.---")
        else:
            total=0

            for i in range(len(N_producto)):
                valor = cantidad1[i] * precio1[i]
                print(f"{N_producto[i]}")
                print(f"cantidad: {cantidad1[i]}")
                print(f"precio: ${precio1[i]}")
                print(f"Valor: ${valor}")
    elif opcion=="3":
        buscar= input("Nombre del producto a buscar: ")
        encontrado = False

        for i in range(len(N_producto)):
            if N_producto[i] == buscar:
                print(f"Nombre: {N_producto[i]}")
                print(f"Cantidad: {cantidad1[i]}")
                print(f"precio: ${precio1[i]}")
                print(f"Valor: ${cantidad1[i] * precio1[i]}")
                encontrado = True
                break

    elif opcion== "4":
        print("---Digito la opcion para salir.---")
        break

