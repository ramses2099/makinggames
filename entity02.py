import pygame as pg
from pygame.locals import *
from pygame.math import Vector2 as Vec2
from colors import *
from settings import *

"""
Entity 01 reprensete object in the screen
"""


class Entity02:
    def __init__(self, pos: list = [0.0, 0.0], color=(255, 255, 255)) -> None:
        self.location = Vec2(pos[0], pos[1])
        self.velovicity = Vec2(1.0, 3.3)
        self.acceleration = Vec2(0.0, 0.0)
        self.color = color
        self.radius = 25.0

    def draw(self, surface: pg.Surface):
        pg.draw.circle(
            surface, self.color, self.location, self.radius
        )

    def update(self, dt):
        self.location.x = self.location.x + self.velovicity.x
        self.location.y = self.location.y + self.velovicity.y

        if (self.location.x > SCREEN_SIZE[0] - self.radius) or (
            self.location.x - self.radius < 0
        ):
            self.velovicity.x = self.velovicity.x * -1
        
        if (self.location.y > SCREEN_SIZE[1] - self.radius) or (
            self.location.y - self.radius < 0
        ):
            self.velovicity.y = self.velovicity.y * -1
