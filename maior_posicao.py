NumRea = int(input("Quantos números você vai digitar? "))
VetR = [0 for x in range(NumRea)]

for ContG in range(0,NumRea):
    VetR[ContG]=float(input("Digite um número: "))

MairNum=VetR[0]
PosC=0

for ContG in range(0,NumRea):
    if VetR[ContG]>MairNum:
        MairNum=VetR[ContG]
        PosC=ContG

print(f"\nMAIOR VALOR = {MairNum:.1f}")
print(f"POSIÇÃO DO MAIOR VALOR = {PosC}")