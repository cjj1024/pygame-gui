import pygame

from clickableobject import *
from constant import *


class InputBox(ClickableObject):
    def __init__(self, size=INIT_INPUTBOX_SIZE, pos=INIT_INPUTBOX_POS, color=INIT_INPUTBOX_COLOR,
                 text=INIT_INPUTBOX_TEXT, text_color=INIT_INPUTBOX_TEXT_COLOR):
        ClickableObject.__init__(self, size=size, color=color, text=text, text_color=text_color)

        self.rect.x, self.rect.y = pos

        self.background_image = self.image.copy()

        self.is_enable_input = False


    def get_input(self, key):
        # 退格键
        if key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        # 48 - 57 为数字 0 - 9
        # 97 - 122 为字母 'a' - 'z'
        elif key >= 97 and key <= 122 or key >= 48 and key <= 57:
            self.text += chr(key)

        print(self.text)
        self.init_text()
        self.set_image(self.background_image.copy())


    def process_event(self, event):
        super().process_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.is_in_object_area(x, y):
                self.is_enable_input = True
            else:
                self.is_enable_input = False
        elif event.type == pygame.KEYDOWN and self.is_enable_input:
            self.get_input(event.key)

