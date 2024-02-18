"""
Problema 1:
Bitcoin es una forma de moneda digital, también conocida como
criptomoneda. En lugar de depender de una autoridad central como un
banco, Bitcoin se basa en una red distribuida, también conocida como
cadena de bloques, para registrar transacciones.
En este problema debe generar un programa que realice:
-
-
Solicite al usuario por línea de comando un valor de “n” el cual representa la cantidad
de bitcoins que posee el usuario.
Consulte la API del índice de precios de Bitcoin de CoinDesk en el siguiente link
(https://api.coindesk.com/v1/bpi/currentprice.json), la cual retornará un objeto JSON,
entre cuyas claves anidadas encontrará el precio actual de Bitcoin como un número
decimal. Asegúrese de detectar cualquier excepción, como el siguiente código:
import requests
try:
...
except requests.RequestException:
...
-
Muestra el costo actual de “n” Bitcoins en USD con cuatro decimales, usando , como
separador de miles.
Nota: El empleo de format string es apropiado para brindar formatos a nuestros datos. Le será
de utilidad el siguiente comando: print(f"${amount:,.4f}")
Recuerde instalar la librería Requests mediante el comando: pip install requests
"""
import requests

def obtener_precio_bitcoin():

  try:
    # Realizar la petición HTTP a la API
    respuesta = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    # Si la petición fue exitosa
    if respuesta.status_code == 200:
      # Convertir la respuesta a un objeto JSON
      datos = respuesta.json()

      # Obtener el precio actual de Bitcoin
      precio_actual = datos["bpi"]["USD"]["rate_float"]

      return precio_actual
    else:
      # Si la petición no fue exitosa
      raise Exception(f"Error al obtener el precio de Bitcoin: {respuesta.status_code}")

  except requests.RequestException as e:
    # Si hubo un error al realizar la petición
    raise Exception(f"Error al conectar con la API de CoinDesk: {e}")

def calcular_costo_total(cantidad_bitcoins, precio_bitcoin):

  return cantidad_bitcoins * precio_bitcoin

def main():

  try:
    # Solicitar la cantidad de Bitcoins al usuario
    cantidad_bitcoins = float(input("Ingrese la cantidad de Bitcoins que posee: "))

    # Obtener el precio actual de Bitcoin
    precio_bitcoin = obtener_precio_bitcoin()

    # Calcular el costo total
    costo_total = calcular_costo_total(cantidad_bitcoins, precio_bitcoin)

    # Mostrar el costo total
    print(f"El costo total de {cantidad_bitcoins:,.4f} Bitcoins es: ${costo_total:,.4f}")

  except Exception as e:
    # Mostrar un mensaje de error si ocurre alguna excepción
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
