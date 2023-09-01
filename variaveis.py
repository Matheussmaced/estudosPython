# Variaveis: Espaços de memorias que sao alocadas
# Não precisa ser tipada
# Tipadas dinamicamente

x = 10
nome = 'test'
nota = 8.5
flag = True

print(type(x)) #int
print(type(nome)) #str
print(type(nota)) #float
print(type(flag)) #bool

# Em python, tudo é objeto!
nome = input('Digite seu nome ')

# Formatadores de caracteres
print('Olá %s, Bem vindo!'%(nome))

#Operações matematicas
# abs() retorna valor absoluto
# pow() retorna a potencia

# primeiro se resolve os parenteses
# depois a pontenciação
# depois a multiplicação e divisão
# depois a soma e subtração


## Estitiras Lógicas, condicionais de pretição em python
nome = 'matheus'
if nome:
    print('A variavel não está vazia')

# Estrutura composta
number = 5

if 5 < 2:
    print('É menor que 2')
else:
    print('É maior que 2')

# Estrutura encadeada

cor = 'amarelo'
# operador relacional ( == )
if cor == 'verde':
    print('acelerar')
elif cor == 'amarelo':
    print('calma')
else:
    print('frear')

# and, or, not

# and: resultado será true, quando os dois argumentos forem verdadeiros &&
# or: o resultado será true, quando pelo menos um dos argumentos for verdadeiro ||
# not: ele irá inverter o valor do argumento !

notaAluno = 7
quantidadeDeFaltas = 6

if quantidadeDeFaltas <= 5 and notaAluno >= 7:
    print('aprovado')
else:
    print('reprovado')

# Estrutura de repetição: while e for

# COMANDO WHILE DEVE SER UTILIZADO PARA CONSTRUIR E CONTROLAR A ESTRUTURA DECISÃO, SEMPRE QUE O NUMERO DE REPETIÇÕES NÃO
#SEJA CONHECIDO

numero = 1
#quando meu numero for diferente de 0 vou executar o treço de codigo
while numero != 0:
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        print('Numero par!')
    else:
        print('Numero impar!')

# COMANDO FOR SEGUIDO DA VARIAVEL DE CONTROLE C, NA SEQUENCIA O COMANDO IN, POR FIM, A SEQUENCIA SOBRE A QUAL A ESTRUTURA DEVE
#ITERAR. OS DOIS PRONTOS MARCAM O INICIO DO BLOCO QUE DEVE SER REPETIDO.

nome = 'Guido'
# Vai printar todas as letras
# imprimi tudo aquilo que tem no meu nome
for c in nome:
    print(c)


#enumerate() PARA RETORNAR A POSIÇÃO DE CADA ITEM, DENTRO DA SEQUENCIA
# vai dizer a posição de cada letra e o valor
for i, c in enumerate(nome):
    print(f'posição = {i}, valor = {c}')

# controle de repetição com range, break e continue:
# range, passo um valor, ele irá imprimir cada index desse valor
for x in range(5,25):
    print(x)

#break e continue mesmo do javascript


#Funções

#função built-in => funções já implementadas

#função que implementa função de 2 segundo grau
a = 2
b = 1
equacao = input('Digite a formula geral da equação linear (a * x + b): ')
print(f"Na entrada do usuario {equacao} é do tipo {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"Resultado da equação para x = {x} é {y}")

#Função definida pelo usuario
#Parece com as funções do js

# posso atribuir no segundo parametro o value default
def imprimir_mensagem(disciplina, curso):
    print(f'Minha primeira função python: {disciplina}, do curso: {curso}')

imprimir_mensagem('Python', 'Engenharia de software')

#FUNÇÃO ANONIMA parecido com js

somar = lambda x, y: x + y
somar(x=5, y=3)