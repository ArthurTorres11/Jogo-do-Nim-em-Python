def computador_escolhe_jogada(n, m):
    computadorRemove = 1
    while computadorRemove != m:
        if (n - computadorRemove) % (n + 1) == 0:
            print(f'O computador tirou {computadorRemove} peça')
            print(f'Agora restam {m - computadorRemove} peças no tabuleiro')
            return computadorRemove
        else:
            computadorRemove += 1

    return computadorRemove
    
    
def usuario_escolhe_jogada(n, m):
    while True: 
        jogada_pessoa = int(input('Informe o número de peças que vai retirar: '))
        if jogada_pessoa <= m: 
            print(f'O usuario tirou {jogada_pessoa} peças')
            print(f'Agora restam {n - jogada_pessoa} peças')
            return jogada_pessoa
        else:
            print(f'Você não pode retirar {jogada_pessoa}, o máximo de peças que pode retirar é {m}.')

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print(f'Número de peças totais no jogo: {n}')
    print(f'Número de peças possiveis a serem retiradas no jogo: {m}')
    tabuleiro = n

    if n % (m+1) == 0: 
        while tabuleiro > 0:
            print('Você começa!')
            print()
            peças_retiradas = usuario_escolhe_jogada(n,m)
            tabuleiro = tabuleiro - peças_retiradas
            if tabuleiro == 0: 
                vencedor = 0
                break
            peças_retiradas = computador_escolhe_jogada(n,m)
            tabuleiro = tabuleiro - peças_retiradas
            if tabuleiro == 0:
                vencedor = 1
                break
    else:
        while tabuleiro > 0:
            print('Computador começa!')
            print()
            peças_retiradas = computador_escolhe_jogada(n,m)
            tabuleiro = tabuleiro - peças_retiradas
            if tabuleiro == 0: 
                vencedor = 1
                break
            peças_retiradas = usuario_escolhe_jogada(n,m)
            tabuleiro = tabuleiro - peças_retiradas
            if tabuleiro == 0:
                vencedor = 0
                break
    if vencedor == 1: 
        print('Computador venceu!')
    else:
        print('Você venceu!')

print(partida())
