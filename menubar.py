import pygame

from clickableobject import *
from menu import *
from constant import *


class MenuBar(ClickableObject):
    def __init__(self, pos=INIT_MENUBAR_POS):
        ClickableObject.__init__(self)

        self.menu_group = pygame.sprite.Group()

        self.total_width = 0


    def add_menu(self, menu):
        menu.rect.x = self.rect.x + self.total_width
        menu.rect.y = self.rect.y
        self.total_width += menu.rect.width
        self.menu_group.add(menu)


    def update(self, screen):
        self.menu_group.update(screen)
        self.menu_group.draw(screen)


    def check_event(self, event):
        super().check_event(event)

        for menu in self.menu_group:
            menu.check_event(event)