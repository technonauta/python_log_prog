NumInt=int(input("Quantos alunos serão digitados? "))
VetNom=[0 for x in range(NumInt)]
VetN1=[0 for x in range(NumInt)]
VetN2=[0 for x in range(NumInt)]
MediA=[0 for x in range(NumInt)]

for ContG in range(NumInt):
    print(f"Digite nome, primeira e segunda nota do {ContG+1}ª aluno:")
    VetNom[ContG]=str(input())
    VetN1[ContG]=float(input())
    VetN2[ContG]=float(input())

for ContG in range(NumInt):
    MediA[ContG]=(VetN1[ContG]+VetN2[ContG])/2

print(f"\nAlunos Aprovados:")
for ContG in range(NumInt):
    if MediA[ContG]>=6:
        print(f"{VetNom[ContG]}")