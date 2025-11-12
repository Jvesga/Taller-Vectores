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

                
            
 
