MedGli = float(input("Digite a medida da glicose: "))

if MedGli<=100:
    print(f"Classificado: normal")
elif MedGli>100 and MedGli<=140:
    print(f"Classificado: elevado")
else:
    print(f"Classificado: diabetes")