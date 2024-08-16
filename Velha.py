#Codigo criado pelo chat GPT !!!!!

# Função para criar um tabuleiro vazio (3x3)
def criar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Função para exibir o tabuleiro de forma visualmente amigável
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

# Função para verificar se um movimento é válido
def movimento_valido(tabuleiro, linha, coluna):
    # Um movimento é válido se a célula estiver dentro do tabuleiro e estiver vazia
    return 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' '

# Função para fazer um movimento no tabuleiro
def fazer_movimento(tabuleiro, linha, coluna, jogador):
    if movimento_valido(tabuleiro, linha, coluna):
        tabuleiro[linha][coluna] = jogador
        return True
    return False

# Função para verificar se um jogador venceu o jogo
def verificar_vencedor(tabuleiro, jogador):
    # Verifica todas as linhas e colunas
    for i in range(3):
        if all([celula == jogador for celula in tabuleiro[i]]):
            return True
        if all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    # Verifica as duas diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]):
        return True
    if all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True
    return False

# Função para verificar se o jogo terminou em empate
def verificar_empate(tabuleiro):
    return all([celula != ' ' for linha in tabuleiro for celula in linha])

# Função Minimax para determinar a melhor jogada
def minimax(tabuleiro, profundidade, maximizando):
    # Verifica se o jogador 'X' venceu
    if verificar_vencedor(tabuleiro, 'X'):
        return 1
    # Verifica se o jogador 'O' venceu
    if verificar_vencedor(tabuleiro, 'O'):
        return -1
    # Verifica se o jogo terminou em empate
    if verificar_empate(tabuleiro):
        return 0

    # Se for a vez do jogador maximizar (máquina - 'X')
    if maximizando:
        melhor_valor = -float('inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = 'X'
                    valor = minimax(tabuleiro, profundidade + 1, False)
                    tabuleiro[i][j] = ' '
                    melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    # Se for a vez do jogador minimizar (humano - 'O')
    else:
        melhor_valor = float('inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = 'O'
                    valor = minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[i][j] = ' '
                    melhor_valor = min(melhor_valor, valor)
        return melhor_valor

# Função para encontrar a melhor jogada para a máquina ('X')
def melhor_movimento(tabuleiro):
    melhor_valor = -float('inf')
    melhor_jogada = None
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = 'X'
                valor = minimax(tabuleiro, 0, False)
                tabuleiro[i][j] = ' '
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = (i, j)
    return melhor_jogada

# Função principal para iniciar e controlar o jogo
def jogar():
    tabuleiro = criar_tabuleiro()
    jogador_humano = '0'
    jogador_maquina = 'X'
    jogadas_restantes = 9

    while jogadas_restantes > 0:
        exibir_tabuleiro(tabuleiro)

        # Turno da máquina (X)
        if jogador_maquina == 'X':
            print("A máquina está jogando...")
            linha, coluna = melhor_movimento(tabuleiro)
            fazer_movimento(tabuleiro, linha, coluna, jogador_maquina)
            if verificar_vencedor(tabuleiro, jogador_maquina):
                exibir_tabuleiro(tabuleiro)
                print("A máquina venceu!")
                return
            # Alterna para o turno do humano
            jogador_maquina, jogador_humano = jogador_humano, jogador_maquina
            jogadas_restantes -= 1

        # Turno do jogador humano (O)
        else:
            print(f"Jogador {jogador_humano}, escolha sua jogada (linha e coluna): ")
            linha = int(input("Linha (0-2): "))
            coluna = int(input("Coluna (0-2): "))

            if fazer_movimento(tabuleiro, linha, coluna, jogador_humano):
                if verificar_vencedor(tabuleiro, jogador_humano):
                    exibir_tabuleiro(tabuleiro)
                    print("Parabéns! Você venceu!")
                    return
                # Alterna para o turno da máquina
                jogador_maquina, jogador_humano = jogador_humano, jogador_maquina
                jogadas_restantes -= 1
            else:
                print("Movimento inválido! Tente novamente.")

    exibir_tabuleiro(tabuleiro)
    print("O jogo terminou em empate!")

# Inicia o jogo
jogar()

