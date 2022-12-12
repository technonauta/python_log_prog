import math
NumOrd=int(input("Qual a ordem da matriz? "))
MatZ=[[0 for x in range(NumOrd)] for x in range(NumOrd)]

for CLiH in range(NumOrd):
    for CCoL in range(NumOrd):
        MatZ[CLiH][CCoL]=float(input(f"Elemento [{CLiH},{CCoL}]: "))

#SOMA DOS POSITIVOS
SomPos=0
for CLiH in range(NumOrd):
    for CCoL in range(NumOrd):
        if MatZ[CLiH][CCoL]>0:
            SomPos += MatZ[CLiH][CCoL]
print(f"\nSOMA DOS POSITIVOS: {SomPos}")

#ÍNDICE LINHA
EscLH=int(input("\n\nEscolha uma linha:"))
print(f"LINHA ESCOLHIDA: ")
for CLiH in range(NumOrd):
    print(f"{MatZ[EscLH][CLiH]}", end=" ")

#ÍNDICE COLUNA
EscLH=int(input("\n\nEscolha uma coluna: "))
print(f"COLUNA ESCOLHIDA: ")
for CLiH in range(NumOrd):
    print(f"{MatZ[CLiH][EscLH]}", end=" ")

#DIAGONAL PRINCIPAL
print(f"\n\nDIAGONAL PRINCIPAL: ")
for CLiH in range(NumOrd):
    for CCoL in range(NumOrd):
        if CLiH ==CCoL:
            print(f"{MatZ[CLiH][CCoL]}", end=" ")

#MATRIZ ALTERADA
for CLiH in range(NumOrd):
    for CCoL in range(NumOrd):
        if MatZ[CLiH][CCoL]<0:
            MatZ[CLiH][CCoL]=math.pow(MatZ[CLiH][CCoL], 2);

print(f"\n\nMATRIZ ALTERADA: ")
for CLiH in range(NumOrd):
    for CCoL in range(NumOrd):
        print(f"{MatZ[CLiH][CCoL]}", end=" ")
    print()

