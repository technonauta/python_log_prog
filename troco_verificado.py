PrecUnt = float(input("Preço unitário do produto: "))
QuantCo = int(input("Quantidade comprada: "))
DinRec = float(input("Dinheiro recebido: "))

Comp = PrecUnt*QuantCo
TroC = DinRec - Comp

if DinRec>=Comp:
    print(f"TROCO = {TroC:.2f}")
else:
    Falt = Comp-DinRec
    print(f"DINHEIRO INSUFICIENTE. FALTAM {Falt:.2f} REAIS")    