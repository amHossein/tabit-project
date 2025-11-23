import pygame
from tabit.ui import theme
from tabit.ui.widgets import button, button_add


class Color:
    def __init__(self, r:int, g:int, b:int):
        self.r = r
        self.g = g
        self.b = b
    
    
class Point: #struct
    def __init__(self,x:int,y:int,):
        self.x = x
        self.y = y
        
    
class Frame(pygame.Surface):
    def __init__(self, surface:pygame.Surface, size:Point=(10,10), x:int = 10, y:int = 10, bg:Color=(pygame.Color("Black"))):
        super().__init__(size,pygame.SRCALPHA)
        self.bg = bg
        self.fill(self.bg)
        self.surface = surface

        self.rect = pygame.rect.Rect((x,y),size)

        self.widgets = dict()
        self.widgets_count = 0
        
        
    def add_widget(self,widget:pygame.sprite.Sprite): # TODO add feature to add multiple widgets at once
        self.widgets_count += 1
        self.widgets[self.widgets_count] = widget

            
    def events(self,event):
        self.fill(self.bg)
        for key,widget in self.widgets.items():
            widget.events(event, frame_offsets=(self.rect.x, self.rect.y))
            widget.blits()
        
        
    def blits(self):
        self.surface.blit(self, self.rect)
        
        
        

if __name__ == "__main__":
    pygame.init()
    demo_screen = pygame.display.set_mode((400,400))
    
    frame = Frame(demo_screen,(140, 160), x=100, y=200)
    btn1 = button.Button(frame, 100 , 50 , 20 , 20, "BTN", command=lambda : print("BTN"))
    btn2 = button_add.ButtonAdd(frame,50,120, lambda: print("Add"))
    frame.add_widget(btn1)
    frame.add_widget(btn2)
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break;
        
        demo_screen.fill(theme.CLR_SPACE_GREY)
        frame.events(event)
        frame.blits()
        pygame.display.update()