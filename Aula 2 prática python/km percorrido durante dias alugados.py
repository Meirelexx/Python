#programa para calcular quantidade de kilometros rodados e dias alugados

#lê kilometros 
kilometros = float(input("Digite a quantidade de Kilometros: "))

#lê dias alugados
dias_alugados = float(input("Digite quantidade de dias alugados: "))

#calcule aluguel total 
aluguel_total = (0.15 * kilometros) + (60 * dias_alugados)

#exibe resultado do aluguel total 
print(f"Aluguel total: {aluguel_total: .2f}")