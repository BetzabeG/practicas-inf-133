from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, Boolean, List, Schema, Field, Mutation

class Planta(ObjectType):
    id = Int()
    nombre = String()
    especie = String()
    edad = Int()
    altura = Int()
    frutos = Boolean()
    
class Query(ObjectType):
    plantas = List(Planta)
    plantas_por_especie = List(Planta, especie=String())
    plantas_tienen_frutos = List(Planta)
# Listar todas las plantas   
    def resolve_plantas(root, info):
        return plantas
# Buscar plantas por especie   
    def resolve_plantas_por_especie(root, info, especie):
        plantas_encontradas = []
        for planta in plantas:
            if planta.especie == especie:
                plantas_encontradas.append(planta)
        return plantas_encontradas  

# Buscar las plantas que tienen frutos 
    def resolve_plantas_tienen_frutos(root, info):
        plantas_encontradas = []
        for planta in plantas:
            if planta.frutos:
                plantas_encontradas.append(planta)
        return plantas_encontradas

# Actualizar la información de una planta
class ActualizarPlanta(Mutation):
    class Arguments:
        id = Int()
        nombre = String()
        especie = String()
        edad = Int()
        altura = Int()
        frutos = Boolean()
    planta = Field(Planta)
    def mutate(root, info, id, nombre, especie, edad, altura, frutos):
        for planta in plantas:
            if planta.id == id:
                planta.nombre == nombre
                planta.especie == especie
                planta.edad == edad
                planta.altura == altura
                planta.frutos == frutos
                return ActualizarPlanta(planta = planta)
# Eliminar una planta
class EliminarPlanta(Mutation):
    class Arguments:
        id = Int()
    planta = Field(Planta)
    def mutate(root, info, id):
        for i, planta in enumerate(plantas):
            if planta.id == id:
                plantas.pop(i)
                return EliminarPlanta(planta=planta)
        return None
    
# Crear una planta    
class CrearPlanta(Mutation):
    class Arguments:
        nombre = String()
        especie = String()
        edad = Int()
        altura = Int()
        frutos = Boolean()
        
    planta = Field(Planta)
    
    def mutate(root, info, nombre, especie, edad, altura, frutos):
        nueva_planta = Planta(
            id = len(plantas) + 1,
            nombre = nombre,
            especie = especie,
            edad = edad,
            altura = altura,
            frutos = frutos
        )
        plantas.append(nueva_planta)
        return CrearPlanta(planta = nueva_planta)     
        
class Mutations(ObjectType):
    crear_planta = CrearPlanta.Field()
    actualizar_planta = ActualizarPlanta.Field()
    eliminar_planta = EliminarPlanta.Field()
    
    
plantas = [
    Planta(id=1, nombre="Ortiga comun", especie="Urtica dioica", edad=3, altura=150, frutos=False),
    Planta(id=2, nombre="Olmo blanco", especie="Ulmaceae", edad=12, altura=200, frutos=False),
    Planta(id=3, nombre="Mora china", especie="Rubus fruticosus", edad=5, altura=30, frutos=True),
    Planta(id=4, nombre="Zarzamora", especie="Rubus fruticosus", edad=8, altura=3, frutos=True),

]
    
schema = Schema(query=Query, mutation=Mutations)

class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            print(data)
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})
    
def run_server(port = 8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()
        
if __name__ == "__main__":
    run_server()