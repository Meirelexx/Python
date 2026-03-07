n = int(input("Me de um numero inteiro e positivo: "))
x = 1
som = 0

while True:
    som = som + 1/x
    if x == n:
        break
    x = x + 1
print(f"A soma é: {som:.2f}")