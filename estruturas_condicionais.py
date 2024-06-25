MAIORIDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))
if idade >= MAIORIDADE:
    print("Pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teórias, mas não práticas")
else:
    print("Não pode tirar a CNH")
