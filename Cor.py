def cor(s,lista):
    saida = ''
    for i in range(len(s)):
        if lista[i] == 0:
            saida += '\033[0;32m {0}'.format(s[i])
        elif lista[i] == 1:
            saida += '\033[0;33m {0}'.format(s[i])
        else:
            saida += '\033[0;31m {0}'.format(s[i])
    return saida