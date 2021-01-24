import pygame as pg
import Colors as color
import random as rnd

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
    
    # Находится ли мышка над кнопкой
    def is_over(self, mouse_x, mouse_y):
        if self.x < mouse_x < self.x + self.width and \
           self.y < mouse_y < self.y + self.height:
            return True
        else:
            return False
    
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
btn_no = Button("NO", color.RED, 250, 100, 100, 30)

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
        if event.type == pg.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]
            if btn_no.is_over(x, y) == True:
                new_x = rnd.randint(10, 300)
                new_y = rnd.randint(10, 300)
                btn_no.jumpto(new_x, new_y)
   
    btn_yes.draw(screen)
    btn_no.draw(screen)
    pg.display.update()
pg.quit()