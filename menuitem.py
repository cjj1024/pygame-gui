from clickableobject import *
from constant import *


class MenuItem(ClickableObject):
    def __init__(self, size=INIT_MENUITEM_SIZE, pos=INIT_MENUITEM_POS,
                 text=None, text_size=INIT_MENUITEM_TEXT_SIZE, text_color=INIT_MENUITEM_TEXT_COLOR):
        ClickableObject.__init__(self, size=size, text=text, text_size=text_size, text_color=text_color)

        pygame.draw.rect(self.image, BLACK, (0, 0, self.image.get_width(), self.image.get_height()), 1)

        self.rect.x, self.rect.y = pos