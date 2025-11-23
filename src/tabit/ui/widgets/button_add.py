import pygame
from tabit.ui.widgets.base import button_base
from tabit.utils import load
from tabit.ui import theme


class ButtonAdd(button_base.BTNBase):
    def __init__(self,surface:pygame.Surface, x:int=10, y:int=10, command:function=None):
        super().__init__(command)
        self.button_images = {
            "NORMAL": load.load_image("add-button","normal.png"),
            "HOVER": load.load_image("add-button","hover.png"),
            "PRESS": load.load_image("add-button","press.png")
        }

        
        self.surface = surface
        self.image = self.button_images["NORMAL"]
        self.rect = self.image.get_rect(topleft = (x, y))
        
    def blits(self):
        if self.state == "NORMAL":
            self.image = self.button_images[self.state]
        elif self.state == "HOVER":
            self.image = self.button_images[self.state]
        elif self.state == "PRESS":
            self.image = self.button_images[self.state]
        
        self.surface.blit(self.image, self.rect)





if __name__ == "__main__": 
    pygame.init()
    clock = pygame.time.Clock()
    demo_screen = pygame.display.set_mode((400,400))
    
    #create
    mybuttons = []
    y_pos = 40
    for i in range(5):
        btn = ButtonAdd(demo_screen, x=60, y=y_pos, command = lambda : print("+Add"))
        mybuttons.append(btn)
        y_pos += 70
        
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break;
        
        demo_screen.fill(theme.CLR_SPACE_GREY)
        
        for btn in mybuttons:
            btn.events(event)
            btn.blits()
        
        pygame.display.update()
        clock.tick(60)