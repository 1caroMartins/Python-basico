# exercício 6

def aumentar(preco:float, taxa:float)->float:
    aumento = preco*(1 + taxa/100)
    return round(aumento, 2)
    
def diminuir(preco:float, taxa:float)->float:
    reducao = preco*(1 - taxa/100)
    return round(reducao, 2)

def dobro(preco:float)->float:
    dobrar = 2*preco
    return round(dobrar, 2)

def metade(preco:float)->float:
    dividir = preco/2
    return round(dividir, 2)

# exercício 7

def moeda(valor:float, moeda:str='R$')->str:
    return f'{moeda}{valor:>.2f}'.replace('.',',')