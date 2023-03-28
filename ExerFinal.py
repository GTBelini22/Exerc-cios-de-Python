import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("\nEntre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentencas):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentencas)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    #A o suspeito
    sub0 = abs(as_a[0] - as_b[0])
    sub1 = abs(as_a[1] - as_b[1])
    sub2 = abs(as_a[2] - as_b[2])
    sub3 = abs(as_a[3] - as_b[3])
    sub4 = abs(as_a[4] - as_b[4])
    sub5 = abs(as_a[5] - as_b[5])

    similaridade = (sub5 + sub4 + sub3 + sub2 + sub1 + sub0)/6

    return similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # Chamada das funções auxiliares e variáveis
    soma_tam_palavras = 0.0
    soma_total_palavras = 0.0
    soma_total_sentenca = 0.0
    soma_tam_sentenca = 0.0
    n_total_frase = 0.0
    soma_tam_frase = 0.0
    frase =[]
    palavras =[]

    sentenca = separa_sentencas(texto)
    for s in range(len(sentenca)):
        aux_frase = separa_frases(sentenca[s])
        for a in range(len(aux_frase)):
            frase.append(aux_frase[a])

    for f in range(len(frase)):
        aux_palavras = (separa_palavras(frase[f]))
        for p in range(len(aux_palavras)):
            palavras.append(aux_palavras[p])

    palavras_dif = n_palavras_diferentes(palavras)
    palavras_uni = n_palavras_unicas(palavras)

    # tamanho médio
    soma_total_palavras = len(palavras)
    for i in palavras:
        soma_tam_palavras += len(i)
    tm_medio_palavras = soma_tam_palavras/soma_total_palavras

    #Relação Type-Token
    type_token = palavras_dif / soma_total_palavras

    #Razão Hapax Legomana
    hapax = palavras_uni /soma_total_palavras

    # tamanho médio senteças
    soma_total_sentenca = len(sentenca)
    for x in sentenca:
        soma_tam_sentenca += len(x)
    tm_medio_sentenca = soma_tam_sentenca / soma_total_sentenca

    #Complexidade de sentença
    n_total_frase = len(frase)
    complex_sentenca = n_total_frase / soma_total_sentenca

    #Tamanho médio de frase
    for y in frase:
        soma_tam_frase += len(y)
    tm_medio_frase = soma_tam_frase / n_total_frase

    return [tm_medio_palavras, type_token, hapax, tm_medio_sentenca, complex_sentenca, tm_medio_frase]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    controle = 0.0
    qual_texto =1
    ass_duvidosa =[]
    for i in range(len(textos)):
        ass_duvidosa = calcula_assinatura(textos[i])
        valor_simi = compara_assinatura(ass_duvidosa , ass_cp)

        if controle > valor_simi or i == 0:
            controle = valor_simi
            qual_texto = i+1

    return qual_texto


# lista_teste = ["Num fabulário a, ainda por encontrar será um dia lida esta fábula: A a uma bordadora dum país longínquo foi. alem do horizonte." , "exactamento palácio e é de supor Não nos movemos, as maos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."]
# ass_p = [7.5,64,5,8,458,4]


#inicio do programa
result =1
ass_cp = le_assinatura()
textos = le_textos()

result = avalia_textos(textos, ass_cp)
print("\nO autor do texto", result ,"está infectado com COH-PIAH")









