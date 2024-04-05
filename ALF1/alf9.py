cantidad = float(input("Ingrese cantidad a invertir :"))
interes = float(input("Ingrese el interes anual :"))
años = float(input("Ingrese la cantidad de años :"))

print("capital final: "+ str(round(cantidad*(interes/100 + 1)** años,2)))