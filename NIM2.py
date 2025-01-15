def computador_escolhe_jogada(n, m):
    if n > m:
        computadorRemove = n % (m + 1)
        if computadorRemove == 0:
            computadorRemove = m
    else:
        computadorRemove = n
    print(f'O computador tirou {computadorRemove} peça(s).')
    print(f'Restam {n - computadorRemove} peça(s).')
    return computadorRemove

def usuario_escolhe_jogada(n, m):
    """
    Função que solicita e valida a jogada do usuário.
    """
    while True:
        jogada_pessoa = int(input('Informe o número de peças que vai retirar: '))
        if 1 <= jogada_pessoa <= m:  # Verifica se a jogada está dentro do limite
            print(f'Você tirou {jogada_pessoa} peça(s).')
            return jogada_pessoa
        else:
            print(f'Você não pode retirar {jogada_pessoa} peça(s). Retire entre 1 e {m}.')

def partida():
    """
    Função principal que coordena o jogo.
    """
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print(f'Número de peças totais no jogo: {n}')
    print(f'Número de peças possíveis a serem retiradas por jogada: {m}')
    tabuleiro = n

    if n % (m + 1) == 0:
        print('Você começa!')
    else:
        print('Computador começa!')

    while tabuleiro > 0:
        if n % (m + 1) == 0:  # Vez do usuário
            jogada = usuario_escolhe_jogada(tabuleiro, m)
            tabuleiro -= jogada
            if tabuleiro == 0:
                print('Você venceu!')
                return
            jogada = computador_escolhe_jogada(tabuleiro, m)
            tabuleiro -= jogada
            if tabuleiro == 0:
                print('Computador venceu!')
                return
        else:  # Vez do computador
            jogada = computador_escolhe_jogada(tabuleiro, m)
            tabuleiro -= jogada
            if tabuleiro == 0:
                print('Computador venceu!')
                return
            jogada = usuario_escolhe_jogada(tabuleiro, m)
            tabuleiro -= jogada
            if tabuleiro == 0:
                print('Você venceu!')
                return

# Executa o jogo
partida()