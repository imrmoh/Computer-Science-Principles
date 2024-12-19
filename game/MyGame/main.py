
#importing the necessary modules
import pygame as pg
import sys
#importing the main class from sprites and importing settings
from sprites import Main 
from settings import *

#source: https://www.youtube.com/watch?v=QFvqStqPCRU

'''
goal: collect as many fruits as possible
rules: cannot go out of bounds, can only move in specific directions
feedback: snake gets longer as it eats more fruit. Fruit respawns when snake eats it at different location.
freedom: player can choose to move in 4 directions
'''

#source: ChatGPT: "Could you split the code up into 2 files, 
#one main file and one file for the game sprites, 
#Could you split the code up into 2 files, one main file and one file for the game sprites,
# but split the code up so that the game still works"

#creating the pygame screen
screen = pg.display.set_mode((cell_number * cell_size, cell_number * cell_size))

#creating the game class with all the main functions
class Game:
    #initializing the game class with the __init__ function
    def __init__(self):
        pg.init()
        #starting the clock
        self.clock = pg.time.Clock()
        self.main_game = Main()  
        self.screen = pg.display.set_mode((800, 800))
        #doing the tasks necessary to set up/initialize the game

    #the update function allows the game to always update itself so that the game screen is always changing
    def update(self):
        #updating the game screen by redrawing items
        screen.fill((175, 215, 70)) 
        self.main_game.draw_items()  
        pg.display.update()

    #the run function runs the game loop
    def run(self):
        #while True indicates the loop is always running
        while True:
            #always running the game events
            self.events()
            #always running the game
            self.update()
            #always running the clock
            self.clock.tick(60)  

    #the events function checks for key events, like key presses or the user quitting the game
    def events(self):
        #checking for events
        for event in pg.event.get():
            #checking if the user quits the game
            if event.type == pg.QUIT:
                #exiting and quiting the game if the player quits
                pg.quit()
                sys.exit()
            #checking if the player is pressing the key
            if event.type == pg.KEYDOWN:
                #checking if the player presses the up arrow
                if event.key == pg.K_UP:
                    #checking to make sure the snake isn't pointing in a specific direction
                    if self.main_game.snake.direction.y != 1:
                        #poining the snake upward
                        self.main_game.snake.direction = pg.Vector2(0, -1)
                #checking if the player presses the down arrow
                if event.key == pg.K_DOWN:
                    #checking to make sure the snake isn't pointing in a specific direction
                    if self.main_game.snake.direction.y != -1:
                        #pointing the snake downward
                        self.main_game.snake.direction = pg.Vector2(0, 1)
                #checking if the player presses the right arrow
                if event.key == pg.K_RIGHT:
                    #checking to make sure the snake isn't pointing in a specific direction
                    if self.main_game.snake.direction.x != -1:
                        #pointing the snake to the right
                        self.main_game.snake.direction = pg.Vector2(1, 0)
                #checking if the player presses the left arrow
                if event.key == pg.K_LEFT:
                    #checking to make sure the snake isn't pointing in a specific direction
                    if self.main_game.snake.direction.x != 1:
                        #pointing the snake to the left
                        self.main_game.snake.direction = pg.Vector2(-1, 0)

            #checking if the user interacts with a game
            if event.type == pg.USEREVENT:
                #moving the snake
                self.main_game.snake.move_snake()  
                #checking if the snake collides with a fruit
                self.main_game.check_collision()
                #checking if the snake collides with itself
                self.main_game.check_fail()


pg.init()
pg.time.set_timer(pg.USEREVENT, 150) 

#checking the file name
if __name__ == "__main__":
    #running the game loop
    game = Game()
    game.run()