import pygame
import os


PATH_FONTS = os.path.join("assets","fonts","PixeloidSans.ttf")
PATH_IMAGES = os.path.join("assets","images")

def load_font(size):
    fnt = pygame.font.Font(os.path.join(PATH_FONTS),size)
    return fnt

def load_image(*paths):
    img = pygame.image.load(os.path.join(PATH_IMAGES,*paths))
    return img