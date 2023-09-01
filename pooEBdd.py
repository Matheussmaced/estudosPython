#POO

#Uma classe é uma abvstração que descreve entidades do mundo real e quando instanciadas dão origem a objetos 
#com caracteristicas similares.

#atributos: são as caracteristicas de um objeto

#herança: permite que uma classe herde atributos de outra classe

#encapsulamento: o ato de combinar atributos e metodos na mesma entidade.
#pratica de tornar um atributo privado quando este é encapsulado em metodos para guardar e acessas seus valores

#poloformismo: classe dentro de classe. significa 'muitas formas'


#classes e metodos em python
class className:
    test: 'test'
    test2: 'test'


#construtor da classe _init_()
#variaveis de instancias. Esse tipo de atributo é capaz de receber um valor diferente para cada objt

#variaveis e metodos privados:
#em python, não existem modificadores de acesso e todos os recursos são publicos


#herança em python:
#em python uma casse aceita multiplas heranças, ou seja, herda recursos de diversas classes
#NomeClasseFilha(NomeClassePai) ex: class pessoa  class x         class Funcionario(pessoa, x): atributo


#metodos magicos em python:
#quando uma classe é criada em python, ela herda, mesmo que não declado explicitamente, todos os recursos
#de uma classe-base chamada object
#dir() underline(sublinhado)


#Bibliotecas e modulos em python

#modulo pode ser uma biblioteca de codigos, o qual possui diversas funções(matematicas, sitema operacinal. etc)
#possibilitando reutilizar o codigo

#maneiras de utilizar um modulo

#importação:
#import moduloXXtext
#import moduloXX as apelido
#from moduloXX import itemA, itemB

#classificação dos modulos (bibliotecas)
# 1. modulos built-in: embutidos no interpretador
# 2. modulos de terceiros: criados por terceiros e pisponibilizados via PyPI.
# 3. modulos proprios: criados pelo desenvolvedor


#Banco de DADOS
#sistema de banco de dados podem ser divididos em duas categorias: banco de dados relacional e
#banco de dados NoSQL

#NoSQL é usado para aboredar a classe de bancos de dados que não seguem os princípios do sistema de
#gerenciamento de banco de dados relacional (RDBMS) e são projetados especificamente para lidar com a
#velocidade e a escala de aplicações

#SQL
#é uma linguagem que permite aos usuários se comunicarem com banco de dados relacionais.
# a estrutura são dividadas em 3
#DLL, DML, DCL

#DLL : criar, deletar e modificar bdd e tabelas, comandos famosos: CREATE, ALTER e o DROP
#DML : recuperar, atualizar, adicionar ou excluir dados do bdd, comandos famosos: INSERT, UPDATE e DELETE
#DLC : segurança adequada para o bdd, comandos famosos: GRANT e REVOKE.

#conexão com banco de dados
# com a linguagem SQL, podemos usar as tecnologias ODBC e JDBC

#Criando um banco de dados
import sqlite3
conn = sqlite3.connect('aulaDB.db')
print(type(conn))

#criando tabela
dll_create = """
CREATE TABLE fornecedor (
id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
cnpj VARCHAR(18) NOT NULL,
cidade TEXT
);
"""
#executando esse objeto
cursor = conn.cursor()
cursor.execute(dll_create)
print(cursor)

#CRUD - create, read, update, delete
#CREATE: maneira mais pratica de inserir varios registros e passar uma lista de tuplas
#READ: recuperar os dados
#UPDATE: Ao inserir um registro no bancom pode ser necessário alterar o valor da coluna
#DELETE: ao inserir um registro no banco, pode ser necessário removê-lo no futuro


