import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('GUI')

sys.path.append('../')
os.chdir('../')

from gui import *
from menubar import *

def main():
    gui = GUI()

    menubar = MenuBar()

    menu = Menu(text='文件')
    menubar.add_menu(menu)
    menuitem2 = MenuItem(text='保存')
    menuitem3 = MenuItem(text='另存为')
    menu.add_menuitem(menuitem2)
    menu.add_menuitem(menuitem3)

    menu2 = Menu(text='帮助')
    menubar.add_menu(menu2)
    menu2.add_menuitem(MenuItem(text='关于'))
    menu2.add_menuitem(MenuItem(text='退出'))

    gui.add_menubar(menubar, pos=(0, 0))


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


