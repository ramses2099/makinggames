"""
class represent vector 2d
"""
from pygame.math import Vector2
import math

class Vec2:
    def __init__(self, x:float = 0.0, y:float = 0.0) -> None:
        self._x = x
        self._y = y

    def add(self, other)->None:   
        if not type(other) is Vec2:
            raise TypeError("Only Vec2 are allowed")       
        self._x = self._x + other._x
        self._y = self._y + other._y
    
    def sub(self, other)->None: 
        if not type(other) is Vec2:
            raise TypeError("Only Vec2 are allowed")       
        self._x = self._x - other._x
        self._y = self._y - other._y
    
    def div(self, n: float)->None:        
        self._x = self._x / n
        self._y = self._y / n
    
    def mult(self, n: float)->None:        
        self._x = self._x * n
        self._y = self._y * n

    def mag(self) -> float:
        return math.sqrt((self._x**2)+(self._y**2)) 
    
    def normalize(self)->None:
        m = self.mag()
        if not m == 0:
            self.div(m)
            
    def limit(self, max:float)->None:
        length = self.mag()
        if length > max:
            self.mult((max/length))
        else:
            self.mult(1.0)
            
    def dist(self, other)-> float:
        if not type(other) is Vec2:
            raise TypeError("Only Vec2 are allowed")  
        p = [self._x, self._y]
        q = [other._x, other._y]
        return math.dist(p, q)
    
    def getvector2d(self)->Vector2:
        return Vector2(self._x, self._y)
    
    def print(self)->None:
        print(f"[x:{self._x},y:{self._y}]")