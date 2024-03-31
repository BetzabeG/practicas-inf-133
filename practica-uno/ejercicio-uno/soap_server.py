from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

# Realizamos la funcion para la operacion de la suma
def suma(num1, num2):
    return num1 + num2

# Creamos la ruta del servidor SOAP
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location = "http://localhost:8000/",
    action = "http://localhost:8000/",
    namespace = "http://localhost:8000/",
    trace = True,
    ns = True,
)

# Registramos la operacion de la suma
dispatcher.register_function(
    "Suma",
    suma,
    returns = {"resultado: ": int},
    args = {"num1": int, "num2":int}
)

# Iniciamos el servidor HTTP
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciando en http://localhost:8000/")
server.serve_forever()