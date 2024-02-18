def contar_lineas_codigo(archivo):
    try:
        with open(archivo, "r") as file:
            lineas = file.readlines()
            lineas_codigo = 0
            comentario_multilinea = False

            for linea in lineas:
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                if linea.startswith("'''") or linea.startswith('"""'):
                    comentario_multilinea = not comentario_multilinea
                    continue
                if not comentario_multilinea and not linea.startswith("'''") and not linea.startswith('"""'):
                    lineas_codigo += 1

            return lineas_codigo
    except FileNotFoundError:
        print("El archivo especificado no fue encontrado.")
        return None


def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")

    if ruta_archivo.endswith(".py"):
        lineas_codigo = contar_lineas_codigo(ruta_archivo)
        if lineas_codigo is not None:
            print(f"Archivo: {ruta_archivo}, número de líneas de código: {lineas_codigo}")
    else:
        print("La ruta especificada no apunta a un archivo .py válido.")


if __name__ == "__main__":
    main()
