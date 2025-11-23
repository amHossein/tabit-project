# a simple window
import pygame
from pygame.constants import *

pygame.init()

pygame.display.set_caption("Empty Window")
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

def update():
    screen.fill(pygame.Color("Black"))
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            running = not running
    
    update()
    clock.tick(60)

pygame.quit()