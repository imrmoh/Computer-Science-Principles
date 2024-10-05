#File by Imraan Mohammed


#importing all necessary modules and libraries
from settings import *
import pygame as p
from pygame.sprite import Sprite

#the Player class allows us to create the player sprite
class Player(Sprite):
    #the __init__ function allows us to initialize the class
    def __init__(self, game, x, y):
        self.game=game
        #assigning the Player sprite to the all_sprites group
        self.groups=game.all_sprites
        Sprite.__init__(self, self.groups)
        self.game=game
        #assigning the color of the player as red
        self.image=p.Surface((32, 32))
        self.rect=self.image.get_rect()
        self.image.fill(RED)
        self.x=x
        self.y=y
        self.speed=10
        #self.rect.x=x
        #self.rect.y=y
        #setting the size of Player on the screen
        self.x=x*TILESIZE
        self.y=y*TILESIZE
        self.speed=10
        self.vx, self.vy = 0, 0 

    #the get_keys function allows for the program to detect when certain keys are being pressed
    def get_keys(self):
        keys=p.key.get_pressed()
        #adjusts the direction that the player is moving in based on which key the player presses
        if keys[p.K_w]:
            self.vy -= self.speed
        if keys[p.K_a]:
            self.vx -=self.speed
        if keys [p.K_s]:
            self.vy += self.speed
        if keys[p.K_d]:
            self.vx += self.speed

    #the collide_with_walls function checks if the player has collided with any walls
    def collide_with_walls(self, dir):
        #checks if the player has collided with the left/right wall
       if dir=="x":
           hits=p.sprite.spritecollide(self, self.game.all_walls,False)
           if hits:
                if self.vx>0:
                   self.x=hits[0].rect.left-self.rect.width
                if self.vx<0:
                    self.x=hits[0].rect.right
                self.vx=0
                self.rect.x=self.x
       #checks if the player has collided with the top/bottom wall
       if dir=="y":
           hits=p.sprite.spritecollide(self, self.game.all_walls,False)
           if hits:
                if self.vy>0:
                   self.y=hits[0].rect.top-self.rect.height
                if self.vy<0:
                    self.y=hits[0].rect.bottom
                self.vy=0
                self.rect.y=self.y
                


    #the update function allows for the game to change as the user interacts with it
    def update(self):
        self.get_keys()
        self.rect.x += self.speed
        self.x+=self.vx*self.game.dt
        self.y+=self.vy*self.game.dt
        self.collide_with_walls("x")
        self.rect.x=self.x
        self.collide_with_walls("y")
        self.rect.y=self.y
        #detects if the Player is off the screen
        if self.rect.right>WIDTH or self.rect.left<0:
            print("off the screen")
            print(self.speed)
            print(self.rect.x)
            self.speed *= -1
            self.rect.y += 32
        #adjusts the speed depending on certain circumstances
        elif self.rect.colliderect(self.game.player):
            self.speed *= 1
        elif self.rect.colliderect(self):
            self.speed *= -1
        
#creating a mon
class Mob(Sprite):
    #intializing the Mob class
    def __init__(self, x, y):
        Sprite.__init__(self, self.groups)
        #setting the size of the Mob
        self.image=p.Surface((32, 32))
        self.rect=self.image.get_rect()
        #setting the color of the Mob
        self.image.fill(RED)
        #adjusting other settings related to the mob
        self.x=x
        self.y=y
        self.speed=10
        self.rect.x=x
        self.rect.y=y
    #the update function allows the game to change continuously
    def update(self):
        self.rect.x += self.speed
        #detects if the side of the screen has been hit
        if self.rect.right >= WIDTH or self.rect.left < 0:
            #does certain actions of the side of the screen has been hit
            print("Hit the side of the screen")
            print(self.speed)
            print(self.rect.x)
            self.speed *= -1
            self.rect.y += 32
        if self.y <= -600:
            self.rect.y += 600

#creating a wall
class Wall(Sprite):
    #initializing the wall class
    def __init__(self, x, y):
        self.groups=(game.all_sprites, game.all_walls)
        self.game=game
        #setting the size of the wall
        Sprite.__init__(self, self.groups)
        self.image=p.Surface((700, TILESIZE))
        self.rect=self.image.get_rect()
        #setting the color of the wall
        self.image.fill(WHITE)
        self.rect.x=x
        self.rect.y=y
'''
class RightWall(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image=p.Surface((700, TILESIZE))
        self.rect=self.image.get_rect()
        self.image.fill(WHITE)
        self.x=x
        self.y=y
'''

#creating a powerup
class PowerUp(Sprite):
    #initializing the powerup class
    def __init__(self, x, y):
        self.groups=(game.all_sprites, game.all_walls)
        self.game=game
        Sprite.__init__(self, self.groups)
        #setting the size fo the powerup
        self.image=p.Surface((700, TILESIZE))
        self.rect=self.image.get_rect()
        #setting the color of the powerup
        self.image.fill(BLACK)
        self.rect.x=x
        self.rect.y=y


