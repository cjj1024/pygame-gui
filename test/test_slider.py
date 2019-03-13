import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('GUI')

sys.path.append('../')
os.chdir('../')

from gui import *
from slider import *
from widget import *

def main():
    gui = GUI()

    slider = Slider(value=0.5)
    widget = Widget()
    widget.add_slider(slider, pos=(0, 200))
    gui.add_widget(widget, pos=(0, 0))
    # gui.add_slider(slider)


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


