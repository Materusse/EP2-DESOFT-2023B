import random
def inicializa(lista):
    dic = {}
    dic['n'] = len(lista[0])
    dic['sorteada'] = random.choice(lista)
    dic['especuladas'] = []
    dic['tentativas'] = len(lista[0]) + 1
    return dic