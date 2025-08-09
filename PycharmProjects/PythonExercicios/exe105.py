def notas(*n, sit = False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas e situações de vários alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if sit:
        if r['Media'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Media'] >5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r
resp = notas(5.5, 2.5 ,9, sit=True)
print(resp)
help(notas)