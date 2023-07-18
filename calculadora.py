def menu():
    print("---- Calculadora ----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def suma(numero1, numero2):
    suma = numero1 + numero2
    return suma

def resta(numero1, numero2):
    resta = numero1 - numero2
    return resta

def multi(numero1, numero2):
    multi = numero1 * numero2
    return multi

def division(numero1, numero2):
    division = numero1 / numero2
    return division

def main():
    menu()
    opcion = input("Ingrese una opción: ")

    while opcion != "5":
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        if opcion == "1":
            print("La suma es: ", suma(num1, num2))
        elif opcion == "2":
            print("La resta es: ", resta(num1, num2))
        elif opcion == "3":
            print("La multiplicación es: ", multi(num1, num2))
        elif opcion == "4":
            print("La división es: ", division(num1, num2))
        else:
            print("Opción inválida")

        opcion2 = input("Desea realizar otra operación? (S/N):")
        if opcion2 == "S" or opcion2 == "s":
            menu()
            opcion = input("Ingrese una opción: ")
        elif opcion2 == "N" or opcion2 == "n":
            print("Adiós")
            break
        else:
            print("Opción inválida")

        
main()