curso = "pYtHon"

print(curso.upper()) # todos os caracteres maiúsculos
print(curso.lower()) # todos os caracteres minúsculos
print(curso.title()) # todos os caracteres minúsculos, com exceção do primeiro, que fica maiúsculo

curso = "    Python  "
print(curso.strip() + ".") # remove espaços antes de depois da string
print(curso.lstrip()+ ".") # remove espaços do lado esquerdo da string
print(curso.rstrip()+ ".") # remove espaços do lado direito da string

curso = "Python"
print(curso.center(10, "#")) #centraliza o texto e adiciona caracteres para completar os espaços. Padrão é espaço.
print(".".join(curso)) #adiciona um texto após cada iteração do item.