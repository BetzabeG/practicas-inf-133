import requests
url = "http://localhost:8000/"
# Crear un mensaje
ruta_post = url + "mensajes"
nuevo_mensaje = {
    "contenido": "Hola, que tal",
}
print("\n***** Crear un mensaje *****\n")
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_mensaje)
print(post_response.text)

# Crear un mensaje
ruta_post = url + "mensajes"
nuevo_mensaje = {
    "contenido": "Bienvenida",
}
print("\n***** Crear un mensaje *****\n")
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_mensaje)
print(post_response.text)

# Listar todos los mensajes
ruta_get = url + "mensajes"
print("\n***** Listar todos los mensajes *****\n")
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# Buscar mensajes por ID
ruta_get = url + "mensajes/1"
print("\n***** Buscar mensajes por ID *****\n")
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

#Actualizar el contenido de un mensaje
ruta_put = url + "mensajes/1"
mensaje_actualizado = {
    "contenido": "Hello, how are you?"
}
print("\n***** Actualizar el contenido de un mensaje *****\n")
put_response = requests.request(method="PUT", url=ruta_put, json=mensaje_actualizado)
print(put_response.text)

# Eliminar un mensaje
ruta_eliminar = url + "mensajes/1"
print("\n***** Eliminar un mensaje *****\n")
delete_response = requests.request(method="DELETE", url=ruta_eliminar)

# Listar todos los mensajes
ruta_get = url + "mensajes"
print("\n***** Lista actual de todos los mensajes *****\n")
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)