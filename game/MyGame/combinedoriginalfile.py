import pygame as pg
import sys
from pygame.math import Vector2
import random

# Constants
WIDTH = 800
height = 800
cell_size = 40
cell_number = 20

# Screen setup
screen = pg.display.set_mode((cell_number * cell_size, cell_number * cell_size))

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.main_game = MAIN()
        self.screen=pg.display.set_mode((800, 800))

    def update(self):
        """Updates the game screen."""
        screen.fill((175, 215, 70))  # Background color
        self.main_game.draw_items()  # Draw the snake and fruit
        pg.display.update()

    def run(self):
        """Runs the game loop."""
        while True:
            self.events()
            self.update()
            self.clock.tick(60)  # Limit to 60 frames per second

    def events(self):
        """Handles user events (key presses and quitting)."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    if self.main_game.snake.direction.y != 1:
                        self.main_game.snake.direction = Vector2(0, -1)
                if event.key == pg.K_DOWN:
                    if self.main_game.snake.direction.y != -1:
                        self.main_game.snake.direction = Vector2(0, 1)
                if event.key == pg.K_RIGHT:
                    if self.main_game.snake.direction.x != -1:
                        self.main_game.snake.direction = Vector2(1, 0)
                if event.key == pg.K_LEFT:
                    if self.main_game.snake.direction.x != 1:
                        self.main_game.snake.direction = Vector2(-1, 0)

            if event.type == pg.USEREVENT:
                self.main_game.snake.move_snake()
                self.main_game.check_collision()
                self.main_game.check_fail()


class MAIN:
    def __init__(self):
        """Initializes the game state."""
        self.snake = SNAKE()
        self.fruit = FRUIT1()

    def update(self):
        """Updates the snake and checks for collisions."""
        self.snake.move_snake()
        self.check_fail()

    def draw_items(self):
        """Draws the grass, snake, and fruit."""
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        """Checks if the snake eats the fruit."""
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        """Checks if the game is over (snake out of bounds or colliding with itself)."""
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def draw_grass(self):
        """Draws the grass (alternating colors)."""
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            for col in range(cell_number):
                if (row + col) % 2 == 0:
                    grass_rect = pg.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pg.draw.rect(screen, grass_color, grass_rect)

    def game_over(self):
        """Ends the game when called."""
        pg.quit()
        sys.exit()

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


# Game initialization
pg.init()
pg.time.set_timer(pg.USEREVENT, 150)  # Timer event to update snake's movement

# Running the game
if __name__ == "__main__":
    game = Game()
    game.run()