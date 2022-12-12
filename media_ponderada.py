ValrN=int(input("Quantos números você vai digitar? "))

for contG in range(ValrN):
    print(f"Digite três número: ")
    CalMed1=float(input())
    CalMed2=float(input())
    CalMed3=float(input())

    Mediana=((CalMed1*2)+(CalMed2*3)+(CalMed3*5))/10
    print(f"MEDIA = {Mediana:.1f}")