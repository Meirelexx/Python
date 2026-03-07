#programa para calcular peso ideal

#lê a altura e peso

altura = float(input("Digite sua altura: "))

#calcule peso ideal
peso_ideal = (72.7 * altura) - 58

#exibe o resultado com duas casas decimais
print(f"peso ideal: {peso_ideal:.2f}")