import requests

respuesta = requests.get("https://www.lahipotecaria.com/")
if respuesta.status_code == 200:
    print("La pagina esta arriba " + str(respuesta.status_code))
else:
    pass
