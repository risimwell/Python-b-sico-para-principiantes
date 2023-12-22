# Variables 

#nombre = "Ricardo"
#edad = 37
#peso = 58
#estatura = 168.5


#print(nombre,edad,peso,estatura)



# # tipos de datos 
#Enteros 
#numero_entero = 42
#print(type(numero_entero))  # Muestra <class 'int'>

# #Flotantes 
#numero_flotante = 3.14
#print(type(numero_flotante)) # Muestra <class 'float'>

## #Cadenas de texto
#texto = "Hola, mundo"
#print(type(texto))  # Muestra <class 'str'>

#Booleanos 
#verdadero = True
#falso = False
#print(verdadero,falso)  # Muestra <class 'bool'>
#print(type(falso))  # Muestra <class 'bool'>

#Listas 
""" mi_lista = [1, 2, 3, 4, 5]
mis_mumeros = [1 , 2, 3, 4 ,5 ,6]
mi_lista = mis_mumeros
print(mi_lista)
mis_mumeros = [1,3,6,7,8]
print(mis_mumeros)
primer_elemento = mi_lista[2]
print("el elemnto de la lista es",primer_elemento)
sublista = mi_lista[1:4] # mostrara los valores del 1-3
print("los valores de las sublista son:",sublista)
mi_lista.append(20)
print("el nuevo valor de mi lista es:",mi_lista)
print(type(mi_lista))  # Muestra <class 'list'>
print("------------------------------------------------------------------")

mi_tupla = (10, 20, 30)
print(mi_tupla)
print(type(mi_tupla))  # Muestra <class 'tuple'>

print("-----------------------------------------------------------------")

mi_diccionario = {"nombre": "Juan", "edad": 25}
print(mi_diccionario)
print(type(mi_diccionario))  # Muestra <class 'dict'>

print("-----------------------------------------------------------------")

mi_conjunto = {1, 2, 3, 4, 5}
print(mi_conjunto)
print(type(mi_conjunto))  # Muestra <class 'set'>

print("-----------------------------------------------------------------")

nulo = None
print(nulo)
print(type(nulo))  # Muestra <class 'NoneType'> """

#COMO CREAR TUPLAS

""" #Utilizando un par de paréntesis: ( )
numeros = (1,2,3)
print(numeros)
#Utilizando una coma a la derecha: x,
numeros1 = 1,2,3
print(numeros1)

#Utilizando un par de paréntesis con objetos separados por comas: ( x, y, z )
numeros2 = 1,2
numeros3 = (3,4)
conjunto = (numeros2,numeros3)
print(conjunto)


#Utilizando: tuple() o tuple(iterador)
mi_lista = tuple([1,2,3,4,5])
print(mi_lista) """

#Operedores arimeticos 
# suma, resta, multipliacion, division, mayor que, menor que, igual, igual igual, resudio
#  +    -       *               /           <       >           =       ==          %

 # Condicionales 

""" edad = 15

if edad >= 18:
    print("Es mayor de edad")
else:
    print("No eres mayor de edad") """





""" puntuacion = 69

if puntuacion >= 90:
    print("Aprobado con 5")
elif puntuacion >= 80:
    print("Aprobado con 4")
elif puntuacion >= 70:
    print("Aprobado con 3")
else:
    print("No aprobado")
 """
 ##Condicionales Anidados 
""" print("Bienveido a su calculadora de mayoria de edad") 
edad = int(input("Por favor ingrese la edad"))
sexo = input("Por favor ingrese su sexo")

if edad >= 18:
    if sexo == "masculino":
        print("Eres un hombre mayor de edad.")
    else:
        print("Eres una mujer mayor de edad.")
else:
    print("Eres menor de edad.") """

# # Switch case

# def opcion_1():
#     return "Elegiste la opción 1."

# def opcion_2():
#     return "Elegiste la opción 2."

# def opcion_3():
#     return "Elegiste la opción 3."

# def default():
#     return "Opción no válida."

# opciones = {
#     1: opcion_1,
#     2: opcion_2,
#     3: opcion_3
# }

# eleccion = 2

# resultado = opciones.get(eleccion, default)()
# print(resultado)



# # Ciclos
# # Imprimir los números del 1 al 5 utilizando un ciclo for

#para        #dentro
###for numero in range(1, 1000):
###   print(numero

#Imprimir los números del 1 al 5 utilizando un ciclo while
#print("Imprimiendo con ciclo while:")
""" numero = 1
while numero <= 5:
    print(numero)
    numero += 1 """


# Funcion completa con todo lo anterior 

# def procesar_datos():

#     edad= 17
#     genero = "masculino"

#     if edad >= 18:
#         if genero == "masculino":
#             print("Eres un hombre mayor de edad.")
#         else:
#             print("Eres una mujer mayor de edad.")
#     else:
#         print("Eres menor de edad")

# procesar_datos()


# #     # Estructura tipo "switch case" simulada
# def opcion_1():
#     return "Elegiste la opción 1."

# def opcion_2():
#     return "Elegiste la opción 2."

# def opcion_3():
#     return "Elegiste la opción 3."

# def default():
#     return "Opción no válida."

# opciones = {
# 1: opcion_1,
# 2: opcion_2,
# 3: opcion_3
# }

# eleccion = 3
# resultado = opciones.get(eleccion, default)()
# print(resultado)

# # Llamada a la función con datos de ejemplo
# procesar_datos(20, "masculino")

while True:
    # Mostrar el menú
    print("Juego el calamar")
    print("1. Luz verde")
    print("2. La galleta")
    print("3. Puente de cristal")
    print("4. Salir")

    # Solicitar al usuario que seleccione una opción
    opcion = input("Seleccione un juego: ")

    # Salir del bucle si la opción es 4
    if opcion == "4":
        print("¡Hasta luego!")
        break

    # Realizar operación si la opción es válida
    if opcion in ("1", "2", "3"):
        # Solicitar los números al usuario
        print("Ahora es el momento de empezar jugar ")

        # Realizar la operación correspondiente y mostrar el resultado
        if opcion == "1":
            print("Has jugado luz verde:")
        elif opcion == "2":
            print("Has jugado galleta:")
        elif opcion == "3":
            print("Has jugado puente de cristal:")
        
    else:
        # Mensaje de error si la opción no es válida
        print("Opción no válida. Por favor, seleccione una opción válida.")


