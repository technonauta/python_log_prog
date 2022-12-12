ValoN=int(input("Quantos casos você vai digitar? "))

for contG in range(ValoN):
    NumR=int(input("Entre com o numerador: "))
    DenR=int(input("Entre com o denominador: "))

    if DenR==0:
        print(f"DIVISÃO IMPOSSÍVEL")
    else:
        ResDiv=NumR/DenR
        print(f"{ResDiv:.2f}")