# Exercício 12
from lib import interface

def arquivo_existe(nome):
    try:
        arquivo = open(file=nome, mode='rt', encoding='utf8') # read text
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(nome):
    try:
        arquivo = open(file=nome, mode='wt+', encoding='utf8') # write text  (+ cria arquivo se não existir)
        arquivo.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def ler_arquivo(nome):
    try:
        arquivo = open(file=nome, mode='rt', encoding='utf8')
    except:
        print('Erro ao ler o arquivo')
    else:
        interface.cabecalho('Pessoas cadastradas')
        for linha in arquivo:
            dados = linha.replace('\n','').split(sep=';')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
    finally:
        arquivo.close()
        
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        arquivo = open(file=arq, mode='at', encoding='utf8') # append text
    except:
        print('Houve um ERRO na abertura do arquivo.')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao tentar escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado')
            arquivo.close()