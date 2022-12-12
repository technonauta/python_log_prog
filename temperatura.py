EscaL=input("Você vai digitar em qual escala (C/F)? ")

if EscaL=="F":
    TempF=float(input("Digite a temperatura em Fahrenheit: "))
    EqVCel=(5/9)*(TempF-32)
    print(f"Temperatura equivalente em Celsius: {EqVCel:.2f}")
else:
    TempC=float(input("Digite a temperatura em Celsius: "))
    EqVFar=TempC*(9/5)+32
    print(f"Temperatura equivalente em Fahrenheit: {EqVFar:.2f}")