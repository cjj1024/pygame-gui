import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('GUI')

sys.path.append('../')
os.chdir('../')
from button import *
from gui import *


def button_click():
    print('hello button clicked')


def button_click2(x):
    print(x)


def main():
    gui = GUI()
    button1 = Button()
    button1.bind_active(button_click)
    gui.add_button(button1, pos=(0, 0))

    img1 = pygame.image.load('./res/button_light_blue.png')
    img2 = pygame.image.load('./res/button_yellow.png')
    img3 = pygame.image.load('./res/button_blue.png')
    button2 = Button(normal_image=img1, hover_image=img3, active_image=img2)
    button2.bind_active(button_click2, 10)
    gui.add_button(button2, pos=(120, 0))


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


