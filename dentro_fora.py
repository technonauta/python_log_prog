ValrN=int(input("Quantos números você vai digitar? "))

dentro=0
fora=0

for icont in range(ValrN):
    ValrX=int(input("Digite um número: "))

    if ValrX < 10 or ValrX > 20:
        fora = fora + 1
    else:
        dentro = dentro + 1

print(f"{dentro} DENTRO")
print(f"{fora} FORA")