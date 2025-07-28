x= int(input("cual es tu edad?:"))
print(x)

if x >= 18 and x <= 65 :
    print("Descuento de 5%")
elif x <= 17:
    print("Debe ser mayor de edad para realizar la compra")
elif x >= 66 and x <= 100:
    print("Descuento del 15%")
else:
    print("Ingrese un dato valido")
    