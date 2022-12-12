NumInt=int(input("Quantos elementos vai ter o vetor? "))
VetR=[0 for x in range(NumInt)]

for ContG in range(NumInt):
    VetR[ContG]=int(input("Digite um número: "))

SomaArt=0
contGM=0
for ContG in range(NumInt):
    if VetR[ContG]%2==0:
        SomaArt += VetR[ContG]
        contGM += 1

if contGM == 0:
    print("NENHUM NÚMERO PAR")
else:
    MediA=float(SomaArt)/contGM
    print(f"MÉDIA DOS NÚMEROS PARES = {MediA:.1f}")