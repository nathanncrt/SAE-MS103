import pygame
from pygame.locals import *
import numpy
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Dessiner avec pygame')
couleurs = numpy.random.randint(0, 255, size=(4,3))
BLANC = (255, 255, 255)
screen.fill(BLANC)
pygame.draw.circle(screen, couleurs[0], (200,200), 25, 0)
pygame.draw.line(screen, couleurs[1], (0, 0),(200, 200), 3)
pygame.draw.rect(screen, couleurs[2], (200, 0,100, 100))
pygame.draw.ellipse(screen, couleurs[3], (100,300, 100, 50), 2)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()