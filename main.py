from genericpath import exists
import pygame
from pygame.locals import *
from sys import exit

largura = 1280
altura = 720
mapa = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Caminhos Em Grafos')

imagemFundo = pygame.image.load('maps/mapa.png').convert_alpha()
imagemFundo = pygame.transform.scale(imagemFundo, (largura,altura))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    mapa.blit(imagemFundo, (0,0))
    pygame.display.update()
