import requests
url = 'http://localhost:8000/graphql'

# Definimos la consulta GraphQL para crear una nueva planta

query_crear = """
mutation {
        crearPlanta(nombre: "Girasol", especie: "Helianthus annuus", edad: 4, altura: 20, frutos: true){
            planta {
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""
print("\n****** Crear una nueva planta *****\n")
response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

query_lista = """
{
        plantas{
            id
            nombre
            especie
            edad
            altura
            frutos
        }
}
"""

print("\n***** Lista de las plantas *****\n")
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Buscar plantas por especie
query_especie = """
{
    plantasPorEspecie(especie:"Rubus fruticosus"){
        id
        nombre
    }
}
"""

print("\n***** Buscar plantas por especie *****\n")
response = requests.post(url, json={'query': query_especie})
print(response.text)

# Buscar las plantas que tienen frutos
query_tienen_frutos = """
{
    plantasTienenFrutos{
        id
        nombre
    }
}
"""
print("\n***** Buscar las plantas que tienen frutos *****\n")
response = requests.post(url, json={'query': query_tienen_frutos})
print(response.text)

# Definimos la consulta para actualizar la información de una planta
query_actualizar_planta = """
mutation {
    actualizarPlanta(id:2, nombre: "Cocotero", especie: "Cocos nucifera", edad: 10, altura: 500, frutos: true){
        planta{
            id
            nombre
            especie
            edad
            altura
            frutos
        }
    }
}
"""
print("\n***** Actualizar la informacion de una planta ****\n")
response = requests.post(url, json={'query': query_actualizar_planta})
print(response.text)

# Definimos la consulta GraphQL para eliminar una planta
query_eliminar = """
mutation {
    eliminarPlanta(id: 3){
        planta{
            id
            nombre
            especie
            edad
            altura
            frutos
        }
    }
}
"""
print("\n***** Eliminar una planta *****\n")
response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)

print("\n***** Lista de las plantas actualmente*****\n")
response = requests.post(url, json={'query': query_lista})
print(response.text)