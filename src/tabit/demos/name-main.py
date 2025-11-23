import pygame

if __name__ == "__main__":
    pygame.init()
    demo_screen = pygame.display.set_mode((400,400))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break;