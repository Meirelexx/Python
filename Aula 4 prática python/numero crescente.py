#leitura dos valores diferentes
a = int(input("Digite o numero de valor inteiro: "))
b = int(input("Digite o numero de valor inteiro (diferente do primeiro): "))
c = int(input("Digite o numero de valor inteiro (difernte dos anteriores): "))

#verificar valores diferentes
if a == b or b == c or c == b:
    print("erro: os valore devem ser diferentes.")
else: 
    #valores em lista
    valores = [a, b, c]
    #Ordena em ordem decrescnte
    valores.sort(reverse=True)
    # Mostra os valores em ordem decrescente
    print("Valores em ordem decrescente:", valores[0], valores[1], valores[2])