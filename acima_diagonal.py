NumOrd=int(input("Qual a ordem da matriz? "))

MatZ=[[0 for x in range(NumOrd)] for x in range(NumOrd)]

for CLinH in range(NumOrd):
    for CCoL in range(NumOrd):
        MatZ[CLinH][CCoL]=int(input(f"Elemento [{CLinH},{CCoL}]: "))

somadiag=0
for CLinH in range(NumOrd):
    for CCoL in range(NumOrd):
        if CLinH<CCoL:
            somadiag += MatZ[CLinH][CCoL]

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {somadiag}")