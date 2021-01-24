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
    
    # Рисование кнопки
    def draw(self, screen):
        #            экран   цвет         координаты      ширина      высота
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def is_click(self):
        pass
    def do(self):
        pass
    
    def jumpto(self, x, y):
        self.x = x
        self.y = y
    
    def set_text(self, text):
        self.text = text
        
    def set_color(self, color):
        self.color = color
        
    def set_size(self, width, height):
        self.width = width
        self.height = height

btn_yes = Button("YES", color.RED, 100, 100, 100, 30)

FPS = 30

pg.init()
screen = pg.display.set_mode((Window.width, Window.height))
clock = pg.time.Clock()

running = True
while running:
    screen.fill(color.WHITE)
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
   
    btn_yes.draw(screen)
    pg.display.update()
pg.quit()