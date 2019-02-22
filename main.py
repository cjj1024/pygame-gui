import sys
import pygame

from button import *
from gui import *


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('GUI')


def main():
    gui = GUI()
    button1 = Button()

    img1 = pygame.image.load('./res/button_light_blue.png')
    img2 = pygame.image.load('./res/button_yellow.png')
    img3 = pygame.image.load('./res/button_blue.png')
    button2 = Button(pos=(0, 100), normal_image=img1, hover_image=img3, active_image=img2)
    gui.add_button(button2)
    gui.add_button(button1)


    clock = pygame.time.Clock()
    while True:
        gui.update()
        gui.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        pygame.display.update()

        clock.tick(60)


if __name__ == '__main__':
    main()


