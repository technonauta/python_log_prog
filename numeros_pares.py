NumInt=int(input("Quantos números você vai digitar? "))
VetR=[0 for x in range(NumInt)]

for ContG in range(NumInt):
    VetR[ContG]=int(input("Digite um número: "))

print(f"\nNÚMEROS PARES:")

QutPar=0
for ContG in range(NumInt):
    if VetR[ContG]%2==0:
        print(f"{VetR[ContG]}",end=" ")
        QutPar +=1
 
print(f"\n\nQUANTIDADE DE PARES: {QutPar}")