import pygame, sys
from classes.fps import FPS

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
fps = FPS()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()





    screen.fill((0 ,0 ,0))
    fps.rend(screen)