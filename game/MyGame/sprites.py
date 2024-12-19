#importing necessary modules
import pygame as pg
import random

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

#constants
cell_size = 40
cell_number = 20

#the main class with the main game functions
class Main:
    #the init function initializes the class 
    def __init__(self):
        
        self.snake = Snake()
        self.fruit = Fruit()

    #the draw_items function creates the different elements on the screen
    def draw_items(self):
       
       #drawing the grass, fruit, and snake on the screen
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    #the check_collision function checks if the snake colides with a fruit

    def check_collision(self):

        #if the snake touches a fruit
        if self.fruit.pos == self.snake.body[0]:
            #spawn the fruit at another location
            self.fruit.randomize()
            #make the snake longer (add a block to the snake's length)
            self.snake.add_block()

    #the check_fail function checks if the snake is touching itself
    def check_fail(self):
        
        #using if statements to determine if the snake is touching itself, and then ending the game if it is
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    #the draw_grass function creates the grass in a specific pattern on the screen
    def draw_grass(self):

        #setting grass color
        grass_color = (167, 209, 61)
        #creating an alternating pattern of checkered squares using rows and columns
        for row in range(cell_number):
            for col in range(cell_number):
                if (row + col) % 2 == 0:
                    #drawing the grass squares
                    grass_rect = pg.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pg.draw.rect(pg.display.get_surface(), grass_color, grass_rect)

    #the game_over functions specifies what to do if the snake dies
    def game_over(self):
 
        #quiting the game and exiting
        pg.quit()
        exit()

#the snake class includes all the functions related to the snake
class Snake:
    #the __init__ function initializes the class and starts creating the snake body
    def __init__(self):
        self.body = [pg.Vector2(5, 10), pg.Vector2(4, 10), pg.Vector2(3, 10)] 
        self.direction = pg.Vector2(1, 0)  
        self.new_block=False

    #the draw_snake function completely draws the snake
    def draw_snake(self):
 
        #creating a generic block that can be used multiple times to form the snake's 
        # body and can be used to lengthen the snake
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pg.Rect(x_pos, y_pos, cell_size, cell_size)
            #using the pg.draw.rect function to draw the snake body
            pg.draw.rect(pg.display.get_surface(), (183, 191, 122), block_rect) 

    #the move_snake function shifts the snake's body to give the appearance of movement
    def move_snake(self):

        #if a new block is beng added to the snake's body
        if self.new_block:
            #adding a new block to the snake
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            #moving the snake in the appropriate direction
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    #the add_block function allows the snake to grow
    def add_block(self):

        #changes the boolean value to True
        self.new_block = True

#the Fruit class includes everything related to the fruit
class Fruit:
    #the __init__ function initializes the class
    def __init__(self):
   
        #placing the fruit in a random position
        self.randomize()

    #the draw fruit funciton creates the fruit on the screen
    def draw_fruit(self):
    
        #using pygame functions to draw the fruit
        fruit_rect = pg.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pg.draw.rect(pg.display.get_surface(), (126, 166, 114), fruit_rect)

    #the randomize function sends the fruit to a random position
    def randomize(self):
    
        #sending the fruit to random coordinates
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pg.Vector2(self.x, self.y)