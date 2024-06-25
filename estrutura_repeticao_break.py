while True:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        break # encerra o loop
    print(numero)

for numero in range(100):
    if numero == 12:
        continue #pula a execução do loop
    if numero == 75:
        break
    print(numero, end= " ")
