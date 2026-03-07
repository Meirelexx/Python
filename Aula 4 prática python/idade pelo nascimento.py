from datetime import date

# Entrada do ano de nascimento
ano_nascimento = int(input("Digite seu ano de nascimento: "))

# Calcula a idade
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

# Verifica idade para votar e para CNH
pode_votar = idade >= 16
pode_cnh = idade >= 18

# Saída
print(f"Sua idade é: {idade} anos.")

if pode_votar:
    print("Você já pode votar.")
else:
    print("Você ainda não pode votar.")

if pode_cnh:
    print("Você já pode tirar a Carteira de Habilitação.")
else:
    print("Você ainda não pode tirar a Carteira de Habilitação.")