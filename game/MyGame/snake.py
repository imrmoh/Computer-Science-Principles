import pygame as pg
import sys
from snakesettings import *
from pygame.math import Vector2
import random

class SNAKE:
    def __init__(self):
        self.body=[Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def draw_snake(self):
        for block in self.body:
            x_pos=int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            block_rect=pg.Rect(x_pos, y_pos, cell_size, cell_size)
            pg.draw.rect(screen, (183,191,122), block_rect)

class FRUIT:
    def __init__(self):
        self.x= random.randint(0, cell_number -1)
        self.y=random.randint(0, cell_number -1)
        self.pos=Vector2(self.x, self.y)
    def draw_fruit(self):
        fruit_rect=pg.Rect(int(self.pos.x*cell_size), int(self.pos.y*cell_size), cell_size, cell_size)
        pg.draw.rect(screen, (126, 166, 114), fruit_rect)

pg.init()
cell_size = 40
cell_number = 20
screen=pg.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock=pg.time.Clock()

fruit=FRUIT()
snake=SNAKE()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()
    pg.display.update()
    clock.tick(60)


                 
                 

