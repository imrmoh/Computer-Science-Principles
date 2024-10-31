
#importing all necessary modules and libraries
import pygame as pg
import sys
from snakesettings import *
from pygame.math import Vector2
import random
from snakesprites import *
#source: https://www.youtube.com/watch?v=QFvqStqPCRU

'''
goal: collect as many fruits as possible
rules: cannot go out of bounds, can only move in specific directions
feedback: snake gets longer as it eats more fruit. Fruit respawns when snake eats it at different location.
freedom: player can choose to move in 4 directions
'''

cell_size = 40
cell_number = 20

#creating a pygame screen
screen=pg.display.set_mode((cell_number * cell_size,cell_number * cell_size))

#creating the main game class (all code here)
class Game:
    #initializing the game class
    def __init__(self):
        pg.init()
        #setting up a timer
        clock=pg.time.Clock()

    def update(self):
            #filling the screen with a specific color
            screen.fill((175, 215, 70))
            #drawing the fruit and snake
            fruit.draw_fruit()
            snake.draw_snake()
            pg.display.update()
            #starting the timer
            clock.tick(60)

    #running the classes in snakesprites
    def run():
        #creating fruit/snake
        pass

    def timer():
        #"SCREEN_UPDATE" indicates when there is a "USEREVENT"
        SCREEN_UPDATE=pg.USEREVENT
        pg.time.set_timer(SCREEN_UPDATE, 150)
        main_game = MAIN()

    def events(self):

        #main game loop, runs forever ("while True")
        while True:
            #all of the game events inside the for loop
            for event in pg.event.get():
                #if the user quits the game, quit the game and exist the system
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                #if the user presses a key, start moving the snake
                if event.type == SCREEN_UPDATE:
                    snake.move_snake()
                #if the user presses a key ... 
                if event.type == pg.KEYDOWN:
                    #changing the snake's direction to point in a different direction based on which key the user presses
                    if event.key == pg.K_UP:
                        main_game.snake.direction=Vector2(0, -1)
                    if event.key == pg.K_DOWN:
                        main_game.snake.direction=Vector2(0, 1)
                    if event.key == pg.K_RIGHT:
                        main_game.snake.direction=Vector2(1, 0)
                    if event.key == pg.K_LEFT:
                        main_game.snake.direction=Vector2(-1, 0)
                    #Vector 2 indicates the direction of the snake

#running the game class
if __name__=="__main__":
    #"calling" the Game class
    gme = Game()
    #running all the functions inside the game class
    gme.events()
    gme.timer()
    gme.update()
    #running the game
    gme.run()

 


                 
                 

