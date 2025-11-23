import pygame
from abc import ABC, abstractmethod


class BTNBase(pygame.sprite.Sprite, ABC):
    def __init__(self,command:function=None):
        super().__init__()        
        self.on_click = command
        
        self.state = "NORMAL"
        self.pressed = False
        
    def events(self, event:pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.pressed = True
                self.state = "PRESS"
                
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.curr_time = pygame.time.get_ticks()
                if self.on_click and self.pressed:
                    self.on_click()
                self.pressed = False
            if self.rect.collidepoint(event.pos):
                self.state = "HOVER"
            else:
                self.state = "NORMAL"
                
        if event.type == pygame.MOUSEMOTION:                
            if self.rect.collidepoint(event.pos):
                if not self.pressed:
                    self.state = "HOVER"
            else:
                self.state = "NORMAL"
                
                
    @abstractmethod  
    def blit(self):
        pass
    