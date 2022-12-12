NumInt=int(input("Quantas pessoas serão digitadas? "))
VetAlt=[0 for x in range(NumInt)]
VetGen=[0 for x in range(NumInt)]

for ContG in range(NumInt):
    VetAlt[ContG]=float(input(f"Altura da {ContG+1}ª pessoa "))
    VetGen[ContG]=str(input(f"Gênero da {ContG+1}ª pessoa "))

MaiAlt=VetAlt[0]
MerAlt=VetAlt[0]
for ContG in range(NumInt): #maior altura/menor altura
    if VetAlt[ContG]>MaiAlt:
        MaiAlt=VetAlt[ContG]
        
    if VetAlt[ContG]<MerAlt:
        MerAlt=VetAlt[ContG]

NumFem=0
AltFem=0
NumMas=0
for ContG in range(NumInt): #media mulheres/número homens
    if VetGen[ContG]=="f":
        NumFem +=1
        AltFem +=VetAlt[ContG]
    else:
        NumMas +=1

MedFem=AltFem/NumFem

print(f"Menor altura: {MerAlt:.2f}")
print(f"Maior altura: {MaiAlt:.2f}")
print(f"Média da altura das mulheres: {MedFem:.2f}")
print(f"Número de homens = {NumMas}")