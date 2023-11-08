def remover_especiais(palavra):
    caracteres_especiais = "!@#$%^&*()_+{}|:\"<>?`-=[]\\;',./"
    palavra_sem_especiais = palavra.strip(caracteres_especiais)
    return palavra_sem_especiais
def filtra(palavras,num_l):
    lista2 = []
    lista3 = []
    for palavra in palavras:
        if len(palavra) == num_l:
            palavra = palavra.lower()
            lista2.append(palavra)
    for palavra in lista2:
        lista3.append(remover_especiais(palavra))
    lista4 = []
    for palavra in lista3:
        if palavra not in lista4:
            lista4.append(palavra)
    return lista4