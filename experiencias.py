TesTS=int(input("Quantos casos de teste serão digitados? "))

QuaTCoB=0
QuTCoe=0
QuTRat=0
QuTSap=0
TipCoel=0
TipRato=0
TipSapo=0

for ContG in range(1,TesTS+1):
    QuantCoB=int(input("Quantidade de cobaias: "))
    TipCoB=str(input("Tipo de cobaia: "))

    QuaTCoB += QuantCoB #total de cobaias
    if TipCoB=="c": #coelhos
        TipCoel += 1
        QuTCoe += QuantCoB
    elif TipCoB=="r": #ratos
        TipRato += 1
        QuTRat += QuantCoB
    else: #sapos
        TipSapo +=1
        QuTSap += QuantCoB

PerCoe = (QuTCoe*100)/QuaTCoB
PerRat = (QuTRat*100)/QuaTCoB
PerSap = (QuTSap*100)/QuaTCoB

print("RELATÓRIO FINAL:")
print(f"Total: {QuaTCoB} cobaias")
print(f"Total de coelhos: {QuTCoe}")
print(f"Total de ratos: {QuTRat}")
print(f"Total de sapos: {QuTSap}")
print(f"Percentual de coelhos: {PerCoe:.2f}")
print(f"Percentual de ratos: {PerRat:.2f}")
print(f"Percentual de sapos: {PerSap:.2f}")