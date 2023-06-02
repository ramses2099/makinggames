import pygame as pg
import sys
from pygame.locals import *
from colors import *
from constants import *
from pygame.math import Vector2 as vec


def main():
    pg.init()

    fpsClock = pg.time.Clock()
    DISPLAYSURF = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pg.display.set_caption(TITLE)

    rect1 = pg.Rect(50, 50, 50, 50)
    x_speed, y_speed = 5, 4

    rect2 = pg.Rect(500, 100, 50, 50)
    other_speed = 3

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        DISPLAYSURF.fill(BLACK)

        # update

        # draw
        pg.draw.rect(DISPLAYSURF, WHITE, rect1)
        pg.draw.rect(DISPLAYSURF, BLUE, rect2)

        pg.display.flip()

        pg.display.update()
        fpsClock.tick(FPS)


if __name__ == "__main__":
    main()
