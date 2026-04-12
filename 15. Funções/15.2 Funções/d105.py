def notas(*num, situ):
    """
    -> Função para analisar notas e situações de vários.
    : param n: uma ou mais notas dos alunos(aceita várias)
    : param sit: valor opcional, indicando se deve ou não adicionar a situação
    : return: dicionário com várias informações sobre a situação da turma. 
    
    """
    
    tot = len(num)
    pos = mai = men = med = som = 0
    while pos < len(num):
        if pos == 0:
            mai = num[pos]
            men = num[pos]

        if num[pos] > mai:
            mai = num[pos]
        
        if num[pos] < men:
            men = num[pos]

        som += num[pos]
        pos += 1
        med = som / len(num)
    if situ == True:
        if med >= 7:
            sit = 'BOA'
        elif med < 7 and med > 5:
            sit = 'Razoável'
        else: 
            sit = 'Lixo'

        d = {'Total' : tot, 'Maior' : mai, 'Menor': men , 'média' : med, 'Situação' : sit }
        return d       
    else:
        d = {'Total' : tot, 'Maior' : mai, 'Menor': men , 'média' : med }
        return d

resp = notas( 9.8, 5.5, 4.5, 8, situ = True)
print(resp)