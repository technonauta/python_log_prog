MintG = int(input("Digite a quantidade de minutos: "))

if MintG<=100:
    print(f"Valor a pagar: R$50,00")
else:
    MinPag = MintG - 100
    Soma = MinPag*2
    ValPag = Soma+50
    print(f"Valor a pagar: R$ {ValPag:.2f}")