CodG=float(input("Código do produto: "))
QuanT=float(input("Quantidade Comprada: "))
'tabela'
CodG1=5.00
CodG2=3.50
CodG3=4.80
CodG4=8.90
CodG5=7.32

if CodG == 1:
    ValR = QuanT*CodG1
elif CodG == 2:
    ValR = QuanT*CodG2
elif CodG == 3:
    ValR = QuanT*CodG3
elif CodG == 4:
    ValR = QuanT*CodG4
else:
    ValR = QuanT*CodG5

print(f"Valor a pagar: R$ {ValR:.2f}")
