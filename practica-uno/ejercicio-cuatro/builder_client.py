import requests

url = "http://localhost:8000/pacientes"
headers = {'Content-type': 'application/json'}
# Crear un paciente
mi_paciente = {
    "nombre": "Anahi",
    "apellido": "Montes",
    "edad": 22,
    "genero": "Femenino",
    "diagnostico": "Gastritis",
    "doctor": "Marcos Cueto"
}
print("\n***** Crear un paciente *****\n")
post_response = requests.post(url, json=mi_paciente, headers=headers)
print(post_response.json())

# Crear un paciente
mi_paciente = {
    "nombre": "Carlos",
    "apellido": "Oruela",
    "edad": 25,
    "genero": "Masculino",
    "diagnostico": "Hipertension",
    "doctor": "Fernando Salas"
}
print("\n***** Crear un paciente *****\n")
post_response = requests.post(url, json=mi_paciente, headers=headers)
print(post_response.json())

# Listar todos los pacientes
get_response = requests.get(url)
print("\n***** Listar todos los pacientes *****\n")
print(get_response.json())
'''
# Buscar pacientes por CI
get_response = requests.get(url + "/1")
print("\n***** Buscar pacientes por CI *****\n")
print(get_response)'''

# Actualizar la informacion de un paciente
edit_paciente ={
    "nombre": "Albert",
    "apellido": "Loza",
    "edad": 26,
    "genero": "Masculino",
    "diagnostico": "Tuberculosis",
    "doctor": "Noemi Estrada",
}
print("\n***** Actualizar la informacion de un paciente *****\n")
put_response = requests.put(url + "/1", json=edit_paciente, headers=headers)
print(put_response.json())

#  Eliminar un paciente
print("\n***** Eiminar un paciente *****\n")
delete_response = requests.delete(url + "/1")
print(delete_response.json())

# Listar todos los pacientes
get_response = requests.get(url)
print("\n***** Lista de los pacientes actualmente *****\n")
print(get_response.json())