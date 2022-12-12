NumEle=int(input("Quantos valores vai ter em cada vetor? "))
VetrA = [0 for x in range(NumEle)]
VetrB = [0 for x in range(NumEle)]
VetrC = [0 for x in range(NumEle)]

print(f"Digite os valores do vetor A:")
for ContG in range(NumEle):
    VetrA[ContG] = int(input())

print(f"Digite os valores do vetor B:")
for ContG in range(NumEle):
    VetrB[ContG]=int(input())

for ContG in range(NumEle):
    VetrC[ContG]=VetrA[ContG]+VetrB[ContG]

print(f"VETOR RESULTANTE:")
for ContG in range(NumEle):
    print(f"{VetrC[ContG]}")
