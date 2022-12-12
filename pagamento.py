nome1 = input("Nome: ")
valorH = float(input("Valor por hora: "))
horaT = float(input("Horas trabalhadas: "))

PagT = horaT*valorH

print(f"O pagamento para {nome1} deve ser {PagT:.2f}")