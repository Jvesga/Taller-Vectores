## Taller Vectores.
### Ejercicio 2. 
```python
# 2.Crea un programa que solicite al usuario la introducción de números enteros de forma continua. 
# La entrada de números finalizará únicamente cuando el usuario ingrese un cero. 
# A medida que se introducen los números, el programa deberá clasificarlos y 
# almacenarlos en dos estructuras de datos separadas: 
# una para los números pares y 
# otra para los números impares.

# Al finalizar la entrada de datos, 
# el programa debe: Mostrar el contenido de ambos vectores (pares e impares). 
# E Indicar la cantidad total de números pares e impares ingresados.

numero = 0
pares = []
impares = []

while True:
    numero = int(input("Digite un numero: "))

    if numero == 0:
        break

    if numero % 2 != 0:
        impares.append(numero)
    else:
        pares.append(numero)
    
print("Numeros pares: ")
print(pares)

print("Numeros impares: ")
print(impares)

print("La cantidad de numeros pares es de: " , len(pares))
print("La cantidad de numeros impares es de: ", len(impares))
```
### Ejercicio 3.
```python
#Realiza un programa que pida al usuario N números enteros y los inserte en un vector. 
#(N será un valor que pediremos al principio, pero nunca deberá ser mayor de 100). El programa deberá permitir entonces la búsqueda de elementos dentro del vector. 
# Para ello (y mientras el usuario no decida salir) se pedirá el número que se desea saber si existe en el vector y se devolverá, 
# en ese caso, su posición o se informará de que no existe. Para verificarlo, 
# muestra el contenido del vector por pantalla. 

N= int(input("Ingrese el tamaño de N (N no puede ser mayor a 100): "))
numeros=[]

if N > 100:
    print("El numero ingresado es mayor a 100 por favor inserte un numero menor a 100")

if N < 100:

    for i in range(0,N,1):
        numeros.append(int(input("Ingrese un numero entero: ")))

    while True:

        buscador=int(input("Que numero desea buscar, si no desea buscar digite el 0: "))

        if buscador == 0:
            print(numeros)
            break
    
        else:
            acumulador=0

            for a in range (0, N,1):

                if numeros[a]==buscador:
                    print("----El numero buscado si se encuentra en el vector----")
                    print(numeros)
                    print(f"Su posicion es la: {a +1} ")
                    acumulador=1

            if acumulador == 0:
                print("---El numero buscado no existe en el vector---")

```
### Ejercicio 4.
```python
#Realizar un programa que tenga una función para leer vectores tridimensionales, 
#otra para mostrarlos por pantalla, otra para sumar, otra para multiplicar escalarmente los vectores y otra para multiplicarlos vectorialmente. Realizar la función principal que haga uso de estas funciones (mediante un menú). 
#Nota: Dados dos vectores {(a1, a2, a3) y (b1, b2, b3)}, su producto escalar y su producto vectorial se calculan mediante:

#Producto escalar =  
#roducto vectorial de dos vectores u(x,y,z) y v(x,y,z), obteniendo: w(x,y,z)
#w[x] = u[y] * v[z] - u[z] * v[y];
#w[y] = u[z] * v[x] - u[x] * v[z];
#w[z] = u[x] * v[y] - u[y] * v[x];

vector1=[]
vector2=[]
resultado=0

for o in range(0,3,1):
    vector1.append(int(input("Ingrese un numero: ")))
    vector2.append(int(input("Ingrese un numero: ")))

print("---Menu de Opciones---")
print("---Opcion 1: Multiplicacion por Escalar.---")
print("---Opcion 2: Multiplicacion Vectorial.---")
opcion= print(int(input("Digite el numero de la Opcion deseada: ")))


if opcion==1:
    for i in range(0,3,1):
        
        resultado= (vector1[i]*vector2[i])+resultado
    print(f"El resultado de la multiplicacion escalar es: {resultado}") 

else:        
    vector_Resultado=[]
    vector_Resultado.append((vector1[1]*vector2[2])-(vector1[2]*vector2[1]))
    vector_Resultado.append((vector1[2]*vector2[0])-(vector1[0]*vector2[2]))
    vector_Resultado.append((vector1[0]*vector2[1])-(vector1[1]*vector2[0]))
    print(f"El resultado de la multiplicacion vectorial es: {vector_Resultado}")
```
### Ejercicio 5.
```python
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
```
