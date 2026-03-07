altura = float(input("Digite sua altura (ex:1.75)"))
sexo = input("Digite seu Sexo (M para Masculino ou F para Feminino): ").strip().upper()

#calculo
if sexo == 'M' :
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'F' :
    peso_ideal = (61.1 * altura) - 44.7
else:
    peso_ideal = None

#saída
if peso_ideal is not None:
    print(f"seu peso ideal é: {peso_ideal:.2f} kg")
else:
    print("sexo inválido. Porfavor insira novamente (Masculino ou Feminino): ")