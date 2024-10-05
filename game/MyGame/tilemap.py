#importing all necessary modules and libraries
import pygame as p
from settings import *

#setting up the tilemap that we drew in the other file
class Tilemap:
    #initializing the tilemap class
    def __init__(self, filename):
        #opening the file with the tilemap
        self.data=[]
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())
        #reading the file with the tilemap and converting it into an actual map in the game
        self.tilewidth=len(self.data[0])
        self.tileheight=len(self.data)
        self.width=self.tilewidth*TILESIZE
        self.height=self.tileheight*TILESIZE

