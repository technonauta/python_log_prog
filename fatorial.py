NumerO = int(input("Digite o valor de N: ") )

FatoR=1
for contG in range(1,NumerO+1):
    FatoR *= contG     # == FatoR = FatoR * contG

print(f"Fatorial de: {FatoR}")