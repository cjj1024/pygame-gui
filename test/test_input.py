import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('GUI')

sys.path.append('../')
os.chdir('../')

from gui import *
from inputbox import *
from label import *


def main():
    gui = GUI()


    inputbox = InputBox()

    label = Label(text="输入")
    gui.add_label(label, pos=(0, 90))
    gui.add_inputbox(inputbox, pos=(label.image.get_width(), 90))


    clock = pygame.time.Clock()
    while True:
        screen.fill((230,230,250), (0, 0, 800, 600))
        gui.update(screen)
        for event in pygame.event.get():
            gui.process_event(event)
            if event.type == pygame.QUIT:
                sys.exit(0)

        pygame.display.update()

        clock.tick(60)


if __name__ == '__main__':
    main()


