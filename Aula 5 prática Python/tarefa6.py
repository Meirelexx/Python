q = 0
som = 0
n = 1

while n != 0:
    n = float(input("Digite um número: "))
    som = som + n
    q = q + 1
print(f"A quantidade de números foi: {q}")
print(f"A somatoria foi: {som}")
print(f"A média foi: {som/q:.2f}")
