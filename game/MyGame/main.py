#file by Imraan Mohammed

#import all necessary modules and libraries
import pygame as p
from settings import *
from sprites import*
from random import randint
from tilemap import *
from os import path
from random import randint


#created a game class to instantiate later
#the class will contain all the necessary parts to run the game

class Game:
    #the __init__ function initializes the class
    def __init__(self):
        p.init()
        p.mixer.init()
        self.screen = p.display.set_mode((WIDTH, height))
        #setting the game's title/caption
        p.display.set_caption("Test Game")
        #creates self.clock
        self.clock = p.time.Clock()
        self.running = True

    def load_data(self):
        self.game_folder=path.dirname(__file__)
        self.map=Map(path.join(self.game_folder, "level1.txt"))

    #creating a new sprite
    def new(self):
        self.load_data()
        #creating the all_sprites group to put the game's sprites in
        self.all_sprites = p.sprite.Group()
        #creating the player sprite
        self.player=Player(self, 50, 50)
        #creating the mob sprite
        self.mob=Mob(self, 100)
        #self.mob=Mob(self, 100)
        #creating a wall
        self.wall=Wall(0, 100)
        #creating a second wall
        self.rightwall=RightWall(100, 100)
        #adding self.player to the all_sprites group
        self.all_sprites.add(self.player)
        #adding the mob to the all_sprites group
        self.all_sprites.add(self.mob)
        #adding the wall to the all_sprites group
        self.all_sprites.add(self.wall)
        #adding the right wall to the all_sprites group
        self.all_sprites.add(self.rightwall)
        '''
        for i in range(6):
            Mob(self, i*randint(0, 200))
            #Mob(self, i*randint(0, 200), i*randint(0, 200))
        for i in range(6):
            Wall( i*TILESIZE, i*TILESIZE)
            #self.all_sprites.add(w)g
        '''
            
        for row, tiles in enumerate(self.map.data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile=="1":
                    Wall(self, col, row)
                if tile=="P":
                    self.player = Player(self, col, row)
                if tile=="M":
                    Mob(self, col, row)

    def run(self):
        while self.running:
            #controlled by clock
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()
    
    #the events function checks for one event, which is the user quitting the game
    def events(self):
    #checks if the user has quit the game
        for event in p.event.get():
            if event.type == p.QUIT:
                #the game stops running if the user has quit the game
                self.running = False
        #p.quit()

    #the update function updates the sprites
    def update(self):
        #updates all the sprites in the game
        self.all_sprites.update()
    #the draw function fills the screen, draws the sprites, and displays them
    def draw(self):
        #fills the screen with a specific color
        self.screen.fill((0, 87, 65))
        #draws the sprites
        self.all_sprites.draw(self.screen)
        p.display.flip()

    


#checking if the file name is main
if __name__=="__main__":
    #"calling" the Game class
    gme = Game()
    gme.new()
    #running the game
    gme.run()
