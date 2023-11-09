from lista_palavras import words
from Inicializa_termo import *
from Indica_posição_correta import *
from Filtra_palavras import *
from Diagrama import *
from Cor import *

n = random.randint(4,6)
lista_filtrada = filtra(words,n)
dic_inicializa = inicializa(lista_filtrada)

num_letras = dic_inicializa['n']
num_tentativas = dic_inicializa['tentativas']
palavra_sort = dic_inicializa['sorteada']
lista_especuladas = dic_inicializa['especuladas']

print('A palavra tem \033[0;31m{0} \033[0;37mletras'.format(num_letras))
print('E você tem \033[0;32m{0} \033[0;37mtentativas para acertar a palavra'.format(num_tentativas))