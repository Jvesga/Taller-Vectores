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