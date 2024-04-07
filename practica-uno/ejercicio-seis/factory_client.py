import requests
import json

url = "http://localhost:8000/animales"
headers = {"Content-Type": "application/json"}

# Crear un animal
nuevo_animal = {  
    "animal_type": "ave",
    "nombre": "Condor",
    "genero": "Macho",
    "edad": 10,
    "peso": 12,   
}
print("\n***** Crear un animal *****\n")
post_response = requests.post(url=url, json=nuevo_animal, headers=headers)
print(post_response.json())

# Crear un animal
nuevo_animal = {  
    "animal_type": "mamifero",
    "nombre": "Tigre",
    "genero": "Hembra",
    "edad": 12,
    "peso": 15,   
}
print("\n***** Crear un animal *****\n")
post_response = requests.post(url=url, json=nuevo_animal, headers=headers)
print(post_response.json())

# Listar a todos los animales
print("\n***** Listar todos los animales *****\n")
get_response = requests.get(url=url)
print(get_response.json())

# Buscar animales por especie 

# Buscar animales por genero 

# Actualizar la información de un animal
update_animal = {
    "animal_type": "mamifero",
    "nombre": "Leon",
    "genero": "Macho",
    "edad": 6,
    "peso": 18,
}
print("\n***** Actualizar la informacin de un animal *****\n")
put_response = requests.put(url=url+"/1", json=update_animal)
print(put_response.json())

# Eliminar un animal
print("\n***** Eliminar un animal *****\n")
delete_response = requests.delete(url=url+"/1")
print(delete_response.json())

# Listar a todos los animales
print("\n***** Listar todos los animales *****\n")
get_response = requests.get(url=url)
print(get_response.json())