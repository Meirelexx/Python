#calcule a quantidade de segundos, minutos, horas e dias somente em segundos

#lê a quantidade de segundos 
segundos = int(input("Digite a quantidade de segundos: "))

#lê a quantidade de minutos 
minutos = int(input("Digite a quantidade de minutos: "))

#lê a quantidade de horas
horas = int(input("Digite a quantidade de horas: "))

#lê a quantidade de dias
dias = int(input("Digite a quantidade de dias: "))

#clcule a quantidade de segundos totais
segundos_totais = (1 * segundos) + (60 * minutos) + (3600 * horas) + (86400 * dias)

print(f"Segundos totais: {segundos_totais}")