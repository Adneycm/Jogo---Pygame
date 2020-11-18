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

# Definindo a imagem de fundo 
largura_tela= 500
altura_tela= 600
tela = pygame.display.set_mode( (largura_tela,altura_tela) )
imagem_de_fundo = pygame.image.load("c:/Users/adney/OneDrive/Documentos/1° semestre - Insper/Desing de Software/Imagens Pygame/predio1.png").convert()
imagem_de_fundo1 = pygame.image.load("c:/Users/adney/OneDrive/Documentos/1° semestre - Insper/Desing de Software/Imagens Pygame/predio2.png").convert()
imagem_de_fundo = pygame.transform.scale(imagem_de_fundo, (largura_tela, altura_tela))
imagem_de_fundo1 = pygame.transform.scale(imagem_de_fundo1, (largura_tela, altura_tela))
y_imagem_de_fundo= 0
y_imagem_de_fundo1= altura_tela


# Definindo as figuras do jogo
""" Gato """
largura_gato = 50
altura_gato = 38
gato_imagem = pygame.image.load('c:/Users/adney/OneDrive/Documentos/1° semestre - Insper/Desing de Software/Imagens Pygame/cat.png').convert_alpha()
gato_imagem = pygame.transform.scale(gato_imagem, (largura_gato,altura_gato) )
""" Objetos """
largura_objetos = 50
altura_objetos = 38
#objeto_imagem = pygame.image.load('c:/Users/adney/OneDrive/Documentos/1° semestre - Insper/Desing de Software/Imagens Pygame/flyingbird').convert_alpha()
#objeto_imagem = pygame.transform.scale(objeto_imagem, (largura_objetos,altura_objetos) )