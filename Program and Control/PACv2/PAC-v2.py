import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
tamanho_celula = 40
# Aumenta a largura e altura da tela para acomodar as novas colunas e linhas
largura_tela = 640 + 2 * tamanho_celula  # 2 colunas adicionais à direita
altura_tela = 480 + 3 * tamanho_celula  # 3 linhas adicionais abaixo
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Pac-Man em Python')

# Carrega as imagens e redimensiona para o tamanho da célula
pacman = pygame.image.load('pacman.png')
pacman = pygame.transform.scale(pacman, (tamanho_celula, tamanho_celula))

fantasma = pygame.image.load('fantasma.png')
fantasma = pygame.transform.scale(fantasma, (tamanho_celula, tamanho_celula))

parede = pygame.image.load('parede.png')
parede = pygame.transform.scale(parede, (tamanho_celula, tamanho_celula))

# Define a matriz do labirinto (16 colunas e 12 linhas agora)
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # +2 colunas à direita
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],  # 
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],  # 
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],  # 
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],  # 
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],  # 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # +2 colunas à direita
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  #
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # +3 linhas abaixo
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  #
]

# Posição inicial do Pac-Man
pacman_pos = [40, 40]

# Posição inicial do Fantasma
fantasma_pos = [100, 100]

def desenha_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            x = coluna * tamanho_celula
            y = linha * tamanho_celula

            if labirinto[linha][coluna] == 1:
                tela.blit(parede, (x, y))

def atualiza_posicao(tecla):
    nova_pos = pacman_pos[:]

    if tecla == pygame.K_LEFT:
        nova_pos[0] -= tamanho_celula
    elif tecla == pygame.K_RIGHT:
        nova_pos[0] += tamanho_celula
    elif tecla == pygame.K_UP:
        nova_pos[1] -= tamanho_celula
    elif tecla == pygame.K_DOWN:
        nova_pos[1] += tamanho_celula

    # Cálculo da posição na matriz do labirinto
    linha = nova_pos[1] // tamanho_celula
    coluna = nova_pos[0] // tamanho_celula

    # Verifica se a nova posição é uma parede (valor 1 na matriz)
    if labirinto[linha][coluna] != 1:
        pacman_pos[:] = nova_pos

def verifica_colisao():
    if pacman_pos == fantasma_pos:
        print("Colisão com o fantasma!")
        pygame.quit()
        sys.exit()

def jogo():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                atualiza_posicao(event.key)

        verifica_colisao()
        tela.fill((0, 0, 0))
        desenha_labirinto()
        tela.blit(pacman, pacman_pos)
        tela.blit(fantasma, fantasma_pos)
        pygame.display.update()

jogo()

