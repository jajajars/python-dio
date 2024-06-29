print(set([1, 2, 3, 1, 3, 4])) # conjuntos não têm elementos repetidos
print(set("abacaxi")) # recebe objetos iteráveis
print(set((1, 2, 3, 1, 3, 4))) # funciona com tuplas

linguagens = {"python", "java", "python"} # é declarado entre chaves
print(linguagens) # remove os duplicados

# Conjuntos não suportam indexação e precisam ser convertidos em lista para acessar os valores

numeros = {1, 2, 3, 4}
numeros = list(numeros)
print(numeros)

# para iterar os elementos do conjunto usa-se for
carros = {"gol", "celta", "palio"}
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Métodos

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.union(conjunto_b)) # união
print(conjunto_a.intersection(conjunto_b)) # intersecção
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b)) # união dos conjuntos menos interscção entre eles

conjunto_b = {4, 1, 2, 5, 6, 3}
print(conjunto_a.issubset(conjunto_b)) # verifica se é subconjunto de outro conjunto
print(conjunto_b.issubset(conjunto_a))

print(conjunto_a.issuperset(conjunto_b)) # verifica se um conjunto contém outro
print(conjunto_b.issuperset(conjunto_a))

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b)) # verifica se os conjuntos são separados
print(conjunto_b. isdisjoint(conjunto_c))
print(conjunto_c.isdisjoint(conjunto_a))

sorteio = {1, 23}
sorteio.add(30) # adiciona um elemento no conjunto
sorteio.add(22)
sorteio.add(25) # não adiciona elementos repetidos
print(sorteio)
sorteio.discard(1) # remove o elemento 
sorteio.discard(120) # ele ignora elementos que não existem
print(sorteio)
sorteio.pop() # remove o primeiro elemento
print(sorteio)
sorteio.remove(25) # remove o elemento. Caso seja passado um elemento não reconhecido, o interpretador apresenta erro
sorteio.clear() # limpa o conjunto
print(sorteio)
sorteio.copy() # gera uma cópia
print(len(sorteio)) # retorna a quantidade de elementos

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(1 in numeros) # retorna se o elemento faz parte do conjunto
print(10 in numeros)

