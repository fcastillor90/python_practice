inversion = float(input("Ingrese cantidad a invertir : "))
interes = 0.04
año1 = (inversion*(1+interes))
print("Cantidad año 1 : " + str(round(año1,2)))
año2 = (año1*(1+interes))
print("Cantidad año 2 : "+ str(round(año2,2)))
año3 = (año2*(1+interes))
print("Cantidad año 3 : "+ str(round(año3,2)))