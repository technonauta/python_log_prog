nome1 = input("Dados da primeira pessoa: ")
idade1 = float(input("Idade da primeira pessoa: "))

nome2 = input("Dados da segunda pessoa: ")
idade2 = float(input("Idade da segunda pessoa: "))

media = 0
media = (idade1 + idade2)/2

print(f"A idade média de {nome1} e {nome2} é de {media:.1f} anos")