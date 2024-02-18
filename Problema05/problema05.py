def escribir_tabla_multiplicar():
    try:
        numero = int(input("Ingrese un número entero entre 1 y 10: "))
        if 1 <= numero <= 10:
            with open(f"tabla-{numero}.txt", "w") as file:
                for i in range(1, 11):
                    file.write(f"{numero} x {i} = {numero*i}\n")
            print(f"Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt")
        else:
            print("El número ingresado está fuera del rango permitido.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")


def leer_tabla_multiplicar():
    try:
        numero = int(input("Ingrese un número entero entre 1 y 10 para leer su tabla de multiplicar: "))
        if 1 <= numero <= 10:
            try:
                with open(f"tabla-{numero}.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print(f"El archivo tabla-{numero}.txt no existe.")
        else:
            print("El número ingresado está fuera del rango permitido.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")


def mostrar_linea_tabla_multiplicar():
    try:
        numero = int(input("Ingrese un número entero entre 1 y 10 para leer su tabla de multiplicar: "))
        linea = int(input("Ingrese el número de línea que desea ver: "))
        if 1 <= numero <= 10:
            try:
                with open(f"tabla-{numero}.txt", "r") as file:
                    lineas = file.readlines()
                    if 1 <= linea <= len(lineas):
                        print(lineas[linea - 1])
                    else:
                        print("El número de línea ingresado está fuera del rango permitido.")
            except FileNotFoundError:
                print(f"El archivo tabla-{numero}.txt no existe.")
        else:
            print("El número ingresado está fuera del rango permitido.")
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")


def main():
    while True:
        print("\nMenú:")
        print("1. Escribir tabla de multiplicar en un archivo.")
        print("2. Leer tabla de multiplicar desde un archivo.")
        print("3. Mostrar línea de la tabla de multiplicar desde un archivo.")
        print("4. Salir.")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            escribir_tabla_multiplicar()
        elif opcion == "2":
            leer_tabla_multiplicar()
        elif opcion == "3":
            mostrar_linea_tabla_multiplicar()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")


if __name__ == "__main__":
    main()
