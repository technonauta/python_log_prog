NumS=int(input("Quantos números você vai digitar? "))

for contG in range(NumS):
    ValrX=int(input("Digite um número: "))

    if ValrX==0:
        print(f"NULO")
    elif ValrX>0 and ValrX%2==0:    
        print(f"PAR POSITIVO")
    elif ValrX<0 and ValrX%2==0:    
        print(f"PAR NEGATIVO")
    elif ValrX>0 and ValrX%2!=0:    
        print(f"IMPAR POSITIVO")
    else:    
        print(f"IMPAR NEGATIVO")