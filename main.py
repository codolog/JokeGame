import pygame as pg

class Window:
    width = 640
    height = 480
    
class Button:
    def __init__(self):
        pass
    def draw(self):
        pass
    def is_click(self):
        pass
    def do(self):
        pass
    def set_text(self):
        pass
    def set_color(self):
        pass
    def set_size(self):
        pass

FPS = 30

pg.init()
screen = pg.display.set_mode((Window.width, Window.height))
clock = pg.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()