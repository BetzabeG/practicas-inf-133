from http.server import HTTPServer, BaseHTTPRequestHandler
import json

animales = {}

class Animal:
    def __init__(self, animal_type, nombre,genero, edad, peso ):
        self.animal_type = animal_type
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.peso = peso
        
class Mamifero(Animal):
    def __init__(self, nombre,genero, edad, peso):
        super().__init__("mamifero", nombre,genero, edad, peso)

class Ave(Animal):
    def __init__(self, nombre,genero, edad, peso):
        super().__init__("ave", nombre,genero, edad, peso)
        
class Reptil(Animal):
    def __init__(self, nombre,genero, edad, peso):
        super().__init__("reptil", nombre,genero, edad, peso)
        
class Anfibio(Animal):
    def __init__(self, nombre,genero, edad, peso):
        super().__init__("anfibio", nombre,genero, edad, peso)
        
class Pez(Animal):
    def __init__(self, nombre,genero, edad, peso):
        super().__init__("pez", nombre,genero, edad, peso)
        
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, nombre, genero, edad, peso):
        if animal_type == "mamifero":
            return Mamifero(nombre, genero, edad, peso)
        elif animal_type == "ave":
            return Ave(nombre, genero, edad, peso)
        elif animal_type == "reptil":
            return Reptil(nombre, genero, edad, peso)
        elif animal_type == "anfibio":
            return Anfibio(nombre, genero, edad, peso)
        elif animal_type == "pez":
            return Pez(nombre, genero, edad, peso)
        else:
            raise ValueError("Tipo de animal de entrega no valido")
        
class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))
        
    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))
    
class AnimalService:
    def __init__(self):
        self.factory = AnimalFactory()
        
    def add_animal(self, data):
        animal_type = data.get("animal_type", None)
        nombre = data.get("nombre", None)
        genero = data.get("genero", None)
        edad = data.get("edad", None)
        peso = data.get("peso", None)
        
        service_animal = self.factory.create_animal(
            animal_type,nombre, genero, edad, peso
        )
        animales[len(animales)+1] = service_animal
        return service_animal
    
    def list_animales(self):
        return {index: animal.__dict__ for index, animal in animales.items()}
    
    def buscar_por_atributo(self, atributo, parametro):
        if atributo in parametro:
            query = parametro[atributo][0]
        elif query:
            if(atributo)=="especie":
                return {index: animal.__dict__ for index, animal in animales.items()}
            elif(atributo)=="genero":
                return {index: animal.__dict__ for index, animal in animales.items()}
        else:
            return None
                

        
    
    def update_animal(self, animal_id, data):
        if animal_id in animales:
            animal = animales[animal_id]
            animal_type = data.get("animal_type", None)
            nombre = data.get("nombre", None)
            genero = data.get("genero", None)
            edad = data.get("edad", None)
            peso = data.get("peso", None)
            if animal_type:
                animal.animal_type = animal_type
            if nombre:
                animal.nombre =  nombre
            if genero:
                animal.nombre =  genero
            if edad:
                animal.edad = edad
            if peso:
                animal.peso = peso
            return animal
        else:
            raise None
        
    def delete_animal(self, animal_id):
        if animal_id in animales:
            del animales[animal_id]
            return {"Message": "Animal eliminado"}
        else:
            return None

class AnimalRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.animal_service = AnimalService()
        super().__init__(*args, **kwargs)
        
    def do_POST(self):
        if self.path == "/animales":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.animal_service.add_animal(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"Message": "Ruta no encontrada"}
            )
            
    def do_GET(self):
        if self.path == "/animales":
            response_data = self.animal_service.list_animales()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Message": "Ruta no encontrada"})
            
    def do_PUT(self):
        if self.path.startswith("/animales/"):
            animal_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.animal_service.update_animal(animal_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(self, 404, {"Messagge": "animal no encontrado"})        
        else:
            HTTPDataHandler.handle_response(self, 404, {"Message": "Ruta no encontrada"})
            
    def do_DELETE(self):
        if self.path.startswith("/animales/"):
            animal_id = int(self.path.split("/")[-1])
            response_data = self.animal_service.delete_animal(animal_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(self, 404, {"message": "Animal no encontrado"})
        else:
            HTTPDataHandler.handle_response(self, 404, {"Message": "Ruta no encontrada"})
            
def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, AnimalRequestHandler)
        print("Iniciando el servidor http en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()
        
if __name__ == "__main__":
    main()