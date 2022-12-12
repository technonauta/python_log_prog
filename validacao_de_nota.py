Nota1=float(input("Digite a primeira nota: "))

while (Nota1<0) or (Nota1>10):
    Nota1=float(input("Valor Inválido! Tente Novamente: "))

Nota2=float(input("Digite a segunda nota: "))

while (Nota2<0) or (Nota2>10):
    Nota2=float(input("Valor Inválido! Tente Novamente: "))

MediA=(Nota1+Nota2)/2
print(f"MEDIA = {MediA:.2f}")