som = 0
aprov = 0
for x in range(0, 80):
    nota = float(input("Qual a nota? "))
    som = som + nota
    if nota >= 6:
        aprov = aprov + 1
print(f"A media foi de: {som/80}")
print(f"A quantidade de aprovados foi de: {aprov}")

