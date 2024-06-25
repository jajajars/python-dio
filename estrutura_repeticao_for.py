texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:   
    print() # adiciona linha em branco
    print("Else executa no final da estrutura for")

for numero in range(11): # range(start, stop, step) realiza incremento de um número até outro. Obrigatório o final. 
    print(numero, end=" ")

for numero in range(0, 21, 2):
    print(numero, end=" ")