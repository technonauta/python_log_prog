print(f"Digite os valores das coordenadas: ")
ValRX=int(input())
ValRY=int(input())

while (ValRX!=0) and (ValRY!=0):
    if (ValRX>0) and (ValRY>0):
        Quad="QUADRANTE Q1"
        print(f"{Quad}")
        print(f"Digite os valores das coordenadas: ")
        ValRX=int(input())
        ValRY=int(input())
    elif (ValRX<0) and (ValRY>0):
        Quad="QUADRANTE Q2"
        print(f"{Quad}")
        print(f"Digite os valores das coordenadas: ")
        ValRX=int(input())
        ValRY=int(input())
    elif (ValRX<0) and (ValRY<0):
        Quad="QUADRANTE Q3"
        print(f"{Quad}")
        print(f"Digite os valores das coordenadas: ")
        ValRX=int(input())
        ValRY=int(input())
    else:
        Quad="QUADRANTE Q4"
        print(f"{Quad}")
        print(f"Digite os valores das coordenadas: ")
        ValRX=int(input())
        ValRY=int(input())