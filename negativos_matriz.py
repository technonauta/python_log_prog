NumLin=int(input("Qual a quantidade de linhas da matriz? "))
NumCol=int(input("Qual a quantidade de colunas da matriz? "))

MatZ=[[0 for x in range(NumCol)] for x in range(NumLin)]

for CLin in range(NumLin):
    for CCol in range(NumCol):
        MatZ[CLin][CCol]=int(input(f"Elemento [{CLin},{CCol}]: "))

print(f"VALORES NEGATIVOS")
for CLin in range(NumLin):
    for CCol in range(NumCol):
        if MatZ[CLin][CCol]<0:
            print(f"{MatZ[CLin][CCol]}")