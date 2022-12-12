nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

notaF = nota1+nota2

print(f"NOTA FINAL = {notaF:.1f}")

if notaF<60:
    print(f"REPROVADO")