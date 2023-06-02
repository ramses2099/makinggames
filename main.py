import pygame as pg
import sys
from pygame.locals import *
from colors import *
from settings import *
from vec2 import Vec2

def showFPS(surface, dt, pos=(10,10)):
    font = pg.font.Font(FONT_NAME,12)
    text = font.render(f"FPS: {dt}",True,WHITE)
    textRect = text.get_rect()
    textRect.center = pos
    surface.blit(text, textRect)
    

def main():
    pg.init()

    fpsClock = pg.time.Clock()
    DISPLAYSURF = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption(TITLE)
    
    #TEST VEC2
    v1 = Vec2(70.0, 70.0)
    v1.add(Vec2(50.0,50.0))
    v1.print()
    
    print(f"mag:{v1.mag()}")
    
    v2 = Vec2(100, 100)
    dist = v1.dist(v2)
    print(f"dist:{dist}")
    
    # DELTA TIME
    dt = 0.0
    fpsClock.tick(FPS)

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        DISPLAYSURF.fill(BLACK)
        
        # draw
        if DEBUG:
            showFPS(DISPLAYSURF, dt,(35,10))
        
        # update
        
        
        pg.display.update()
        dt = fpsClock.tick(FPS)/1000.0


if __name__ == "__main__":
    main()
