import math
Area = 0
Perim = 0
Diag = 0

Bas = float(input("Base do retangulo= "))
Alt = float(input("Altura do retangulo= "))

Area = Bas * Alt
Perim = 2*(Bas+Alt)
Diag = math.sqrt((Bas ** 2) + (Alt ** 2))

print(f"Area = {Area:.4f}")
print(f"Perimetro = {Perim:.4f}")
print(f"Diagonal = {Diag:.4f}")
