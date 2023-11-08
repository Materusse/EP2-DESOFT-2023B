def inidica_posicao(palavra_sort, palavrai_espec):
    lista = []
    if len(palavra_sort) != len(palavrai_espec):
        return lista

    for i in range(len(palavrai_espec)):
        c = palavrai_espec[i]
        if c == palavra_sort[i]:
            lista.append(0)
        elif c in palavra_sort:
            lista.append(1)
        else:
            lista.append(2)

    return lista
