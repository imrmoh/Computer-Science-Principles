
#importing all necessary modules and libraries
import pygame as pg
import sys
from snakesettings import *
from pygame.math import Vector2
import random
#source: https://www.youtube.com/watch?v=QFvqStqPCRU

'''
goal: collect as many fruits as possible
rules: cannot go out of bounds, can only move in specific directions
feedback: snake gets longer as it eats more fruit. Fruit respawns when snake eats it at different location.
freedom: player can choose to move in 4 directions
'''

#point left off at: https://youtu.be/QFvqStqPCRU?t=4699

#move code to downloads
apple = pg.image.load('Downloads/apple.png').convert_alpha()
#setting the cell number and size vars
cell_size = 40
cell_number = 20

#creating a pygame screen
screen=pg.display.set_mode((cell_number * cell_size,cell_number * cell_size))

#creating the snake sprite
class SNAKE:
    #initializing the snake class
    def __init__(self):
        #creating the snake body as being at specific positions
        self.body=[Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        #orienting the snake initially
        self.direction=Vector2(1, 0)
        self.new_block = False

    #draw_snake creates the snake sprite on the screen
    def draw_snake(self):
        #creating the snake out of different blocks
        for block in self.body:
            #ensuring that the blocks are the correct size
            x_pos=int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            #creating the snake as a whole
            block_rect=pg.Rect(x_pos, y_pos, cell_size, cell_size)
            #drawing the blocks to create the snake
            pg.draw.rect(screen, (183,191,122), block_rect)

    #creating the illusion of the snake moving
    def move_snake(self):
        if self.new_block == True:
            body_copy=self.body[:-1]
            #moving the squares of the snake to a different position
            body_copy.insert(0, body_copy[0] + self.direction)
            #making a copy of the body and moving it to the new location
            self.body=body_copy[:]
            self.new_block = False
        else:
            body_copy=self.body[:-1]
            #moving the squares of the snake to a different position
            body_copy.insert(0, body_copy[0] + self.direction)
            #making a copy of the body and moving it to the new location
            self.body=body_copy[:]

    def add_block(self):
        self.new_block = True

#the fruit class
class FRUIT:
    #initializing the fruit class
    def __init__(self):
        #placing the fruit at a random point by giving it random x and y coordinates
        self.x= random.randint(0, cell_number -1)
        self.y=random.randint(0, cell_number -1)
        #establising the position of the fruit
        self.pos=Vector2(self.x, self.y)
    #making the furit appear on the screen

    def draw_fruit(self):
        #creating a rectangle for the fruit with the right position and size
        fruit_rect=pg.Rect(int(self.pos.x*cell_size), int(self.pos.y*cell_size), cell_size, cell_size)
        #drawing the fruit rectangle on the screen
        screen.blit(apple, fruit_rect)
        #pg.draw.rect(screen, (126, 166, 114), fruit_rect)
        #updating the pygame display
        pg.display.flip()

    #the randomize function moves the fruit to a random position
    def randomize(self):
        #changing the x and y coordinates of the fruit to a random location
        self.x=random.randint(0, cell_number -1)
        self.y=random.randint(0, cell_number -1)
        #changing the fruit's position
        self.pos=Vector2(self.x, self.y)

    #the add_block function will make the snake longer
    def add_block(self):
        pass

#the main class
class MAIN:
    #initializing the main class
    def __init__(self):
        #initializing the main class
        self.snake=SNAKE()
        self.fruit=FRUIT()

    #update function, ensures that the snake's position can update
    def update(self):
        #allows the snake to move
        self.snake.move_snake()
        self.check_fail()

    #the draw_items function draws the fruit and draws the snake
    def draw_items(self):
        #using the draw_fruit and draw_snake functions to create the fruit and snake
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    #checks if the snake has collided with the fruit
    def check_collision(self):
        #the if statement checks if the fruit and snake's positions are the same
        if self.fruit.pos == self.snake.body[0]:
            #moving the fruit to a random position
            self.fruit.randomize()
            #adding a block to the end of the snake to make it longer
            self.snake.add_block
    MAIN.draw_items()

    def check_fail(self):
        #check if snake meets conditions to die
        #check if snake is outside of screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        #checking if the snake colides with itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                #ending the game if the snake collides with itself
                self.game_over()
        
    def draw_grass(self):
        grass_color=(167,209,61)
        for row in range(cell_number):
            if row%2 == 0:
                for col in range(cell_number):
                    if col%2 == 0:
                        grass_rect=pg.Rect(col*cell_size, row*cell_size, cell_size, cell_size)
                        pg.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col%2 != 0:
                        grass_rect=pg.Rect(col*cell_size, row*cell_size, cell_size, cell_size)
                        pg.draw.rect(screen, grass_color, grass_rect)


#the game over function ends the game
    def game_over(self):
        pg.quit()
        sys.exit()
        



pg.init()

