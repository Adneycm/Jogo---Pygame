# Design de Software
# Projeto - Pygame
# Professor: Luciano Soares
# Grupo: Adney Costa, Ricardo Mourão e Ykaro Andrade
# Turma 1A - 2020.2

# Blibiotecas importadas
import pygame
import random
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
""" DP """
largura_DP = 50
altura_DP = 50
DP_imagem = pygame.image.load('c:/Users/adney/OneDrive/Documentos/1° semestre - Insper/Desing de Software/Imagens Pygame/DP.png').convert_alpha()
DP_imagem = pygame.transform.scale(DP_imagem, (largura_DP,altura_DP) )
""" DP` """
largura_DPlinha = 50
altura_DPlinha = 50
DPlinha_imagem = pygame.image.load('c:/Users/adney/OneDrive/Documentos/1° semestre - Insper/Desing de Software/Imagens Pygame/DP`.png').convert_alpha()
DPlinha_imagem = pygame.transform.scale(DPlinha_imagem, (largura_DPlinha,altura_DPlinha) )
""" A+ """
largura_A = 50
altura_A = 50
A_imagem = pygame.image.load('c:/Users/adney/OneDrive/Documentos/1° semestre - Insper/Desing de Software/Imagens Pygame/A+ - Sem fundo.png').convert_alpha()
A_imagem = pygame.transform.scale(A_imagem, (largura_A,altura_A) )



# Definindo as classes:
class Gato(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura_tela / 2
        self.rect.bottom = altura_tela / 2 - 180
        self.speedx = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > largura_tela:
            self.rect.right = largura_tela
        if self.rect.left < 0:
            self.rect.left = 0

class DP(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura_tela - largura_DP)
        self.rect.y = random.randint(620, 650)
        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(-4, -2)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top < 0 or self.rect.right < 0 or self.rect.left > largura_tela:
            self.rect.x = random.randint(0, largura_tela - largura_DP)
            self.rect.y = random.randint(620, 650)
            self.speedx = random.randint(-1, 1)
            self.speedy = random.randint(-4, -2)

class DPlinha(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura_tela - largura_DPlinha)
        self.rect.y = random.randint(620, 650)
        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(-4, -2)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top < 0 or self.rect.right < 0 or self.rect.left > largura_tela:
            self.rect.x = random.randint(0, largura_tela - largura_DPlinha)
            self.rect.y = random.randint(620, 650)
            self.speedx = random.randint(-1, 1)
            self.speedy = random.randint(-4, -2)

class A(pygame.sprite.Sprite):
    def _init_(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite._init_(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura_tela - largura_A)
        self.rect.y = random.randint(620,650)
        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(-4, -2)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top<0 or self.rect.right < 0 or self.rect.left > largura_tela:
            self.rect.x = random.randint(0, largura_tela - largura_A)
            self.rect.y = random.randint(620,650)
            self.speedx = random.randint(-1, 1)
            self.speedy = random.randint(-4, -2)

        
# Inicializando o jogo
jogo = True

# Lista das colisões
Vida = [0,0,0]

# Criando um grupo para cada obstáculo
all_sprites = pygame.sprite.Group()
all_dps = pygame.sprite.Group()
all_dplinhas = pygame.sprite.Group()
all_as = pygame.sprite.Group()

# Criando o jogador
gato = Gato(gato_imagem)
all_sprites.add(gato)

# Criando os obstáculos
for i in range(2):
    dp = DP(DP_imagem)
    dplinha = DPlinha(DPlinha_imagem)
    a = A(A_imagem)

    all_sprites.add(dp)
    all_sprites.add(dplinha)
    all_sprites.add(a)

    all_dps.add(dp)
    all_dplinhas.add(dplinha)
    all_as.add(a)

# Tempo para atualização de imagens
clock = pygame.time.Clock()

# Tempo para atualização de imagens
clock = pygame.time.Clock()

while jogo:
    clock.tick(200) # Grante um FPS de 300Hz
        # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            jogo = False
    # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                gato.speedx -= 5
            if event.key == pygame.K_RIGHT:
                gato.speedx += 5
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                gato.speedx += 5
            if event.key == pygame.K_RIGHT:
                gato.speedx -= 5
        # ----- Gera saídas
    
    # Chamando a função blit para que nossas imangens apareção na tela
    tela.blit(imagem_de_fundo, (0,y_imagem_de_fundo))
    tela.blit(imagem_de_fundo1, (0,y_imagem_de_fundo1))
    #tela.blit(gato_imagem, (250,300))

    # Mudando as posições da imagem de fundo para que tenhamos a impressão do gato estar caindo
    y_imagem_de_fundo -= 1
    y_imagem_de_fundo1 -= 1

    # Condicionais para que as imagens continuem aparecendo mesmo após sair da tela
    if y_imagem_de_fundo1 <= -altura_tela:
        y_imagem_de_fundo1= altura_tela

    if y_imagem_de_fundo <= -altura_tela:
        y_imagem_de_fundo= altura_tela

    # Atualizando a posição dos meteoros
    all_sprites.update()
     
     # Tratamento de colisões
    hits_dp = pygame.sprite.spritecollide(gato, all_dps, True)
    for dp in hits_dp:
        g=DP(DP_imagem)
        all_sprites.add(g)
        all_dps.add(g)
    
    hits_dplinha = pygame.sprite.spritecollide(gato, all_dplinhas, True)
    for dpl in hits_dplinha:
        h=DPlinha(DPlinha_imagem)
        all_sprites.add(h)
        all_dplinhas.add(h)
    
    hits_a = pygame.sprite.spritecollide(gato, all_as, True)
    for a in hits_a:
        i=DP(A_imagem)
        all_sprites.add(i)
        all_as.add(i)

    # Definido como fica a vida do gato após a colisão
    if len(hits_dp) >= 1:
        Vida.remove(Vida[0])

    if len(hits_dplinha) >= 1:
        Vida.remove(Vida[0])
        Vida.remove(Vida[0])

    if len(hits_a) >= 1:
        Vida.append(0)

    if len(Vida) <= 0:
        jogo = False
        
    # Desenhando os obstáculos e o gato
    all_sprites.draw(tela)

    # ----- Atualiza estado do jogo
    pygame.display.update() 
    
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados 