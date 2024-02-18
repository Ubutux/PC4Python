"""
FIGlet, llamado así por las cartas de Frank, Ian y Glen, es un programa de principios de la
década de 1990 para hacer letras grandes a partir de texto ordinario, una forma de arte ASCII:
-
-
En la siguiente web puede ver una lista de fuentes admitidas por FIGlet
figlet.org/examples.html
Desde entonces, FIGlet ha sido portado a Python como un módulo llamado pyfiglet.
Cree un programa el cual cumpla con las siguientes especificaciones:
-
-
-
Solicite al usuario el nombre de una fuente a utilizar. En caso no sé ingrese ninguna
fuente, su programa deberá seleccionar de forma aleatoria la fuente a utilizar.
Solicite al usuario un texto.
Finalmente, su programa deberá imprimir el texto solicitado usando la fuente
apropiada.
Notas:
-
-
Instalar la librería usando: pip install pyfiglet
Para usar la librería, debe hacer:
from pyfiglet import Figlet
figlet = Figlet()
-
-
-
-
Puede obtener la lista de fuentes disponibles usando: figlet.getFonts()
Para seleccionar el fondo a utilizar emplee: figlet.setFont(font=fuente_seleccionada)
Finalmente podrá imprimir el texto usando : print(figlet.renderText(texto_imprimir))
Recuerde que random tiene un método random choice
"""

import pyfiglet
import random

def obtener_fuente_aleatoria(fuentes):

  return random.choice(fuentes)

def main():

  # Obtener la lista de fuentes disponibles
  fuentes = pyfiglet.Figlet().getFonts()

  # Solicitar el nombre de la fuente al usuario
  nombre_fuente = input("Ingrese el nombre de la fuente (o presione Enter para aleatorio): ")

  # Si no se ingresa ninguna fuente, seleccionar una aleatoria
  if not nombre_fuente:
    nombre_fuente = obtener_fuente_aleatoria(fuentes)

  # Solicitar el texto al usuario
  texto = input("Ingrese el texto a imprimir: ")

  # Imprimir el texto con la fuente seleccionada
  figlet = pyfiglet.Figlet(font=nombre_fuente)
  print(figlet.renderText(texto))

if __name__ == "__main__":
  main()
