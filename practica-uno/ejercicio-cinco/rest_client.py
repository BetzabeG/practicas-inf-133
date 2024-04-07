import requests

url = "http://localhost:8000/"

ruta_post = url + "animales"
nuevo_animal = {
    "nombre": "Condor",
    "especie": "Ave",
    "genero": "Macho",
    "edad": 10,
    "peso": 12,   
}
print("\n***** Crear un animal *****\n")
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_animal)
print(post_response.text)

# Listar a todos los animales
ruta_get = url + "animales"
print("\n***** Listar todos los animales *****\n")
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# Buscar animales por especie   
ruta_get_especie = url + "animales?especie=Mamifero"
print("\n***** Buscar animales por especie *****\n")
get_response_especie = requests.request(method="GET", url=ruta_get_especie)
print(get_response_especie.text)

# Buscar animales por genero 
ruta_get_genero= url + "animales?genero=Macho"
print("\n***** Buscar animales por genero *****\n")
get_response_genero = requests.request(method="GET", url=ruta_get_genero)
print(get_response_genero.text)

# Actualizar la información de un animal
ruta_update = url + "animales/1"
animal_actualizado = {
    "nombre": "Leon",
    "especie": "Mamifero",
    "genero": "Macho",
    "edad": 6,
    "peso": 18,
}
print("\n***** Actualizar la informacin de un animal *****\n")
put_response = requests.request(method="PUT", url=ruta_update, json=animal_actualizado)
print(put_response.text)

# Eliminar un animal
ruta_delete = url + "animales/2"
print("\n***** Eliminar un animal *****\n")
delete_response = requests.request(method="DELETE", url=ruta_delete)
print(delete_response.text)


# Listar a todos los animales
ruta_get = url + "animales"
print("\n***** Listar todos los animales *****\n")
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
