import pygame
from tabit.ui import theme
from pygame.font import Font
from tabit.utils import load


class Button(pygame.sprite.Sprite):
    def __init__(self,surface:pygame.Surface, width:int=10, height:int=10, x:int=10, y:int=10, text:str="" ,font_size:int=18, font_bold:bool=False, command:function=None):
        super().__init__()        
        self.surface = surface
        self.command = command
        self.on_click = self.command
        
        self.background = pygame.Surface((width,height), pygame.SRCALPHA)
        
        self.image = self.background
        self.rect = self.image.get_rect(topleft = (x, y))
        
        self.font = Font(load.load_font(), font_size)
        if font_bold:
            self.font.set_bold(True)
            
        self.text = self.font.render(text,True,theme.CLR_SPACE_GREY)
        self.text_rect = self.text.get_rect() # pos relates to self.image pos
        self.text_rect.topleft = ((width//2)-(self.text_rect.w//2),(height//2)-(self.text_rect.h//2))
        
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
                
                
    def blit(self):
        self.image = self.background
        
        if self.state == "NORMAL":
            self.image.fill(theme.BTN_CLR_NORMAL)
        elif self.state == "HOVER":
            self.image.fill(theme.BTN_CLR_HOVER)
        elif self.state == "PRESS":
            self.image.fill(theme.BTN_CLR_PRESS)
        
        self.image.blit(self.text, self.text_rect)    
        self.surface.blit(self.image, self.rect)

                    

class ButtonAdd():
    # TODO
    pass






if __name__ == "__main__": 
    pygame.init()
    clock = pygame.time.Clock()
    demo_screen = pygame.display.set_mode((400,400))
    
    # create
    button1 = Button(surface=demo_screen, width=100, height=50 , text="Text", font_size=24, font_bold=True,command=lambda : print("Button One"))
    button2 = Button(demo_screen,x=100, y=120, width=250, height=50, text="This is a Text", font_size=30, command=lambda : print("Button Two"))
    button3 = Button(demo_screen,x=100, y=220, width=200, height=50, text="YO", font_size=28, command=lambda : print("YO"))
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break;
        
        demo_screen.fill(theme.CLR_SPACE_GREY)
        
        # handle events
        button1.events(event)
        # blit
        button1.blit()
        
        button2.events(event)
        button2.blit()

        button3.events(event)
        button3.blit()
        
        pygame.display.update()
        clock.tick(60)