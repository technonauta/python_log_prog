AreaT = 0
ValM = 0
Larg = float(input("Digite a largura do terreno: "))
Comp = float(input("Digite o comprimento do terreno: "))
Val = float(input("Digite o valor do metro quadrado: "))

AreaT = Larg * Comp  
ValM = AreaT * Val

print(f"Area do terreno= {AreaT:.2f}")
print(f"Valor do terreno= {ValM:.2f}")