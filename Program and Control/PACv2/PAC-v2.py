import pygame
import sys

# Inicializa o Pygame
pygame.init()

def jogo():
    # Configurações da tela
    tamanho_celula = 40
    largura_tela = 640 + 2 * tamanho_celula  # 2 colunas adicionais à direita
    altura_tela = 480 + 4 * tamanho_celula  # 3 linhas adicionais abaixo
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('Pac-Man em Python')

    # Carrega as imagens e redimensiona para o tamanho da célula
    pacman = pygame.image.load('pacman.png')
    pacman = pygame.transform.scale(pacman, (tamanho_celula, tamanho_celula))

    # Carregando diferentes sprites de fantasmas
    fantasma_azul = pygame.image.load('fantasma_azul.png')
    fantasma_azul = pygame.transform.scale(fantasma_azul, (tamanho_celula, tamanho_celula))

    fantasma_vermelho = pygame.image.load('fantasma_vermelho.png')
    fantasma_vermelho = pygame.transform.scale(fantasma_vermelho, (tamanho_celula, tamanho_celula))

    fantasma_rosa = pygame.image.load('fantasma_rosa.png')
    fantasma_rosa = pygame.transform.scale(fantasma_rosa, (tamanho_celula, tamanho_celula))

    parede = pygame.image.load('parede.png')
    parede = pygame.transform.scale(parede, (tamanho_celula, tamanho_celula))

    # Define a matriz do labirinto
    labirinto = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],   
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],   
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],   
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],   
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],  
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],  
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],  
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1], 
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], 
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    ]

    # Posição inicial do Pac-Man e direção inicial
    pacman_pos = [40, 40]
    pacman_direcao = pygame.K_RIGHT  # Direção inicial do Pac-Man

    # Posições iniciais e sprites dos fantasmas
    fantasmas = [
        {'pos': [320, 280], 'sprite': fantasma_azul},   # Fantasma azul
        {'pos': [360, 280], 'sprite': fantasma_vermelho}, # Fantasma vermelho
        {'pos': [400, 280], 'sprite': fantasma_rosa},   # Fantasma rosa
    ]

    # Configura o tempo para a movimentação
    clock = pygame.time.Clock()
    tickrate = 1  # Quantidade de movimentos por segundo (1 movimento por segundo)
    ultima_movimentacao = pygame.time.get_ticks()  # Tempo da última movimentação

    def desenha_labirinto():
        for linha in range(len(labirinto)):
            for coluna in range(len(labirinto[linha])):
                x = coluna * tamanho_celula
                y = linha * tamanho_celula

                if labirinto[linha][coluna] == 1:
                    tela.blit(parede, (x, y))

    def atualiza_posicao():
        nova_pos = pacman_pos[:]
        if pacman_direcao == pygame.K_LEFT:
            nova_pos[0] -= tamanho_celula
        elif pacman_direcao == pygame.K_RIGHT:
            nova_pos[0] += tamanho_celula
        elif pacman_direcao == pygame.K_UP:
            nova_pos[1] -= tamanho_celula
        elif pacman_direcao == pygame.K_DOWN:
            nova_pos[1] += tamanho_celula

        # Verifica se a nova posição é válida
        linha = nova_pos[1] // tamanho_celula
        coluna = nova_pos[0] // tamanho_celula
        if 0 <= linha < len(labirinto) and 0 <= coluna < len(labirinto[linha]):
            if labirinto[linha][coluna] != 1:
                pacman_pos[:] = nova_pos
            else:
                # Se houver parede, não move Pac-Man
                pass

    def verifica_colisao():
        for fantasma in fantasmas:
            if pacman_pos == fantasma['pos']:
                print("Colisão com o fantasma!")
                restart = int(input("Deseja reiniciar o jogo? Digite 1 para reiniciar ou qualquer outro número para parar: "))
                if restart == 1:
                    jogo()  # Reinicia o jogo chamando a função do jogo
                else:
                    pygame.quit()
                    sys.exit()  # Sai do jogo corretamente

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    pacman_direcao = event.key

        # Atualiza a posição do Pac-Man a cada segundo
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - ultima_movimentacao >= 1000 / tickrate:
            atualiza_posicao()
            ultima_movimentacao = tempo_atual

        verifica_colisao()
        tela.fill((0, 0, 0))
        desenha_labirinto()
        tela.blit(pacman, pacman_pos)
        for fantasma in fantasmas:
            tela.blit(fantasma['sprite'], fantasma['pos'])
        pygame.display.update()
        clock.tick(60)  # Define o frame rate para 60 FPS

jogo()
