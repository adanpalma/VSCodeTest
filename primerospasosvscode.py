import math
import os
import sys
from os import rename

import requests


respuesta = requests.get("https://www.lahipotecaria.com/")

if respuesta.status_code == 200:
    print("La pagina esta arriba " + str(respuesta.status_code))
else:
    print("la pagina esta caida " + str(respuesta.status_code))


hola


def hola():
    print("hola" * 20)
