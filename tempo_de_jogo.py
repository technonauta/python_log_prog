HorIn=int(input("Hora inicial: "))
HorFn=int(input("Hora final: "))

if HorFn>HorIn:
    Dur=HorFn-HorIn
elif HorFn==HorIn:
    Dur=24
else :
    Temp=24-HorIn
    Dur=Temp+HorFn

print(f"O JOGO DUROU {Dur} HORAS")