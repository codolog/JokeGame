import pygame as pg
import Colors as color
import random as rnd

pg.init()
# Структура, которая хранит именованные размеры окна, px
class Window:
    width = 640
    height = 480

# Класс, описывающий все кнопки
class Button:
    isOver = False
    isDown = False
    isClick = False
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

font = pg.font.SysFont('Arial', 30)
text_question = font.render('Ты доволен зарплатой?', True, color.BLACK)
text_yes = font.render('YES', True, color.BLACK)
text_no = font.render('NO', True, color.BLACK)

btn_yes = Button("YES", color.RED, 100, 100, 100, 30)
btn_no = Button("NO", color.RED, 250, 100, 100, 30)

FPS = 30

screen = pg.display.set_mode((Window.width, Window.height))
clock = pg.time.Clock()

counter_click_yes = 0

running = True
while running:
    screen.fill(color.WHITE)
    clock.tick(FPS)

    listEvents = pg.event.get()
    for event in listEvents:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEMOTION:
            x, y = event.pos
            if btn_no.is_over(x, y) == True:
                new_x = rnd.randint(10, 300)
                new_y = rnd.randint(10, 300)
                btn_no.jumpto(new_x, new_y)
            btn_yes.isOver = btn_yes.is_over(x, y)
        if event.type == pg.MOUSEBUTTONDOWN:
            btn_yes.isDown = event.button == 1 and btn_yes.isOver
        if event.type == pg.MOUSEBUTTONUP:
            btn_yes.isClick = btn_yes.isDown and btn_yes.isOver

    if btn_yes.isClick == True:
        btn_yes.isClick = False
        counter_click_yes += 1

    if counter_click_yes == 2:
        btn_yes.color = color.GREEN
    elif counter_click_yes == 4:
        btn_yes.color = color.BLUE
    elif counter_click_yes > 5:
        counter_click_yes = 0
        btn_yes.color = color.RED
        
    screen.blit(text_question, (50, 10))
    btn_yes.draw(screen)
    btn_no.draw(screen)
    pg.display.update()
pg.quit()