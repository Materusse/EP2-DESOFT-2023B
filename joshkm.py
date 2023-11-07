# funcoes obrigatorias:

import random
def inicializa(lista):
    dic = {}
    dic['n'] = len(lista[0])
    dic['sorteada'] = random.choice(lista)
    dic['especuladas'] = []
    dic['tentativas'] = len(lista[0]) + 1
    return dic

def filtra(lista,n):
    saida = []
    for palavra in lista:
        if len(palavra) == n:
            if palavra.lower() not in saida:
                saida.append(palavra.lower())
    return saida

def inidica_posicao(sorteado,espec):
    if len(sorteado) != len(espec):
        return []
    saida = [0]*len(sorteado)
    for i in range(len(sorteado)):
        if espec[i] == sorteado[i]:
            saida[i] = 0
        elif espec[i] in sorteado:
            saida[i] = 1
        elif espec[i] not in sorteado:
            saida[i] = 2
    return saida

