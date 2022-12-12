NumInt = int(input("Quantos números você vai digitar? "))
VetR= [0 for contX in range(NumInt)]

for ContG in range(0,NumInt):
    VetR[ContG] = int(input("Digite um número: "))

print()
print("Números Negativos:")
for ContG in range(0,NumInt):
    if VetR[ContG]<0:
        print(f"{VetR[ContG]}")
