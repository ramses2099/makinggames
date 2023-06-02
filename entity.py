import pygame as pg
from pygame.locals import *
from colors import *
from settings import *
from vec2 import Vec2

"""
Entity reprensete object in the screen
"""
class Entity:
    def __init__(self, pos:Vec2, color =(255,255,255)) -> None:
        self.acceleration = Vec2(2.0,0.0)
        self.velocity = Vec2(0.0,0.0)
        self.location = pos
        self.radius = 15.0 
        self.color = color
        
        # speed and force
        self.maxspeed = 4;
        self.maxforce = 0.1
        
    def applyforce(self,force:Vec2)->None:
        self.acceleration.add(force)
        
    def seek(self,taget:Vec2)->None:
        pass
        

    def draw(self, surface: pg.Surface) -> None:
        pg.draw.circle(surface,self.color,self.location.getvector2d(), self.radius)
    
    def update(self, dt) -> None:        
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.location.add(self.velocity)
        self.acceleration.mult(0)
        
        