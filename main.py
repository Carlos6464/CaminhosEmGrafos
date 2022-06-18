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

class personagem(pygame.sprite.Sprite):
      def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.sprites = []
          self.sprites.append(pygame.image.load('sprites/parado/Idle1.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle2.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle3.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle4.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle5.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle6.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle7.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle8.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle9.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle10.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle11.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle12.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle13.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle14.png'))
          self.sprites.append(pygame.image.load('sprites/parado/Idle15.png'))
          self.atual = 0
          self.image = self.sprites[self.atual]
          self.image = pygame.transform.scale(self.image, (614/7, 564/7))

         
          self.rect = self.image.get_rect()
          self.rect.topleft = 100, 100

todas = pygame.sprite.Group()
Personagem = personagem()
todas.add(Personagem)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    mapa.blit(imagemFundo, (0,0))
    todas.draw(mapa)
    todas.update()
    pygame.display.update()
