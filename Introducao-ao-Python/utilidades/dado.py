# Exercício 10

def leiaDinheiro(msg:str)->float:
    while True:
        try:
            entrada = float(str(input(msg)).replace(',','.').strip())
        except (ValueError, TypeError):
            print(f'ERRO: valor inválido!')
            continue
        except KeyboardInterrupt:
            print(f'ERRO: O usuário preferiu não informar um valor!')
            return 0
        except Exception as exc:
            print(f'ERRO inseperado: {exc.__class__}')
            continue
        else:
            return entrada
        