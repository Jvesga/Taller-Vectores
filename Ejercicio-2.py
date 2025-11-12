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