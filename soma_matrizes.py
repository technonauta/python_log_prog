NumLinH=int(input("Quantas linhas vai ter cada matriz? "))
NumCoL=int(input("Quantas colunas vai ter cada matriz? "))

MatzA=[[0 for x in range(NumCoL)] for x in range(NumLinH)]
MatzB=[[0 for x in range(NumCoL)] for x in range(NumLinH)]
MatzC=[[0 for x in range(NumCoL)] for x in range(NumLinH)]

print(f"Digite os valores da matriz A: ")
for CLinH in range(NumLinH):
    for CCoL in range(NumCoL):
        MatzA[CLinH][CCoL]=int(input(f"Elemento [{CLinH},{CCoL}]: "))

print(f"Digite os valores da matriz B: ")
for CLinH in range(NumLinH):
    for CCoL in range(NumCoL):
        MatzB[CLinH][CCoL]=int(input(f"Elemento [{CLinH},{CCoL}]: "))

for CLinH in range(NumLinH):
    for CCoL in range(NumCoL):
        MatzC[CLinH][CCoL]=MatzB[CLinH][CCoL]+MatzA[CLinH][CCoL]

print(f"MATRIZ SOMA")
for CLinH in range(NumLinH):
    for CCoL in range(NumCoL):
        print(f"{MatzC[CLinH][CCoL]}", end=" ")
    print()