#PROGRAM AND CONTROL

import pygame
pygame.init()

# Configurações da tela
largura_tela = 640
altura_tela = 480
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Pac-Man em Python')


# Carrega as imagens
pacman = pygame.image.load('pacman.png')
fantasma = pygame.image.load('fantasma.png')
parede = pygame.image.load('parede.png')


pacman_pos = [largura_tela//2, altura_tela//2]
fantasma_pos = [100, 100]
parede_pos = [[10, 50], [100, 50], [200, 50], [300, 50], [400, 50], [500, 50]]


#PORQUÊ SENHOR? ESTE CODIGO ABAIXO DÁ TANTO PROBLEMA??? :(

def desenha_cena():
    tela.fill((0, 0, 0))  # Preenche a tela com a cor preta

    # Desenha o Pac-Man na posição atual
    tela.blit(pacman, pacman_pos)

    # Desenha o fantasma na posição atual
    tela.blit(fantasma, fantasma_pos)

    # Desenha as paredes na posição atual
    for pos in parede_pos:
        tela.blit(parede, pos)


def atualiza_posicao(tecla):
    if tecla == pygame.K_LEFT:
        pacman_pos[0] -= 10
    elif tecla == pygame.K_RIGHT:
        pacman_pos[0] += 10
    elif tecla == pygame.K_UP:
        pacman_pos[1] -= 10
    elif tecla == pygame.K_DOWN:
        pacman_pos[1] += 10


def jogo():
    while True:
        # Verifica se houve eventos (teclado, mouse, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                atualiza_posicao(event.key)

        # Desenha a cena na tela
        desenha_cena()

        # Atualiza a tela
        pygame.display.update()

jogo()
