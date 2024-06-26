nome = "Jajars"
idade = 32
profissao = "programador"
linguagem = "Python"

dados = {"nome": "Jajars", "idade": 31, "profissao": "programador", "linguagem": "Python"}

print("Olá, me chamo %s. Tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s. " % (nome, idade, profissao, linguagem)) # não é mais muito utilizado
print("Olá, me chamo {}. Tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}. ".format(nome, idade, profissao, linguagem)) # pouco comum de ser utilizado
print("Olá, me chamo {3}. Tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}".format(linguagem, profissao, idade, nome)) # é possível organizar a ordem que serão colocadas as strings
print("Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}".format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem)) # adiciona um identifcador que pode ser associado a uma variável
print("Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}".format(**dados)) #utiliza dos dados de um dicionário
      
print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}") # mais utilizado

PI = 3.14159
print(f"Valor de pi: {PI:.2f}")
print(f"Valor de pi: {PI:10.2f}") # 10 é a quantidade de casas antes do ponto, .2f é a quantidade de casas depois do ponto