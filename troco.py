PreUn = float(input("Preço unitário do produto: "))
QuanC = int(input("Quantidade comprada: "))
DinRec = float(input("Dinheiro recebido: "))

PagT=0
TrocO=0
PagT = PreUn * QuanC
TrocO = DinRec - PagT

print(f"TROCO = {TrocO:.2f}")