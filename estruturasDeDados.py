# Estruturas de dados
# resumo: Saber utilizar modelos de estrutura de dados em python
# palavras-chave: algoritmos; python; ordenação; estrutura de dados; busca;

# Vamos estudar:
# obj type sequencia: texto, listas e tuplas.
# Obj type set (conjunto).
# Obj type mapping (dicionário).
# Obj type array NumPy.

# Sequencia
# representam sequencias finitas indexadas por numeros não negativos

texto = 'aprendendo python'
print(f'tamanho do texto = {len(texto)}')
print(f'python in texto = {"Python" in texto}')
print(f'quantidade de y no texto = {texto.count("y")}')
print(f'As 5 primeiras letras são = {texto[0:6]}')

# plit() serve para cortar, igual ao splice() do javascript

#lista  remove um item do meu array
# criando uma lista a partir de outra lista
linguagens = ['JavaScript', 'Python', 'Java']
print('antes da listcomp = "', linguagens)

linguagens = [item.lower() for item in linguagens]  #lower serve como lowerCase do javascript
print('\nDepois da listcomp = "', linguagens)

#map() e filter() são iguais ao javascript

nova_lista = map(lambda x: x.lower(), (linguagens))
print(nova_lista)

numeros = list(range(0,21))
numeros_pares = list(filter(lambda x: x% 2 == 0, numeros))
print(numeros_pares)

#Tuplas
#A grande diferença entre listas e tuplas é que as primeiras são mutaveis, razão pela qual, com elas, conmseguimos
# fazer atribuições a posições especificas: por exemplo, lista[2] = 'maça'
# tupla1 = ()
# tupla2 = ('a','b','c')
# tuple()

vogais = ('a','e','i')
print(f'tipo de vogais ={type(vogais)}')

for p, x in enumerate(vogais):
    print(f'posição ={p}, valor ={x}')


#set
#objetos do tipo set

#array
#import numpy

#matriz_1_1 = numpy.array([1,2,3])

#Algoritmos de busca
#Busca linear
#Percorre os elementos de uma sequencia procurando aquele de destino, começando por uma das
#extremidades daquela sequencia e vai percorrendo até encontrar(ou não) o valor desejado
lista = [1,2,3,4,5]

def executar_busca_linear(list, valor):
    for elemento in lista:
        if valor == elemento:
            return True
        return False
executar_busca_linear(lista, 3)

#Sequencia
# em python, as estruturas de dados do tipo sequencia possuem a função index(), que é usada da seguinte forma:
# sequencia.index(valor)
# igual ao index do javascript
vogais = 'aeiou'
resultado = vogais.index('e')
print(resultado)


#Complexidade
#Estudo da viabilidade de um algoritmo, em termos de espaço e tempo de
#processamento, é chamado de analise da complexidade do algoritmo(onde vamos verificar se o algoritmo é viavel ou n)


#Busca Binária
#Outro algoritmo usado para buscar um valor em sequencia. A primeira grande diferença entre eles, é que
# os valores precisam estar ordenados.

# encontra o item no meio da sequencia(meio da lista)
# se o valor procurado for igual ao item do meio, a busca se encerra
# se não for, verifica-se se o valor buscado é maior ou menor que o valor cental
# se for maior, então a busca acontecerá na metade superior da sequencia ( a inferiopr é descatada ); se não for,
# a busca acontecerá na metade inferior da sequencia ( a superior é descartada).
list = [1,2,3]
def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        #encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        #verifica se o valor procurado está a esquerda ou direita do valor central
        if valor < lista[meio]:
            maximo = meio -1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True # o valor for encontrado para aqui
        
        return False # se chegar até aqui, significa que o valor não foi encontrado

executar_busca_binaria(list,2)
#sequencial metodo mais caro


#Algoritmos de ordenação

#consiste em comparar dois valores, verificar qual é menor e colocar na posição correta
#sorted() e o metodo sort() presente nos objetos da classe list.

list = [10,4,1,15,-3]
lista_ordenada1 = sorted(list)

lista_ordenada2 = list.sort()

print('lista = ', list, '\n')

print('lista_ordenada1 =', lista_ordenada1)
print('lista_ordenada2 =', lista_ordenada2)

print('lista = ', list)


#selection sort (ordenação por seleção)

#recebe esse nome, porque faz a ordenação sempre escolhendo o menor valor para ocupar uma determinar posição
# troca o menor pelo maior da direita pra esquerda fazendo o swap


#Buble sort (Ordenação por 'bolha')

#faz a ordenação sempre a partir do inicio da lista, comprando um valor com seu vizinho. Esse processo é
#repetido até que todas as valores estejam na posição correta.


#Merge sort (ordenação por junção)
#recebe esse nome porque faz a ordenação em duas etapas:
# 1 divide a llista em sublistas;
# 2 e junta (merge) as sublistas ja ordenadas

