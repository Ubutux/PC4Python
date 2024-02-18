import sqlite3
import requests

def obtener_datos_sunat(year):
    # Conexión a la base de datos
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()

    # Crear tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                        fecha TEXT PRIMARY KEY,
                        compra REAL,
                        venta REAL
                    )''')

    # Hacer solicitudes a la API y almacenar los datos en la base de datos
    url_base = "https://api.apis.net.pe/v1/tipo-cambio-sunat?month=5&year=2023"
    for mes in range(1, 13):
        url = f"{url_base}?month={mes}&year={year}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            dolar_compra = data['compra']
            dolar_venta = data['venta']
            fecha = f"{year}-{mes:02d}"  # Formato: YYYY-MM
            # Insertar datos en la tabla
            cursor.execute("INSERT OR IGNORE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)", (fecha, dolar_compra, dolar_venta))
            print(f"Datos para {fecha} almacenados en la base de datos.")
        else:
            print(f"No se pudo obtener información para {year}-{mes:02d}.")

    # Guardar cambios y cerrar conexión
    conexion.commit()
    conexion.close()

def mostrar_contenido_tabla():
    # Mostrar contenido de la tabla
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    print("\nContenido de la tabla 'sunat_info':")
    for row in cursor.fetchall():
        print(row)
    conexion.close()

def main():
    year = 2023
    obtener_datos_sunat(year)
    mostrar_contenido_tabla()

if __name__ == "__main__":
    main()


