# Exercício 8

def aumentar(preco:float, taxa:float, formatar:bool=False)->float:
    aumento = preco*(1 + taxa/100)
    return round(aumento, 2) if formatar == False else moeda(aumento)
    
def diminuir(preco:float, taxa:float, formatar:bool=False)->float:
    reducao = preco*(1 - taxa/100)
    return round(reducao, 2) if formatar == False else moeda(reducao)

def dobro(preco:float, formatar:bool=False)->float:
    dobrar = 2*preco
    return round(dobrar, 2) if formatar == False else moeda(dobrar)

def metade(preco:float, formatar:bool=False)->float:
    dividir = preco/2
    return round(dividir, 2) if formatar == False else moeda(dividir)

def moeda(valor:float, moeda:str='R$')->str:
    return f'{moeda}{valor:>.2f}'.replace('.',',')

# Exercício 9

def resumo(preco:float, taxaa:float=10, taxar:float=5)->float:
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}') # tabulação: \t
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com 10% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com 5% de redução: \t{diminuir(preco, taxar, True)}')