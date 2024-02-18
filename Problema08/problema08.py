import sqlite3
import requests

def obtener_precio_bitcoin():
    # Conexión a la base de datos
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()

    # Crear tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                        fecha TEXT PRIMARY KEY,
                        precio_usd REAL,
                        precio_gbp REAL,
                        precio_eur REAL,
                        precio_pen REAL
                    )''')

    # Hacer solicitud a la API de Bitcoin
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        fecha = data['time']['updated']
        precio_usd = float(data['bpi']['USD']['rate'].replace(',', ''))
        precio_gbp = float(data['bpi']['GBP']['rate'].replace(',', ''))
        precio_eur = float(data['bpi']['EUR']['rate'].replace(',', ''))

        # Obtener tipo de cambio PEN desde SUNAT
        url_sunat = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
        response_sunat = requests.get(url_sunat)
        if response_sunat.status_code == 200:
            data_sunat = response_sunat.json()
            tipo_cambio_pen = data_sunat['venta']

            # Calcular precio en PEN
            precio_pen = precio_usd * tipo_cambio_pen

            # Insertar datos en la tabla
            cursor.execute("INSERT OR IGNORE INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) VALUES (?, ?, ?, ?, ?)",
                           (fecha, precio_usd, precio_gbp, precio_eur, precio_pen))
            print(f"Datos para {fecha} almacenados en la tabla 'bitcoin'.")
        else:
            print("No se pudo obtener el tipo de cambio PEN desde SUNAT.")
    else:
        print("No se pudo obtener información del precio del Bitcoin.")

    # Guardar cambios y cerrar conexión
    conexion.commit()
    conexion.close()

def consultar_precios():
    # Conexión a la base de datos
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()

    # Consultar precios de compra de 10 bitcoins en moneda PEN y EUR
    cursor.execute("SELECT precio_pen, precio_eur FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    resultado = cursor.fetchone()
    if resultado:
        precio_pen_bitcoin = resultado[0] * 10
        precio_eur_bitcoin = resultado[1] * 10
        print(f"Precio de compra de 10 bitcoins en PEN: {precio_pen_bitcoin:.2f} PEN")
        print(f"Precio de compra de 10 bitcoins en EUR: {precio_eur_bitcoin:.2f} EUR")
    else:
        print("No hay datos disponibles en la tabla 'bitcoin'.")

    # Cerrar conexión
    conexion.close()

def main():
    obtener_precio_bitcoin()
    consultar_precios()

if __name__ == "__main__":
    main()
