import xmlrpc.client


server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Operaciones para la calculadora que se usaran
print("Suma (5 + 3):", server.add(5, 3))
print("Resta (5 - 3):", server.subtract(5, 3))
print("Multiplicación (5 * 3):", server.multiply(5, 3))
print("División (5 / 3):", server.divide(5, 3))
print("División (5 / 0):", server.divide(5, 0))
