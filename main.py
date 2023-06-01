import pygame as pg
import sys
from pygame.locals import *
from colors import *
from constants import *


def main():
    pg.init()

    fpsClock = pg.time.Clock()
    DISPLAYSURF = pg.display.set_mode((400, 400))
    pg.display.set_caption(TITLE)

    tankImg = pg.image.load(IMAGE)
    tankx = 10
    tanky = 10

    direction = "r"

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        DISPLAYSURF.fill(WHITE)

        if direction == "r":
            tankx += 5
            if tankx == 280:
                direction = "d"
        elif direction == "d":
            tanky += 5
            if tanky == 220:
                direction = "l"
        elif direction == "l":
            tankx -= 5
            if tankx == 10:
                direction = "u"
        elif direction == "u":
            tanky -= 5
            if tanky == 10:
                direction = "r"

        DISPLAYSURF.blit(tankImg, (tankx, tanky))

        pg.display.update()
        fpsClock.tick(FPS)


if __name__ == "__main__":
    main()
