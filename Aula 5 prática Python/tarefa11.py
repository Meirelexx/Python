mf = 0
somsala = 0
som = 0
qt = 0
qm = 0
sex = "reset"
while True:
    idad = int(input("Qual a idade? "))
    if idad < 0:
        break
    while sex != "M" or sex != "F":
        sex = str(input("M ou F? ")).upper()
        if sex == "M" or sex == "F":
            break
    sala = float(input("Qual o salario? "))
    if sex == "F" and sala < 600:
        mf = mf + 1
        
    if sex == "M":
        somsala = somsala + sala
        qm = qm + 1
    som = idad + som
    qt = qt + 1
    sex = "reset"

print(f"A media de idade do gp é: {som / qt}")
print(f"A media de salario dos homens é de: {somsala / qm}")
print(f"A quantidade de mulheres muito pobres é de: {mf}")
