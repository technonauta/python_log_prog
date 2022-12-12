NumInt=int(input("Quantas pessoas você vai digitar? "))
VetNom =[0 for contX in range(NumInt)]
VetIdd =[0 for contX in range(NumInt)]

for ContG in range(NumInt):
    print(f"Dados da {ContG+1}ª pessoa")
    VetNom[ContG]=str(input("Nome: "))
    VetIdd[ContG]=int(input("Idade: "))

IddPes=VetIdd[0]
PesVel=0
for ContG in range(NumInt):
    if VetIdd[ContG]>IddPes:
        IddPes=VetIdd[ContG]
        PesVel=ContG

print(f"PESSOA MAIS VELHA: {VetNom[PesVel]}")