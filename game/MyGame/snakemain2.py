import pygame as pg
import sys
from pygame.math import Vector2
from snakesprites import SNAKE, FRUIT2  # Import sprites from snakesprites.py

#source:
#source: ChatGPT: asked "Can you split the code from snake.py into two files, one main file and one file with the sprites"

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
        self.fruit = FRUIT2()

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


# Game initialization
pg.init()
pg.time.set_timer(pg.USEREVENT, 150)  # Timer event to update snake's movement

# Running the game
if __name__ == "__main__":
    game = Game()
    game.run()
