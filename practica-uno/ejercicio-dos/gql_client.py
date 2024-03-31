import requests
url = 'http://localhost:8000/graphql'

# Definimos la consulta GraphQL para crear una nueva planta
query_crear = """
mutation {
        crearPlanta(nombre: "Girasol", especie: "Girasol", edad: 6, altura: 120, frutos: True){
            Planta {
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

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)