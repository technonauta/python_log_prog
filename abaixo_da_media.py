NumInt=int(input("Quantos elementos vai ter o vetor? "))
VetrNR=[0 for x in range(NumInt)]

for ContG in range(NumInt):
    VetrNR[ContG]=float(input("Digite um número: "))

AritM=0
for ContG in range(NumInt):
    AritM += VetrNR[ContG]

MediA=AritM/NumInt

print(f"\nMEDIA DO VETOR = {MediA:.3f}")
print(f"ELEMENTOS ABAIXO DA MEDIA: ")

for ContG in range(NumInt):
    if VetrNR[ContG] < MediA:
        print(f"{VetrNR[ContG]:.1f}")