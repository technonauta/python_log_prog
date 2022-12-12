QtPess=int(input("Quantas pessoas serão digitadas? "))

VetNom =[0 for contX in range(QtPess)]
VetIdd =[0 for contX in range(QtPess)]
VetAlt =[0 for contX in range(QtPess)]


for ContI in range(QtPess):
    print(f"Dados da {ContI+1}ª pessoa:")
    VetNom[ContI]=str(input("Nome: "))
    VetIdd[ContI]=int(input("Idade: "))
    VetAlt[ContI]=float(input("Altura: "))

Altura=0
NumMenores=0
for ContI in range(QtPess):
    if VetIdd[ContI]<16:
        NumMenores += 1
        Altura += VetAlt[ContI]

MedAlt=Altura/NumMenores
PorcIdd=(float(NumMenores)*100)/QtPess

print(f"\nAltura média: {MedAlt:.2f}")
print(f"Pessoas com menos de 16 anos: {PorcIdd:.1f}%")

for ContI in range(QtPess):
    if VetIdd[ContI]<16:
        print(VetNom[ContI])