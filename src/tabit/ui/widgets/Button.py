import pygame
from tabit.ui.widgets.base import button_base
from tabit.utils import load
from tabit.ui import theme


class Button(button_base.BTNBase):
    def __init__(self,surface:pygame.Surface, width:int=10, height:int=10, x:int=10, y:int=10, text:str="" ,font_size:int=18, font_bold:bool=False, command:function=None):
        super().__init__(command)
        self.surface = surface
        self.background = pygame.Surface((width,height), pygame.SRCALPHA)
        
        self.image = self.background
        self.rect = self.image.get_rect(topleft = (x, y))
        
        self.font = load.load_font(font_size)
        if font_bold:
            self.font.set_bold(True)
            
        self.text = self.font.render(text,True,theme.CLR_SPACE_GREY)
        self.text_rect = self.text.get_rect() # pos relates to self.image pos
        self.text_rect.topleft = ((width//2)-(self.text_rect.w//2),(height//2)-(self.text_rect.h//2))
        
        
    def blits(self):
        self.image = self.background
        
        if self.state == "NORMAL":
            self.image.fill(theme.BTN_CLR_NORMAL)
        elif self.state == "HOVER":
            self.image.fill(theme.BTN_CLR_HOVER)
        elif self.state == "PRESS":
            self.image.fill(theme.BTN_CLR_PRESS)
        
        self.image.blit(self.text, self.text_rect)    
        self.surface.blit(self.image, self.rect)
        
        
        
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
        button1.blits()
        
        button2.events(event)
        button2.blits()

        button3.events(event)
        button3.blits()
        
        pygame.display.update()
        clock.tick(60)