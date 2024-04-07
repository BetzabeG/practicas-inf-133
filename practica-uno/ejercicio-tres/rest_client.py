import requests
url = "http://localhost:8000/"

# Crear un paciente
ruta_post = url + "pacientes"
nuevo_paciente = {
    "nombre": "Margharet",
    "apellido": "Ruiz",
    "edad": 30,
    "genero": "Femenino",
    "diagnostico": "Ansiedad",
    "doctor": "Jorge Salas",
}
print("\n****** Crear un paciente *****\n")
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_paciente)
print(post_response.text)

# Listar todos los pacientes
ruta_get = url + "pacientes"
print("\n****** Listar todos los pacientes *****\n")
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# Buscar pacientes por CI
ruta_get = url + "pacientes/1"
print("\n****** Buscar pacientes por CI *****\n")
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# Listar a los pacientes que tienen diagnostico de `Diabetes`
ruta_get = url + "pacientes?diagnostico=Diabetes"
print("\n****** Listar a los pacientes que tienen diagnostico de `Diabetes` *****\n")
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# Listar a los pacientes que atiende el Doctor `Pedro Pérez`
ruta_get = url + "pacientes?doctor=Pedro Perez"
print("\n****** Listar a los pacientes que atiende el Doctor `Pedro Pérez` *****\n")
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# Actualizar la información de un paciente
ruta_put = url + "pacientes/2"
paciente_actualizado = {
    "nombre": "Albert",
    "apellido": "Loza",
    "edad": 26,
    "genero": "Masculino",
    "diagnostico": "Tuberculosis",
    "doctor": "Noemi Estrada",
}
print("\n****** Actualizar la información de un paciente *****\n")
put_response = requests.request(method="PUT", url=ruta_put, json=paciente_actualizado)
print(put_response.text)

# Eliminar un paciente
ruta_delete = url + "pacientes/1"
print("\n****** Eliminar un paciente *****\n")
delete_response = requests.request(method="DELETE", url=ruta_delete)
print(delete_response.text)

# Listar todos los pacientes
ruta_get = url + "pacientes"
print("\n****** Lista de pacientes actualmente *****\n")
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)


