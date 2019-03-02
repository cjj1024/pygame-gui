from clickableobject import *
from textobject import *
from constant import *


class InputBox(ClickableObject, TextObject, pygame.sprite.Sprite):
    def __init__(self, size=INIT_INPUTBOX_SIZE, text=INIT_INPUTBOX_TEXT,
                 text_size=INIT_INPUTBOX_TEXT_SIZE, text_color=INIT_INPUTBOX_TEXT_COLOR):
        pygame.sprite.Sprite.__init__(self)

        ClickableObject.__init__(self, size=size)

        TextObject.__init__(self, text=text, text_size=text_size, text_color=text_color)

        self.background_image = pygame.Surface(size)
        self.background_image.fill(INIT_INPUTBOX_COLOR, self.background_image.get_rect())
        pygame.draw.rect(self.background_image, GREY, self.rect, 1)

        self.image = self.background_image.copy()


        self.is_enable_input = False


    def get_input(self, key):
        # 退格键
        if key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        # 48 - 57 为数字 0 - 9
        # 97 - 122 为字母 'a' - 'z'
        elif key >= 97 and key <= 122 or key >= 48 and key <= 57:
            self.text += chr(key)

        self.image = self.merge_text_image(self.text, self.text_size, self.text_color,
                                           self.background_image, False, LEFT)


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

