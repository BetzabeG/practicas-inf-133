from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

mensajes = {}

class MensajesService:
    @staticmethod
    def create_mensaje(contenido):
        id = len(mensajes)+1
        mensaje_encriptado = encriptar_mensaje(contenido)
        mensajes[id] = {
            "id": id,
            "contenido": contenido,
            "contenido_encriptado":mensaje_encriptado
        }
        return mensajes[id]

    @staticmethod
    def listar_mensajes():
        return list(mensajes.values())

    @staticmethod
    def find_mensaje(id):
        if id in mensajes:
            return mensajes[id]
        else:
            return None

    @staticmethod
    def update_mensaje(id, contenido):
        if id in mensajes:
            mensaje_encriptado = encriptar_mensaje(contenido)
            mensajes[id]["contenido"] = contenido
            mensajes[id]["contenido_encriptado"] = mensaje_encriptado
            return mensajes[id]
        else:
            return None

    @staticmethod
    def delete_mensaje(id):
        if id in mensajes:
            del mensajes[id]
            return True
        else:
            return False

def encriptar_mensaje(contenido):
    resultado =""
    for char in contenido:
        if char.isalpha():
            codigo_ascii = ord(char.lower())+3
            if codigo_ascii > ord('z'):
                codigo_ascii = codigo_ascii - 26
            resultado = resultado + chr(codigo_ascii)
        else:
            resultado = resultado+ char
    return resultado

class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == "/mensajes":
            mensajes_listados = MensajesService.listar_mensajes()
            HTTPResponseHandler.handle_response(self, 200, mensajes_listados)
        elif parsed_path.path.startswith("/mensajes/"):
            id = int(parsed_path.path.split("/")[-1])
            mensaje = MensajesService.find_mensaje(id)
            if mensaje:
                HTTPResponseHandler.handle_response(self, 200, [mensaje])
            else:
                HTTPResponseHandler.handle_response(self, 404, {"Error": "Mensaje no encontrado"})
        else:
            HTTPResponseHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_POST(self):
        if self.path == "/mensajes":
            data = self.read_data()
            nuevo_mensaje = MensajesService.create_mensaje(data["contenido"])
            HTTPResponseHandler.handle_response(self, 201, nuevo_mensaje)
        else:
            HTTPResponseHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_PUT(self):
        if self.path.startswith("/mensajes/"):
            id = int(self.path.split("/")[-1])
            data = self.read_data()
            mensaje_actualizado = MensajesService.update_mensaje(id, data["contenido"])
            if mensaje_actualizado:
                HTTPResponseHandler.handle_response(self, 200, mensaje_actualizado)
            else:
                HTTPResponseHandler.handle_response(self, 404, {"Error": "Mensaje no encontrado"})
        else:
            HTTPResponseHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_DELETE(self):
        if self.path.startswith("/mensajes/"):
            id = int(self.path.split("/")[-1])
            if MensajesService.delete_mensaje(id):
                HTTPResponseHandler.handle_response(self, 200, {"mensaje": "Mensaje eliminado"})
            else:
                HTTPResponseHandler.handle_response(self, 404, {"Error": "Mensaje no encontrado"})
        else:
            HTTPResponseHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data

def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()

if __name__ == "__main__":
    run_server()