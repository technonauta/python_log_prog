NumN = int(input("Qual a ordem da matriz? "))

MatrZN = [[0 for x in range(NumN)] for x in range(NumN)]

for IntI in range(NumN):
    for IntJ in range(NumN):
        MatrZN[IntI][IntJ] = int(input(f"Elemento [{IntI},{IntJ}]: "))

print(f"DIAGONAL PRINCIPAL: ")
for IntI in range(NumN):
    print(f"{MatrZN[IntI][IntI]}", end=" ")

quant=0
for IntI in range(NumN):
    for IntJ in range(NumN):
            if MatrZN[IntI][IntJ]<0:
                quant += 1

print(f"\nQUANTIDADE DE NEGATIVOS: {quant}")