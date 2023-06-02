import pygame as pg
from pygame.locals import *
from colors import *
from settings import *
from vec2 import Vec2

"""
Entity 01 reprensete object in the screen
"""

class Entity01:
    def __init__(self, x:float=0.0, y:float=0.0,color=(255,255,255)) -> None:
        self.location = [x,y]
        self.velovicity = [1.0,3.3]
        self.acceleration = [0.0,0.0]
        self.color = color
        self.radius = 25.0
    
    def draw(self, surface:pg.Surface):
         pg.draw.circle(surface,self.color,(self.location[0],self.location[1]), self.radius)
    
    def update(self, dt):
        self.location[0] = self.location[0] + (self.velovicity[0])
        self.location[1] = self.location[1] + (self.velovicity[1])
        
        if(self.location[0] > SCREEN_SIZE[0]- self.radius) or (self.location[0] - self.radius < 0):
            self.velovicity[0] = self.velovicity[0] * -1
        if(self.location[1] > SCREEN_SIZE[1]- self.radius) or (self.location[1] - self.radius < 0):
            self.velovicity[1] = self.velovicity[1] * -1
        