#Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
#Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.
#Objetivo
#Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.
#Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:
#   Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"
#   Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!"
#Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.
#Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.


def computador_escolhe_jogada(n, m):
    computador_retira_peça = 0
    estratégia_vencedora = False
    while estratégia_vencedora == False:
        if n % (m + 1) == 0:
            estratégia_vencedora = True
        else:
            computador_retira_peça += 1
            n = n - 1
    if n == 1:
        print("O computador retirou uma peça.")
    else:
        print("O computador tirou ", computador_retira_peça, "peças.")
    return computador_retira_peça

def usuario_escolhe_jogada(n, m):
    usuario_retira_peça = int(input("Quantas peças você vai tirar? "))
    while usuario_retira_peça <= 0 or usuario_retira_peça > m or usuario_retira_peça > n:
        print()
        print("Oops! Jogada inválida! Tente de novo")
        print()
        usuario_retira_peça = int(input("Quantas peças você vai tirar? "))
        print()
    if n == 1:
        print()
        print("Você tirou uma peça.")
    else:
        print()
        print("Você tirou ", usuario_retira_peça,"peças.")
    return usuario_retira_peça

def partida():
    fim_partida = False
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    jogada_computador = False
    if n % (m + 1) == 0:
        print("Você começa!")
        jogada_computador = False
    else:
        print("Computador começa!")
        jogada_computador = True
    while jogada_computador and not fim_partida:
        peças_retiradas_computador = computador_escolhe_jogada(n, m)
        n = n - peças_retiradas_computador
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        elif n > 1:
            print("Agora restam ", n, "peças no tabuleiro.")
            print()
        else:
            fim_partida = True
        peças_retiradas_usuario = usuario_escolhe_jogada(n, m)

        n = n - peças_retiradas_usuario
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        if n > 1:
            print("Agora restam ", n, "peças no tabuleiro.")
            print()
    print("Fim do jogo! O computador ganhou!")
