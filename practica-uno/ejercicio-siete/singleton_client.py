import requests
import json

url = "http://localhost:8000"
headers = {"Content-Type": "application/json"}

# Crear una partida nueva
print("\n***** Crear una partida *****\n")
response = requests.post(url=url +"/partidas", json={"elemento": "piedra"}, headers=headers)
print(response.json())

# Crear una partida nueva
print("\n***** Crear una partida *****\n")
response = requests.post(url=url +"/partidas", json={"elemento": "tijera"}, headers=headers)
print(response.json())

# Crear una partida nueva
print("\n***** Crear una partida *****\n")
response = requests.post(url=url +"/partidas", json={"elemento": "piedra"}, headers=headers)
print(response.json())


# Listar todas las partidas
print("\n***** Listar todas las partidas *****\n")
response = requests.get(f"{url}/partidas")
print(response.json())


# Listar partidas perdidas
print("\n***** Listar partidas perdidas *****\n")
response = requests.get(f"{url}/partidas?resultado=perdio")
print(response.json())

# Listar partidas ganadas
print("\n***** Listar partidas ganadas *****\n")
response = requests.get(f"{url}/partidas?resultado=gano")
print(response.json())
