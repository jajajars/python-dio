# Declaração de listas
frutas = [] #lista vazia
print(frutas)

frutas = ["laranja", "maca", "uva", "morango"]
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

# Acesso direto um item da lista

print(frutas[0]) # os índices comecam no zero
print(frutas[2])
print(frutas[:2])
print(frutas[-1]) # é possível indexar itens negativos

# Listas aninhadas
# Usadas geralmente para representar tabelas bidimensionais
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz)
print(matriz[0]) 
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-2])

# É possível usar o fatiamento para selecionar vários itens da lista
lista = list("python")
print(lista)
print(lista[2:])
print(lista[:2])
print(lista[1:4])
print(lista[::2])
print(lista[::])
print(lista[::-1])

carros = ["gol", "celta", "palio"]

for carro in carros: # percorrer os dados da lista
    print(carro)

for indice, carro in enumerate(carros): # retona o índice e o valor de cada item da lista
    print(f"{indice}: {carro}")

pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) # adiciona a variável na lista

print(pares)

pares_2 = [numero for numero in numeros if numero % 2 == 0] # lista = [retorno iteração condição]
print(pares_2)