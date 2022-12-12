NumInt=int(input("Serão digitados dados de quantos produtos? "))
VetNom=[0 for x in range(NumInt)]
VetPrCom=[0 for x in range(NumInt)]
VetPrVen=[0 for x in range(NumInt)]
VetTotal=[0 for x in range(NumInt)]

for ContG in range(NumInt):
    print(f"Produto {ContG+1}:")
    VetNom[ContG]=str(input("Nome: "))
    VetPrCom[ContG]=float(input("Preço compra: "))
    VetPrVen[ContG]=float(input("Preço venda: "))

for ContG in range(NumInt):
    VetTotal[ContG]=VetPrVen[ContG]-VetPrCom[ContG]

LucAb=0
LucMed=0
LucAlt=0
for ContG in range(NumInt): #calculos % lucros
    Lucro=(VetTotal[ContG]*100)/VetPrCom[ContG]
    if Lucro<10:
        LucAb +=1
    elif Lucro>=10 and Lucro<=20:
        LucMed +=1
    else:
        LucAlt +=1

TotCom=0
TotVed=0
for ContG in range(NumInt): #valor total da compra/venda
    TotCom += VetPrCom[ContG]
    TotVed += VetPrVen[ContG]

Total=TotVed-TotCom

print(f"\nRELATORIO")
print(f"Lucro abaixo de 10%: {LucAb}")
print(f"Lucro entre 10% e 20%: {LucMed}")
print(f"Lucro acima de 20%: {LucAlt}")
print(f"Valor total da compra: {TotCom:.2f}")
print(f"Valor total da venda: {TotVed:.2f}")
print(f"Lucro total: {Total:.2f}")