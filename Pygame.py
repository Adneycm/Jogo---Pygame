# Design de Software
# Projeto - Pygame
# Professor: Luciano Soares
# Grupo: Adney Costa, Ricardo Mourão e Ykaro Andrade
# Turma 1A - 2020.2

# Blibiotecas importadas
import pygame

# Inicializando o Pygame
pygame.init()

""" Gerando Tela de início do jogo """
"""
tela = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Pygame')

# Inicia estruturas de dados
game = True

# Inicia assets
font = pygame.font.SysFont(None, 48)
ModSim = font.render('ModSim', True, (255, 255, 255))
cat = font.render("CAT", True, (255, 255, 255))
# Loop principal
while game:
    # Trata eventos
    for event in pygame.event.get():
        # Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    tela.fill((0, 0, 0))  # Preenche com a cor branca
    tela.blit(ModSim, (180, 200))
    tela.blit(cat, (210,250))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
"""
