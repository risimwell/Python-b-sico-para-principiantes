# Definición de funciones para las operaciones básicas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # Verificar división por cero
    if b != 0:
        return a / b
    else:
        return "Error:  No se puede división por cero"

# Bucle principal de la calculadora
while True:
    # Mostrar el menú
    print("Calculadora Simple")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    # Solicitar al usuario que seleccione una opción
    opcion = input("Seleccione una operación: ")

    # Salir del bucle si la opción es 5
    if opcion == "5":
        print("¡Hasta luego!")
        break

    # Realizar operación si la opción es válida
    if opcion in ("1", "2", "3", "4"):
        # Solicitar los números al usuario
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        # Realizar la operación correspondiente y mostrar el resultado
        if opcion == "1":
            print("Resultado:", sumar(num1, num2))
        elif opcion == "2":
            print("Resultado:", restar(num1, num2))
        elif opcion == "3":
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == "4":
            print("Resultado:", dividir(num1, num2))
    else:
        # Mensaje de error si la opción no es válida
        print("Opción no válida. Por favor, seleccione una opción válida.")
