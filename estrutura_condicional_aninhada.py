conta_normal = False
conta_universitaria = False
saldo = 2000
saque = float(input("Quanto deseja sacar? "))
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")
else:
    print("Tipo de conta não reconhecida. Contate o gerente.")