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