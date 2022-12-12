codg1=int(input("Informe um código (1,2,3) ou 4 para parar: "))

gas=0
alc=0
die=0

while codg1!=4:
    if codg1==1:
        alc=alc+1
    elif codg1==2:
        gas=gas+1
    elif codg1==3:
        die=die+1
    codg1=int(input("Informe um código (1,2,3) ou 4 para parar: "))

print("MUITO OBRIGADO")
print(f"Alcool: {alc}")
print(f"Gasolina: {gas}")
print(f"Diesel: {die}")