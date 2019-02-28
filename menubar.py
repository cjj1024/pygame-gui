from menu import *
from constant import *


class MenuBar(pygame.sprite.Sprite):
    def __init__(self, pos=INIT_MENUBAR_POS):
        pygame.sprite.Sprite.__init__(self)

        self.menu_group = pygame.sprite.Group()

        self.total_width = 0

        self.image = None
        self.rect = pygame.Rect(pos, (0, 0))


    def add_menu(self, menu):
        menu.rect.x = self.rect.x + self.total_width
        menu.rect.y = self.rect.y + 5
        self.total_width += menu.rect.width
        self.menu_group.add(menu)


    def update(self, screen):
        self.menu_group.update(screen)
        self.menu_group.draw(screen)


    def process_event(self, event):
        for menu in self.menu_group:
            menu.process_event(event)


    # rel为相对位移
    def drag(self, rel):
        for menu in self.menu_group:
            menu.drag(rel)


    def adjust_pos(self, x, y):
        for menu in self.menu_group:
            menu.adjust_pos(x, y)