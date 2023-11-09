from lista_palavras import words
from Inicializa_termo import *
from Indica_posição_correta import *
from Filtra_palavras import *
from Diagrama import *
from Cor import *

positivos = ['Sim','sim','S','SIM']
continuar = 'sim'
while continuar in positivos:
    n = random.randint(4,6)
    lista_filtrada = filtra(words,n)
    dic_inicializa = inicializa(lista_filtrada)

    num_letras = dic_inicializa['n']
    num_tentativas = dic_inicializa['tentativas']
    palavra_sort = dic_inicializa['sorteada']
    lista_especuladas = dic_inicializa['especuladas']

    print('A palavra tem \033[0;31m{0} \033[0;37mletras'.format(num_letras))
    print('E você tem \033[0;32m{0} \033[0;37mtentativas para acertar a palavra'.format(num_tentativas))
    espec = input('Digite uma palavra: ')
    i = 0
    while espec != palavra_sort and i < num_tentativas-1:
        if espec not in words:
            print('Digite uma palavra que exista!')
        elif len(espec) > num_letras:
            print('Digite uma palavra menor!')
        elif len(espec) < num_letras:
            print('Digite uma palavra maior!')
        elif espec in lista_especuladas:
            print('Digite uma palavra diferente!')
        else:
            lista_posicao = inidica_posicao(palavra_sort,espec)
            s_color = cor(espec,lista_posicao)
            lista_especuladas.append(s_color)
            s_diagrama = diagrama(lista_especuladas)
            print(s_diagrama)
            i += 1
        espec = input('Digite uma palavra: ')
    lista_posicao = inidica_posicao(palavra_sort,espec)
    s_color = cor(espec,lista_posicao)
    lista_especuladas.append(s_color)
    s_diagrama = diagrama(lista_especuladas)
    print(s_diagrama)
    if espec == palavra_sort:
        print('Parábens você acertou!')
    elif espec != palavra_sort:
        print('Que pena! Você errou!')
    continuar = input('Deseja continuar jogando? ')