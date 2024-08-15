import pygame
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Inicializa o Pygame
pygame.init()

# Caminho da pasta de imagens
pasta_sprites = os.path.join(os.path.dirname(__file__), 'Sprites')

def carregar_gif(nome_arquivo):
    gif = Image.open(nome_arquivo)
    frames = []
    try:
        while True:
            frame = ImageTk.PhotoImage(gif.copy())
            frames.append(frame)
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass
    return frames

def mostrar_mensagem():
    # Cria uma janela tkinter oculta
    root = tk.Tk()
    root.title("Pac-Man")
    
    # Define o tamanho da janela
    root.geometry("498x280")
    
    # Cria um Canvas para adicionar o GIF e os botões
    canvas = tk.Canvas(root, width=498, height=280)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Caminho do GIF
    caminho_gif = os.path.join(pasta_sprites, 'pacman_background.gif')

    # Carrega e exibe o GIF animado
    try:
        frames = carregar_gif(caminho_gif)  # Certifique-se de ter um GIF animado
        imagem_gif = canvas.create_image(0, 0, anchor=tk.NW, image=frames[0])
        
        def atualizar_frame():
            nonlocal current_frame
            canvas.itemconfig(imagem_gif, image=frames[current_frame])
            current_frame = (current_frame + 1) % len(frames)
            root.after(100, atualizar_frame)  # Atualiza a cada 100 milissegundos

        current_frame = 0
        atualizar_frame()
    except IOError:
        pass

    # Cria um título
    titulo = tk.Label(root, text="Colidiu com o fantasma!", font=('Helvetica', 14, 'bold'), fg='yellow', bg='black')
    canvas.create_window(250, 60, window=titulo)

    # Cria uma mensagem
    mensagem = tk.Label(root, text="Deseja reiniciar o jogo?", font=('Helvetica', 12), fg='white', bg='black')
    canvas.create_window(250, 120, window=mensagem)

    # Cria os botões de resposta
    resposta = tk.StringVar()
    def reiniciar():
        resposta.set("yes")
        root.destroy()
    
    def sair():
        resposta.set("no")
        root.destroy()

    botao_reiniciar = tk.Button(root, text="Reiniciar", command=reiniciar, bg='yellow', fg='black')
    canvas.create_window(175, 220, window=botao_reiniciar)

    botao_sair = tk.Button(root, text="Sair", command=sair, bg='red', fg='white')
    canvas.create_window(325, 220, window=botao_sair)

    root.mainloop()
    
    return resposta.get() == "yes"

def jogo():
    # Configurações da tela
    tamanho_celula = 40
    largura_tela = 640 + 2 * tamanho_celula  # 2 colunas adicionais à direita
    altura_tela = 480 + 4 * tamanho_celula  # 3 linhas adicionais abaixo
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption('Pac-Man em Python')

    # Carrega as imagens e redimensiona para o tamanho da célula
    caminho_pacman = os.path.join(pasta_sprites, 'pacman.png')
    pacman = pygame.image.load(caminho_pacman)
    pacman = pygame.transform.scale(pacman, (tamanho_celula, tamanho_celula))

    # Carregando diferentes sprites de fantasmas
    caminho_fantasma_azul = os.path.join(pasta_sprites, 'fantasma_azul.png')
    fantasma_azul = pygame.image.load(caminho_fantasma_azul)
    fantasma_azul = pygame.transform.scale(fantasma_azul, (tamanho_celula, tamanho_celula))

    caminho_fantasma_vermelho = os.path.join(pasta_sprites, 'fantasma_vermelho.png')
    fantasma_vermelho = pygame.image.load(caminho_fantasma_vermelho)
    fantasma_vermelho = pygame.transform.scale(fantasma_vermelho, (tamanho_celula, tamanho_celula))

    caminho_fantasma_rosa = os.path.join(pasta_sprites, 'fantasma_rosa.png')
    fantasma_rosa = pygame.image.load(caminho_fantasma_rosa)
    fantasma_rosa = pygame.transform.scale(fantasma_rosa, (tamanho_celula, tamanho_celula))

    caminho_parede = os.path.join(pasta_sprites, 'parede.png')
    parede = pygame.image.load(caminho_parede)
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
    tickrate_ms = 650  # Atualiza a cada 500 milissegundos
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
                if mostrar_mensagem():
                    return True  # Reinicia o jogo
                else:
                    pygame.quit()
                    sys.exit()  # Sai do jogo corretamente
        return False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    pacman_direcao = event.key

        # Atualiza a posição do Pac-Man a cada 650 milissegundos
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - ultima_movimentacao >= tickrate_ms:
            atualiza_posicao()
            ultima_movimentacao = tempo_atual

        if verifica_colisao():
            jogo()  # Reinicia o jogo

        tela.fill((0, 0, 0))
        desenha_labirinto()
        tela.blit(pacman, pacman_pos)
        for fantasma in fantasmas:
            tela.blit(fantasma['sprite'], fantasma['pos'])
        pygame.display.update()
        clock.tick(60)  # Define o frame rate para 60 FPS

jogo()


