texto = "Este é um exemplo de texto"

# string[start:stop:step].    
print(texto[0]) # Índice inicia no 0.
print(texto[:9]) # Caso fique vazio o start, incia no 0. Será exibido até o stop - 1
print(texto[10:]) # Caso o stop esteja vazio, vai até o final da string.
print(texto[10:17])
print(texto[-1:-5:-1])
print(texto[10:17:2]) 
print(texto[:]) # Caso não seja passado nenhum valor, retorna a string inteira
print(texto[::-1]) # Com step negativo, inverte a ordem da string