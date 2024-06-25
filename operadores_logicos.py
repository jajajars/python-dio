saldo = 1200
saque = 200
limite = 100

print(saldo >= saque)
print (saque <= limite)

print(saldo >= saque and saque <= limite) #operador lógico E
print(saldo >= saque or saque <= limite) #operador lógico OU

contatos_emergencia=[] #listas vazias em python são consideradas false
print(not 1000 > 1500) #operador negação
print(not contatos_emergencia)
print (not "saque 1500") #strings preenchidas são true
print (not "") #strings vazias são false

conta_especial = True
print(saldo >= saque and saque <= limite or conta_especial and saldo == saque) #ordem de lógica: not > and > or
print((saldo >= saque and saque <= limite) or (conta_especial and saldo == saque)) #parênteses são usados para dar precedência
print(saldo >= saque and (saque <= limite or conta_especial) and saldo == saque)