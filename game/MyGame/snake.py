import pygame as pg
import sys
from snakesettings import *


pg.init()
screen=pg.display.set_mode(width, height)
clock=pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
    


                 
                 

