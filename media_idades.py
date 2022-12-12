IdaD=int(input("Digite as idades: "))

if IdaD<0:
    print(f"IMPOSSÍVEL CALCULAR")    

else:
    soma=0
    cont=0
    while IdaD > 0:
        soma = soma+IdaD
        cont = cont+1
        IdaD=int(input(""))

    Med=soma/cont
    print(f"MEDIA = {Med:.2f}")