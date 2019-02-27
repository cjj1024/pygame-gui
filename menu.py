import pygame

from clickableobject import *
from constant import *
from menuitem import *


class Menu(ClickableObject):
    def __init__(self, size=INIT_MENUITEM_SIZE, pos=INIT_MENUITEM_POS,
                 text=None, text_size=INIT_MENUITEM_TEXT_SIZE, text_color=INIT_MENUITEM_TEXT_COLOR):
        ClickableObject.__init__(self, size=size, text=text, text_size=text_size, text_color=text_color)

        self.rect.x, self.rect.y = pos

        self.total_height = self.rect.height

        self.is_expand = False

        self.menuitem_group = pygame.sprite.Group()


    def update(self, screen):
        super().update()
        if self.is_expand:
            self.menuitem_group.update()
            self.menuitem_group.draw(screen)


    def add_menuitem(self, menuitem):
        menuitem.rect.x = self.rect.x
        menuitem.rect.y = self.rect.y + self.total_height
        self.total_height += menuitem.rect.height
        self.menuitem_group.add(menuitem)


    def active(self):
        self.is_expand = not self.is_expand


    # rel为相对位移
    def drag(self, rel):
        self.rect.x += rel[0]
        self.rect.y += rel[1]
        for menuitem in self.menuitem_group:
            menuitem.rect.x += rel[0]
            menuitem.rect.y += rel[1]


    def adjust_pos(self, x, y):
        super().adjust_pos(x, y)

        for menuitem in self.menuitem_group:
            menuitem.adjust_pos(x, y)
