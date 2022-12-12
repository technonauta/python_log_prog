import math

CoefA = float(input("Coeficiente a: "))
CoefB = float(input("Coeficiente b: "))
CoefC = float(input("Coeficiente c: "))

raiz = math.sqrt((CoefB**2)-(4*CoefA*CoefC))

ResulX1 = (-CoefB-raiz)/(2*CoefA)
ResulX2 = (-CoefB+raiz)/(2*CoefA)

print(f"X1 = {ResulX1:.4f}")
print(f"X2 = {ResulX2:.4f}")