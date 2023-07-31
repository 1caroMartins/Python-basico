#Exercício 12

def leiaInt(txt:str)->int:
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário. \033[m')
            return 0
        else:
            return num

def linha(tam:int = 42)->str:
    return '-' * tam

def cabecalho(txt:str)->str:
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista:list)->int:
    cabecalho('Menu Principal')
    for chave, valor in enumerate(lista):
        print(f'\033[33m{chave+1} - \033[34m{valor}\033[m')
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc