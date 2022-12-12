ValX=int(input("Valor de X: "))
ValY=int(input("Valor de Y: "))

if (ValX>0) and (ValY>0):
    ValR="Q1"
elif (ValX<0) and (ValY>0):
    ValR="Q2"
elif (ValX<0) and (ValY<0):
    ValR="Q3"
elif (ValX==0) and (ValY==0):
    ValR="Origem"
else:
    ValR="Q4"

print(f"{ValR}")