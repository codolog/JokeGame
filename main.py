import pygame as pg
import Colors as color

# Структура, которая хранит именованные размеры окна, px
class Window:
    width = 640
    height = 480

# Класс, описывающий все кнопки
class Button:
    # Конструктор
    def __init__(self, text, color, x, y, width, height):
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
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

btn_yes = Button("YES", color.RED, 10, 10, 100, 30)

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