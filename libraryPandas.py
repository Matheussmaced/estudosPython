# introdução a bibliotedas pandas
# manipulação de dados
# visualização de dados

#fonece struturas de dados projetados para trabalhar com dados

#install
#series é como um vetor de dados unidemencional armazenando diferentes tipos de dados
#dataframe é um conjunto de series, conteiner para serie

#ambas possui indexação das linhas

import pandas as pd

#series metodo Series() construtor: pandas.Series(data=None, index=None)
# uma series com dados é necessario usar um data=XXXX.

pd.Series(data=5)
lista_nomes ='testando1'.split()    #cria uma series com valor a lista_+nomes = 'testando1'.split()

pd.Series(lista_nomes)
dados = {
    'nome1': 'test1',
    'nome2': 'test2',
    'nome3': 'test3',
    'nome4': 'test4',
}

pd.Series(dados) #cria uma series com um dicionario

#read.JSON, read.csv leitura de arquivos

#parametro obrigatorio path_or_buf
#pd.read_json('caminho').head()

#Bibliotecas de graficos
#matplotib e outras baseadas na matplotlib

#install matplotlib npm i matplotlib
#import matplotblib.pyplot plt
