from xmlrpc.server import SimpleXMLRPCServer

# Operaciones de calculadora
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: División por cero"
        return x / y



# Iniciando el servidor XML-RPC en el puerto 8000.
server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor corriendo en http://localhost:8000/")

server.register_instance(Calculator())


server.serve_forever()
