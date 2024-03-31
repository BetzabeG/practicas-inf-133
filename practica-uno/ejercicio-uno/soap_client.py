from zeep import Client
client = Client('http://localhost:8000/')

result_Suma = client.service.SumaDosNumeros(num1=12, num2=6)
print("Operacion de la suma de dos numeros enteros")
print(f"La suma de 12 y 6 es: {result_Suma}")

result_Resta = client.service.RestaDosNumeros(num1=24, num2=7)
print("\nOperacion de la resta de dos numeros enteros")
print(f"La resta de 24 - 7 es: {result_Resta}")

result_Multiplicacion = client.service.MultiplicacionDosNumeros(num1=12, num2=4)
print("\nOperacion de la multiplicacion de dos numeros enteros")
print(f"La multiplicacion de 12 * 4 es: {result_Multiplicacion}")

result_Division = client.service.DivisionDosNumeros(num1=48, num2=4)
print("\nOperacion de la divicion de dos numeros enteros")
print(f"La division de 48 entre 4 es: {result_Division}")