NumOrd=int(input("Qual a ordem da matriz? "))
MatZ=[[0 for x in range(NumOrd)] for x in range(NumOrd)]

for CLinH in range(NumOrd):
    for CCoL in range(NumOrd):
        MatZ[CLinH][CCoL]=int(input(f"Elemento [{CLinH},{CCoL}]: "))

print(f"MAIOR ELEMENTO DE CADA LINHA: ")

for CLinH in range(NumOrd):
    LinElm=0
    for CCoL in range(NumOrd):
        if LinElm<MatZ[CLinH][CCoL]:
            LinElm=MatZ[CLinH][CCoL]
    print(f"{LinElm}")