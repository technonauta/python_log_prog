Valor1=int(input("Primeiro valor: "))
Valor2=int(input("Segundo valor: "))
Valor3=int(input("Terceiro valor: "))

if Valor1<Valor2 and Valor1<Valor3:
    menor=Valor1
elif Valor2<Valor1 and Valor2<Valor3:
    menor = Valor2
else: menor = Valor3

print(f"MENOR = {menor}")