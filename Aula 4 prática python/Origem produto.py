def origem_produto(codigo):
    if codigo == 1:
        return "Sul"
    elif codigo == 2:
        return "Norte"
    elif codigo == 3:
        return "Leste"
    elif codigo == 4:
        return "Oeste"
    elif codigo == 5 or codigo == 6:
        return "Nordeste"
    elif codigo in [7, 8, 9]:
        return "Sudeste"
    elif 10 <= codigo <= 20:
        return "Centro-Oeste"
    elif 25 <= codigo <= 30:
        return "Nordeste"
    else:
        return "Importado"

# Entrada de dados
preco = float(input("Digite o preço do produto: R$ "))
codigo = int(input("Digite o código de origem do produto: "))

# Processamento
procedencia = origem_produto(codigo)

# Saída
print(f"Preço: R$ {preco:.2f} - Procedência: {procedencia}")