import sys
import pygame

from button import *


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('GUI')


def main():
    gui_group = pygame.sprite.Group()
    button1 = Button(pos=(100, 100))
    gui_group.add(button1)

    clock = pygame.time.Clock()
    while True:
        gui_group.update()
        gui_group.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        pygame.display.update()

        clock.tick(60)


if __name__ == '__main__':
    main()


