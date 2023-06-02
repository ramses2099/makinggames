import pygame as pg
import sys
from pygame.locals import *
from colors import *
from settings import *
from vec2 import Vec2

# test entity
from entity import Entity
from entity01 import Entity01
from entity02 import Entity02


def showFPS(surface, dt, pos=(10, 10)):
    font = pg.font.Font(FONT_NAME, 12)
    text = font.render(f"FPS: {dt}", True, WHITE)
    textRect = text.get_rect()
    textRect.center = pos
    surface.blit(text, textRect)


def main():
    pg.init()

    fpsClock = pg.time.Clock()
    DISPLAYSURF = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption(TITLE)

    # TEST VEC2
    v1 = Vec2(70.0, 70.0)
    entity00 = Entity(v1, BLUE)

    entity01 = Entity01(250.0, 300.0)
    
    entity02 = Entity02([30.0,400.0],RED)

    # DELTA TIME
    dt = 0.0
    fpsClock.tick(FPS)

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        DISPLAYSURF.fill(BLACK)

        # update
        entity00.update(dt)
        entity01.update(dt)
        entity02.update(dt)
        
        # draw
        if DEBUG:
            showFPS(DISPLAYSURF, dt, (35, 10))

        entity00.draw(DISPLAYSURF)
        entity01.draw(DISPLAYSURF)
        
        entity02.draw(DISPLAYSURF)


        pg.display.update()
        dt = fpsClock.tick(FPS) / 1000.0


if __name__ == "__main__":
    main()
