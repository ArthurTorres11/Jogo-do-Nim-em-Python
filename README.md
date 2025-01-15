# Jogo do NIM

O **Jogo do NIM** é um jogo de estratégia de dois jogadores, onde o objetivo é evitar ser o jogador que tira a última peça do tabuleiro. Neste jogo, os jogadores alternam retirando entre 1 e um número máximo de peças por vez. O jogo pode ser jogado em **modo partida isolada** ou **modo campeonato**.

## Como Jogar

O jogo oferece duas opções principais:

1. **Partida Isolada**: Onde você joga uma única partida contra o computador.
2. **Campeonato**: Onde você joga três rodadas contra o computador.

No início do jogo, você define:
- O número total de peças no tabuleiro.
- O limite de peças que podem ser retiradas por jogada (de 1 até o número máximo definido).

### Regras do Jogo
- O jogador e o computador alternam as jogadas.
- Cada jogador, em sua vez, pode remover de 1 até o limite de peças por jogada.
- Quem tirar a última peça perde o jogo.
- No **modo campeonato**, o computador ganha 3 rodadas consecutivas, e o placar final será exibido.

### Funções do Código

- **computador_escolhe_jogada(n, m)**: Função que calcula qual será a jogada do computador, baseando-se no número de peças restantes no tabuleiro (`n`) e no limite de peças por jogada (`m`).
- **usuario_escolhe_jogada(n, m)**: Função que solicita ao usuário que escolha quantas peças deseja retirar, garantindo que a escolha seja válida (dentro do limite de peças).
- **partida()**: Função que executa uma partida única, controlando o fluxo do jogo entre o jogador e o computador.
- **campeonato()**: Função que gerencia o campeonato de 3 rodadas, exibindo o placar final ao término.
