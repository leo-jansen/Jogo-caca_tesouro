import random
import pygame

matriz = ['t', 't', 't', 't'], ['b', 'b', 't', 't'], ['b', 0, 0, 0], [0, 0, 0, 0]

ma_vazia = ['[]', '[]', '[]', '[]'], ['[]', '[]', '[]', '[]'], ['[]', '[]', '[]', '[]'], ['[]', '[]', '[]', '[]']
jogadores = [["jogador 1", 0],  # jogador e pontuação
             ["jogador 2", 0]]

def quemjogaprimeiro():  # sortear quem joga primeiro
    if random.randint(0, 1) == 0:
        return 0
    else:
        return 1

def quemeojogador():
    if jogador == 0:
        return 1
    else:
        return 2

def imprimir(matriz):  # criação da matriz principal   verificar no idle
    for i in range(0, 4):
        for j in range(0, 4):
            print(matriz[i][j], end=' ')
        print()

pygame.init()  # inicia o pygame

branco = (255, 255, 255)
preto = (0, 0, 0)
largura = 1080
altura = 720
fundo_t = pygame.display.set_mode((largura, altura))  # abrir tela
imgregras = pygame.image.load('regras.png')
img0 = pygame.image.load('0.png')
img1 = pygame.image.load('1.png')
img2 = pygame.image.load('2.png')
img3 = pygame.image.load('3.png')
img4 = pygame.image.load('4.png')
imgtesouro = pygame.image.load('tesouro.png')
imgburaco = pygame.image.load('buraco.png')
imgab = pygame.image.load('abertura.png')
imglayout = pygame.image.load('layoutjogo.png')
imgvenc1 = pygame.image.load('vencedor1.png')
imgvenc2 = pygame.image.load('vencedor2.png')
imgempate = pygame.image.load('empate.png')
vetImg = [img0, img1, img2, img3, img4]  # facilitar nossa vida, que ja nao ta muito boa
pygame.display.set_caption("Caça ao tesouro")  # nome do jogo
jogador = quemjogaprimeiro()
jogada = 0  # "contador"
fonte = pygame.font.SysFont("Comic Sams MS", 30)
texto = fonte.render("Jogada " + str(jogada), False, branco)
vez = fonte.render("vez do Jogador " + str(quemeojogador()), False, branco)
pontjog1 = fonte.render("Pontuação: " + str(jogadores[0][1]), False, branco)
pontjog2 = fonte.render("Pontuação: "+ str(jogadores[1][1]), False, branco)

jogo = True
while jogo:
    fundo_t.blit(imgab,(0,0))
    for evento in pygame.event.get():
        if (evento.type == pygame.MOUSEBUTTONUP):
            x, y = pygame.mouse.get_pos()
            if (x >= 0 or y >= 0):
                jogo = False
        pygame.display.update()

jogo = True
while jogo:
    fundo_t.blit(imgregras,(0,0))
    for evento in pygame.event.get():
        if (evento.type == pygame.MOUSEBUTTONUP):
            x, y =pygame.mouse.get_pos()
            if(x>=0 or y>=0):
                jogo = False
        pygame.display.update()

for s in range(0, 100):  # sortear as "posições" dos tesouros, buracos e numeros
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    x1 = random.randint(0, 3)
    y1 = random.randint(0, 3)
    aux1 = matriz[x][y]
    matriz[x][y] = matriz[x1][y1]
    matriz[x1][y1] = aux1

for i in range(0, 4):  # verificação de tesouro na horizontal e vertical
    for j in range(0, 4):
        if matriz[i][j] == 0:
            if (j + 1) <= 3:
                if matriz[i][j + 1] == 't':
                    matriz[i][j] += 1
            if (j - 1) >= 0:
                if matriz[i][j - 1] == 't':
                    matriz[i][j] += 1
            if (i + 1) <= 3:
                if matriz[i + 1][j] == 't':
                    matriz[i][j] += 1
            if (i - 1) >= 0:
                if matriz[i - 1][j] == 't':
                    matriz[i][j] += 1

jogo = True  # "começa o jogo "

while jogo:

    for evento in pygame.event.get():
        fundo_t.blit(imglayout, (0,0))
        imprimir(ma_vazia)
        if evento.type == pygame.QUIT:  # se clicar em sair a variavel 'sair' vira falsa para quebrar  o while
            jogo = False  # quebrar o while
        if (evento.type == pygame.MOUSEBUTTONUP):  # usar o mouse
            x, y = pygame.mouse.get_pos()
            if (x > 732 or y > 552) or (x < 348 or y < 168):  # se clicar fora da matriz não bugar
                continue
            x = (x - 340) // 100
            y = (y - 160) // 100
            if ma_vazia[x][y] == matriz[x][y]:  # quebrar contagem de mesmo clique
                continue
            ma_vazia[x][y] = matriz[x][y]
            jogada = jogada + 1
            texto = fonte.render("Jogada " + str(jogada), False, branco)

            if ma_vazia[x][y] == 't':
                jogadores[jogador][1] += 100
                pontjog1 = fonte.render("Pontuação: " + str(jogadores[0][1]), False, branco)
                pontjog2 = fonte.render("Pontuação: " + str(jogadores[1][1]), False, branco)
            if ma_vazia[x][y] == 'b':
                if jogadores[jogador][1] >= 50:
                    jogadores[jogador][1] -= 50
                    pontjog1 = fonte.render("Pontuação: " + str(jogadores[0][1]), False, branco)
                    pontjog2 = fonte.render("Pontuação: " + str(jogadores[1][1]), False, branco)
                else:
                    jogadores[jogador][1] = 0
                    pontjog1 = fonte.render("Pontuação: " + str(jogadores[0][1]), False, branco)
                    pontjog2 = fonte.render("Pontuação: " + str(jogadores[1][1]), False, branco)
            if jogador == 0:  # troca a vez do jogador
                jogador = 1
            else:
                jogador = 0
            vez = fonte.render("vez do Jogador " + str(quemeojogador()), False, branco)

        for i in range(4):
            for j in range(4):
                if ma_vazia[i][j] == 't':
                    fundo_t.blit(imgtesouro, ((i * 100) + 340, (j * 100) + 160))
                elif ma_vazia[i][j] == 'b':
                    fundo_t.blit(imgburaco, ((i * 100) + 340, (j * 100) + 160))
                elif (ma_vazia[i][j] == '[]'):
                    pygame.draw.rect(fundo_t, preto, ((i * 100) + 340, (j * 100) + 160, 100, 100), 1)
                else:
                    fundo_t.blit(vetImg[ma_vazia[i][j]], ((i * 100) + 340, (j * 100) + 160))
        
        fundo_t.blit(texto, (720, 670))
        fundo_t.blit(vez,(720,630))
        fundo_t.blit(pontjog2, (840, 280))
        fundo_t.blit(pontjog1,(70,280))
        if jogada == 16:
            jogo = False
        pygame.display.update()

if jogada == 16:
    jogo = True
    while jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # se clicar em sair a variavel 'sair' vira falsa para quebrar  o while
                jogo = False
            if jogadores[0][1] > jogadores[1][1]:
                fundo_t.blit(imgvenc1, (0, 0))
            if jogadores[0][1] < jogadores[1][1]:
                fundo_t.blit(imgvenc2, (0, 0))
            if jogadores[0][1] == jogadores[1][1]:
                fundo_t.blit(imgempate, (0, 0))
        pygame.display.update()

pygame.quit()




"""
        if jogada == 16:
            if jogadores[0][1] > jogadores[1][1]:
                vencedor1 = True
                vencedor2 = False
                empate = False
                jogo = False
            elif jogadores[0][1] < jogadores[1][1]:
                vencedor2 = True
                vencedor1 = False
                empate = False
                jogo = False
            elif jogadores[0][1] == jogadores[1][1]:
                empate = True
                vencedor1 = False
                vencedor2 = False
                jogo = False

if vencedor1 == True:
    jogo = True
    while jogo:
        fundo_t.blit(imgvenc1, (0, 0))
        for evento in pygame.event.get():
            if (evento.type == pygame.MOUSEBUTTONUP):
                x, y = pygame.mouse.get_pos()
                if (x >= 0 or y >= 0):
                  jogo = False
            pygame.display.update()

elif vencedor2 == True:
    jogo = True
    while jogo:
        fundo_t.blit(imgvenc2, (0, 0))
        for evento in pygame.event.get():
            if (evento.type == pygame.MOUSEBUTTONUP):
                x, y = pygame.mouse.get_pos()
                if (x >= 0 or y >= 0):
                    jogo = False
            pygame.display.update()

elif empate == True:
    jogo = True
    while jogo:
        fundo_t.blit(imgempate,(0,0))
        for evento in pygame.event.get():
            if(evento.type == pygame.MOUSEBUTTONUP):
                x, y = pygame.mouse.get_pos()
                if (x >= 0 or y >= 0):
                    jogo = False
            pygame.display.update()
"""
