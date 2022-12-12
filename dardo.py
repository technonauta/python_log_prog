Dard1 = float(input("Digite as três distâncias: "))
Dard2 = float(input())
Dard3 = float(input())

if Dard1>Dard2 and Dard1>Dard3:
    print(f"MAIOR DISTÂNCIA = {Dard1}")
elif Dard2>Dard3 and Dard2>Dard1:
    print(f"MAIOR DISTÂNCIA = {Dard2}")
else:
    print(f"MAIOR DISTÂNCIA = {Dard3}")