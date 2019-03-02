from button import *
from constant import *


class MenuItem(Button):
    def __init__(self, size=INIT_MENUITEM_SIZE,text=None, text_size=INIT_MENUITEM_TEXT_SIZE,
                 text_color=INIT_MENUITEM_TEXT_COLOR):
        Button.__init__(self, size=size, text=text, text_size=text_size, text_color=text_color)
