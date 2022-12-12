SalR=float(input("Digite o salário da pessoa: "))

'tabela'
Poc1=20
Poc2=15
Poc3=10
Poc4=5

if SalR<=1000.00:
    Aum=(SalR*Poc1)/100
    NovSal= SalR+Aum
    Poc=Poc1

elif (SalR>1000.00) and (SalR<=3000.00):
    Aum=(SalR*Poc2)/100
    NovSal= SalR+Aum
    Poc=Poc2

elif (SalR>3000.00) and (SalR<=8000.00):
    Aum=(SalR*Poc3)/100
    NovSal= SalR+Aum
    Poc=Poc3

else :
    Aum=(SalR*Poc4)/100
    NovSal= SalR+Aum
    Poc=Poc4

print(f"Novo Salário = R$ {NovSal:.2f}")
print(f"Aumento = R$ {Aum:.2f}")
print(f"Porcentagem = {Poc:.2f}%")