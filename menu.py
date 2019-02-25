import pygame

from clickableobject import *
from constant import *
from menuitem import *


class Menu(ClickableObject):
    def __init__(self, size=INIT_MENUITEM_SIZE, pos=INIT_MENUITEM_POS,
                 text=None, text_size=INIT_MENUITEM_TEXT_SIZE, text_color=INIT_MENUITEM_TEXT_COLOR):
        ClickableObject.__init__(self, size=size, text=text, text_size=text_size, text_color=text_color)

        pygame.draw.rect(self.image, BLACK, (0, 0, self.image.get_width(), self.image.get_height()), 1)

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