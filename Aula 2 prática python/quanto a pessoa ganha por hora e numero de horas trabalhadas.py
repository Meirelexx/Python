#calcule a quantidade que a pessoa ganha por hora e numero de horas trabalhadas no mês

#lê valor de hora
valor_por_hora = float(input("Digite valor por horas trabalhadas: "))

#lê quantidade de horas
numeros_de_horas = float(input("Digite a quantidade de horas trabalhadas: "))

#calcule sálario bruto
Salário_bruto = (valor_por_hora * numeros_de_horas)

#calule descontos

#calculo porcenteagem de desconto
imposto_de_renda = (Salário_bruto * 0.11)

INSS = (Salário_bruto * 0.08)

sindicato = (Salário_bruto * 0.05) 

descontos_totais = (INSS + imposto_de_renda + sindicato)

#calcule o salario bruto
Salário_liquido = (Salário_bruto - descontos_totais)

print(f"Salário líquido: {Salário_liquido: .2f}")