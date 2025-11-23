import pygame
from tabit.ui import theme

if __name__ == "__main__":
    pygame.init()
    demo_screen = pygame.display.set_mode((400,400))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break;
            
        demo_screen.fill(theme.CLR_SPACE_GREY)
        pygame.display.update()