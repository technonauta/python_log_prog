print(f"Digite dois números: ")
ValRX=int(input())
ValRY=int(input())

if ValRX>ValRY:
    receb=ValRY
    ValRY=ValRX
    ValRX=receb

soma=0;
for icont in range(ValRX+1, ValRY):
    if icont % 2 != 0:
        soma = soma + icont

print(f"SOMA DOS IMPARES= {soma}")