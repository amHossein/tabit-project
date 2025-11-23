import pygame
from abc import ABC, abstractmethod


class BTNBase(pygame.sprite.Sprite, ABC):
    def __init__(self,command:function=None):
        super().__init__()        
        self.on_click = command
        
        self.state = "NORMAL"
        self.pressed = False
    
    @staticmethod
    def convert_pos(pos:tuple[int,int], offsets:tuple[int,int]):
        """
        to fix frame positioning
        actually buttons collision is counted relative to main screen surface
        but to fix it i convert cursor position for when widget is inside frame
        
        :param pos: cursor position by `pygame.event`
        :param offsets: the difference between main pos and frame pos
        
        :return: exact position where cursor can find widget
        """
        return (pos[0]-offsets[0] ,pos[1]-offsets[1])
        
    
    def events(self, event:pygame.event.Event, frame_offsets:tuple[int,int] = (0,0)):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            cursor_pos = self.convert_pos((event.pos[0],event.pos[1]), frame_offsets) 
            if self.rect.collidepoint(cursor_pos):
                self.pressed = True
                self.state = "PRESS"
                
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            cursor_pos = self.convert_pos((event.pos[0],event.pos[1]), frame_offsets) 
            if self.rect.collidepoint(cursor_pos):
                self.curr_time = pygame.time.get_ticks()
                if self.on_click and self.pressed:
                    self.on_click()
                self.pressed = False
            if self.rect.collidepoint(cursor_pos):
                self.state = "HOVER"
            else:
                self.state = "NORMAL"
                
        if event.type == pygame.MOUSEMOTION:    
            cursor_pos = self.convert_pos((event.pos[0],event.pos[1]), frame_offsets)            
            if self.rect.collidepoint(cursor_pos):
                if not self.pressed:
                    self.state = "HOVER"
            else:
                self.state = "NORMAL"
                
                
    @abstractmethod  
    def blits(self):
        pass
    