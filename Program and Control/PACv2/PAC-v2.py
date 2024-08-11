import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 640
altura_tela = 480
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Pac-Man em Python')

# Configurações do labirinto
tamanho_celula = 40

# Carrega as imagens e redimensiona para o tamanho da célula
pacman = pygame.image.load('pacman.png')
pacman = pygame.transform.scale(pacman, (tamanho_celula, tamanho_celula))

fantasma = pygame.image.load('fantasma.png')
fantasma = pygame.transform.scale(fantasma, (tamanho_celula, tamanho_celula))

parede = pygame.image.load('parede.png')
parede = pygame.transform.scale(parede, (tamanho_celula, tamanho_celula))

# Define a matriz do labirinto
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
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
            elif labirinto[linha][coluna] == 2:
                tela.blit(pacman, pacman_pos)
            elif labirinto[linha][coluna] == 3:
                tela.blit(fantasma, fantasma_pos)

def atualiza_posicao(tecla):
    if tecla == pygame.K_LEFT:
        pacman_pos[0] -= tamanho_celula
    elif tecla == pygame.K_RIGHT:
        pacman_pos[0] += tamanho_celula
    elif tecla == pygame.K_UP:
        pacman_pos[1] -= tamanho_celula
    elif tecla == pygame.K_DOWN:
        pacman_pos[1] += tamanho_celula

def jogo():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                atualiza_posicao(event.key)

        tela.fill((0, 0, 0))
        desenha_labirinto()
        tela.blit(pacman, pacman_pos)
        tela.blit(fantasma, fantasma_pos)
        pygame.display.update()

jogo()
