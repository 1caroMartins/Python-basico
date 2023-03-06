def aumentar(preco, taxa, formatar=False):
    res = preco*(1 + taxa/100)
    return res if formatar is False else moeda(res) 
    
def diminuir(preco, taxa, formatar=False):
    res = preco*(1 - taxa/100)
    return res if formatar is False else moeda(res)
    
def dobro(preco, formatar=False):
    res = preco * 2
    return res if not formatar else moeda(res)

def metade(preco, formatar=False):
    res = preco / 2
    return res if not formatar else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-'*30)