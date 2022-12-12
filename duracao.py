
duracao = int(input("Digite a duracao em segundos: "))

horas = duracao // 3600; 'resultado numero inteiro'
resto = duracao % 3600;  'resultado o q sobrou da equacao da hora'

minutos = resto // 60;   'mint descobertos do valor da hora em formato inteiro'
segundos = resto % 60;   'resto dos minutos / tirados das horas'

print(f"{horas}:{minutos}:{segundos}")