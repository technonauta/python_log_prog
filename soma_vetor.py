QtNum=int(input("Quantos números você vai digitar? "))

VetR=[0 for contX in range(QtNum)]

for ContG in range(QtNum):
    VetR[ContG]=float(input("Digite um número: "))

Soma=0
for ContG in range(QtNum):    
    Soma += VetR[ContG]

Med=Soma/QtNum

print(f"\nVALORES = ", end="")
for ContG in range(QtNum):
    print(f"{VetR[ContG]:.1f} ", end="")

print(f"\nSOMA = {Soma:.2f} ")
print(f"MEDIA = {Med:.2f} ")