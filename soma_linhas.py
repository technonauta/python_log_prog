NumLin=int(input("Qual a quantidade de linhas da matriz? "))
NumCol=int(input("Qual a quantidade de colunas da matriz? "))

MatrZ=[[0 for x in range(NumCol)] for x in range(NumLin)]
VetR=[0 for x in range(NumLin)]

for ContLin in range(NumLin):
    print(f"Digite os elementos da {ContLin+1}ª linha: ")
    for ContCol in range(NumCol):
        MatrZ[ContLin][ContCol] = float(input())

for ContLin in range(NumLin):
    somalinha=0
    for ContCol in range(NumCol):
        somalinha += MatrZ[ContLin][ContCol]
    VetR[ContLin] = somalinha

print(f"VETOR GERADO")
for ContLin in range(NumLin):
    print(f"{VetR[ContLin]:.1f}")