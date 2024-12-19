import pygame as pg
from pygame.math import Vector2
import random


# Constants
cell_size = 40
cell_number = 20
BLACK=0, 0, 0

screen = pg.display.set_mode((cell_number * cell_size, cell_number * cell_size))

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]  # Starting position
        self.direction = Vector2(1, 0)  # Initial movement direction (right)
        self.new_block = False

    def draw_snake(self):
        """Draws the snake to the screen."""
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pg.Rect(x_pos, y_pos, cell_size, cell_size)
            pg.draw.rect(screen, (183, 191, 122), block_rect)  # Snake color

    def move_snake(self):
        """Moves the snake by one unit in the current direction."""
        if self.new_block:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        """Adds a new block to the snake's body."""
        self.new_block = True


class FRUIT1:
    def __init__(self):
        """Initializes the fruit at a random position."""
        self.randomize()

    def draw_fruit(self):
        """Draws the fruit to the screen."""
        fruit_rect = pg.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pg.draw.rect(screen, (126, 166, 114), fruit_rect)

    def randomize(self):
        """Randomizes the position of the fruit."""
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

pg.display.flip()

#the fruit class
class FRUIT2:
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
        pg.draw.rect(screen, (126, 166, 114), fruit_rect)
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