router=[]
switch=[]
computadora=[]
accessPoint=[]
telefonos=[]
FW=[]
IPT=[]
lista = ["R1","R2","R3","R4","S1","S2",
         "S3", "AP1","AP2","AP3","FW1","FW2",
         "PC1","PC2","PC3","IPT1","IPT2","IP3","Tlf1","Tlf2","Tlf3",]
for item in lista:
    if "R" in item:
        router.append(item)
    elif "S" in item:
        switch.append(item)
    elif "PC" in item:
        computadora.append(item)
    elif "A" in item:
        accessPoint.append(item)
    elif "Tl" in item:
        telefonos.append(item)
    elif "F" in item:
        FW.append(item)
    elif "IPT" in item:
        IPT.append(item)
print(router)
print(switch)
print(computadora)
print(accessPoint)
print(telefonos)
print(FW)
print(IPT)