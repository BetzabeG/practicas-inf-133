from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import random

class Game:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.partidas = []
        return cls._instance

    def crear_partida(self, elemento_jugador):
        elemento_servidor = random.choice(["piedra", "papel", "tijera"])
        resultado = self.calcular_resultado(elemento_jugador, elemento_servidor)
        partida = {
            "id": len(self.partidas) + 1,
            "elemento_juador": elemento_jugador,
            "elemento_servidor": elemento_servidor,
            "resultado": resultado
        }
        self.partidas.append(partida)
        return partida

    def calcular_resultado(self, elemento_jugador, elemento_servidor):
        if elemento_jugador == elemento_servidor:
            return "empate"
        elif (
            (elemento_jugador == "piedra" and elemento_servidor == "tijera") or
            (elemento_jugador == "papel" and elemento_servidor == "piedra") or
            (elemento_jugador == "tijera" and elemento_servidor == "papel")):
            return "gano"
        else:
            return "perdio"

    def obtener_partidas(self):
        return self.partidas

    def partidas_perdidas(self):
        return [partida for partida in self.partidas if partida["resultado"] == "perdio"]

    def partidas_ganadas(self):
        return [partida for partida in self.partidas if partida["resultado"] == "gano"]

class GameHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/partidas":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode("utf-8"))
            game = Game()
            partida = game.crear_partida(data["elemento"])
            self.send_response(201)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(partida).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        game = Game()
        if self.path == "/partidas":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(game.obtener_partidas()).encode("utf-8"))
        elif self.path.startswith("/partidas?resultado="):
            resultado = self.path.split("=")[1]
            if resultado =="gano":
                partidas = game.partidas_ganadas()
            elif resultado == "perdio":
                partidas = game.partidas_perdidas()
            else:
                self.send_response(400)
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(partidas).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def main():
    try:
        server_address = ("",8000)
        httpd = HTTPServer(server_address, GameHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()
if __name__ == "__main__":
    main()