#File by Imraan Mohammed
from settings import *
import pygame as p
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, game, x, y):
        self.game=game
        self.groups=game.all_sprites
        Sprite.__init__(self, self.groups)
        self.game=game
        self.image=p.Surface((32, 32))
        self.rect=self.image.get_rect()
        self.image.fill(RED)
        self.x=x
        self.y=y
        self.speed=10
        #self.rect.x=x
        #self.rect.y=y
        self.x=x*+TILESIZE
        self.y=y*+TILESIZE
        self.speed=10
        self.vx, self.vy = 0, 0 

    def get_keys(self):
        keys=p.key.get_pressed()
        if keys[p.K_w]:
            self.vy -= self.speed
        if keys[p.K_a]:
            self.vx -=self.speed
        if keys [p.K_s]:
            self.vy += self.speed
        if keys[p.K_d]:
            self.vx += self.speed

    def update(self):
        self.get_keys()
        self.rect.x += self.speed
        if self.rect.right>WIDTH or self.rect.left<0:
            print("off the screen")
            print(self.speed)
            print(self.rect.x)
            self.speed *= -1
            self.rect.y += 32
        elif self.rect.colliderect(self.game.player):
            self.speed *= 1
        elif self.rect.colliderect(self):
            self.speed *= -1

class Mob(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self, self.groups)
        self.image=p.Surface((32, 32))
        self.rect=self.image.get_rect()
        self.image.fill(RED)
        self.x=x
        self.y=y
        self.speed=10
        self.rect.x=x
        self.rect.y=y
    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= WIDTH or self.rect.left < 0:
            print("Hit the side of the screen")
            print(self.speed)
            print(self.rect.x)
            self.speed *= -1
            self.rect.y += 32
        if self.y <= -600:
            self.rect.y += 600

class Wall(Sprite):
    def __init__(self, x, y):
        self.groups=game.all_sprites
        self.game=game
        Sprite.__init__(self, self.groups)
        self.image=p.Surface((700, TILESIZE))
        self.rect=self.image.get_rect()
        self.image.fill(WHITE)
        self.x=x
        self.y=y

class RightWall(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image=p.Surface((700, TILESIZE))
        self.rect=self.image.get_rect()
        self.image.fill(WHITE)
        self.x=x
        self.y=y
