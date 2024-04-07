from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from urllib.parse import urlparse, parse_qs

pacientes = [
    
    {
        "ci": 1,
        "nombre": "Fernando",
        "apellido": "Garcia",
        "edad": 25,
        "genero": "Masculino",
        "diagnostico": "Diabetes",
        "doctor": "Pedro Ramos",
    },
    {
        "ci": 2,
        "nombre": "Maria",
        "apellido": "Lopez",
        "edad": 35,
        "genero": "Femenino",
        "diagnostico": "Hipertension",
        "doctor": "Pedro Perez",
    },
]

class PacientesService:
    @staticmethod
    def find_pacient(ci):
        return next(
            (paciente for paciente in pacientes if paciente["ci"]==ci),
            None,
        )
        
    ###
    @staticmethod
    def filter_pacients_by_diagnostico(diagnostico):
        return[
            paciente for paciente in pacientes if paciente["diagnostico"] == diagnostico
        ]
    
    @staticmethod
    def filter_pacients_by_doctor(doctor):
        return[paciente for paciente in pacientes if paciente["doctor"]==doctor]
    
    @staticmethod
    def add_pacient(data):
        data["ci"] = len(pacientes) + 1
        pacientes.append(data)
        return pacientes

    @staticmethod
    def update_pacient(ci, data):
        paciente = PacientesService.find_pacient(ci)
        if paciente:
            paciente.update(data)
            return pacientes
        else:
            return None
        
    @staticmethod
    def delete_pacients():
        pacientes.clear()
        return pacientes
    
class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Conten-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))
        
class RESTRequestHandler(BaseHTTPRequestHandler):
    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data
    # Crear un paciente
    def do_POST(self):
        if self.path == "/pacientes":
            data = self.read_data()
            pacientes = PacientesService.add_pacient(data)
            HTTPResponseHandler.handle_response(self, 201, pacientes)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        # listar todos los pacientes
        if parsed_path.path == "/pacientes" and "diagnostico" not in query_params and "doctor" not in query_params: 
            HTTPResponseHandler.handle_response(self, 200, pacientes)      
        # buscar pacientes por ci
        elif self.path.startswith("/pacientes/"):
            try:
                ci = int(self.path.split("/")[-1])
                paciente = PacientesService.find_pacient(ci)
                if paciente:
                    HTTPResponseHandler.handle_response(self, 200, [paciente])
                else:
                    HTTPResponseHandler.handle_response(self, 404, {"Error": "Paciente no encontrado"})
            except ValueError:
                HTTPResponseHandler.handle_response(self, 400, {"Error": "ci de paciente no valido"})
            
        # Listar a los pacientes que tienen diagnostico de `Diabetes`
        elif parsed_path.path == "/pacientes":
            if "diagnostico" in query_params:
                diagnostico = query_params["diagnostico"][0]
                pacientes_filtrados_diagnostico = PacientesService.filter_pacients_by_diagnostico(
                    diagnostico
                )
                if pacientes_filtrados_diagnostico:
                    HTTPResponseHandler.handle_response(
                        self, 200, pacientes_filtrados_diagnostico
                    )
                else:
                    HTTPResponseHandler.handle_response(self, 204, [])

            # Listar a los pacientes que atiende el Doctor `Pedro Perez`
            elif "doctor" in query_params:
                doctor = query_params["doctor"][0]
                pacientes_filtrados_doctor = PacientesService.filter_pacients_by_doctor(doctor)
                if pacientes_filtrados_doctor:
                    HTTPResponseHandler.handle_response(
                        self, 200, pacientes_filtrados_doctor
                    )
                else:
                    HTTPResponseHandler.handle_response(self, 204, [])
            else:
                HTTPResponseHandler.handle_response(self, 204, [])       
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )
    # Actualizar la información de un paciente
    def do_PUT(self):
        if self.path.startswith("/pacientes/"):
            ci = int(self.path.split("/")[-1])
            data = self.read_data()
            pacientes = PacientesService.update_pacient(ci, data)
            if pacientes:
                HTTPResponseHandler.handle_response(self, 200, pacientes)
            else:
                HTTPResponseHandler.handle_response(
                    self, 404, {"Error":"Paciente no encontrado"}
                )
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error":"Ruta no existenete"}
            )

    def do_DELETE(self):
        if self.path.startswith("/pacientes/"):
            ci = int(self.path.split("/")[-1])
            paciente = PacientesService.find_pacient(ci)
            if paciente:
                pacientes.remove(paciente)
                HTTPResponseHandler.handle_response(self, 200, paciente)
            else:
                HTTPResponseHandler.handle_response(self, 404, {"error": "Paciente no encontrado"})
        else:
            HTTPResponseHandler.handle_response(self, 400, {"error": "Ruta no existente"})

    
    
            
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
            
        
        