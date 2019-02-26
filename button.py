from clickableobject import *

from constant import *


class Button(ClickableObject):
    def __init__(self, pos=INIT_BUTTON_POS, size=INIT_BUTTON_SIZE, text=INIT_BUTTON_TEXT,
                 text_size=INIT_BUTTON_TEXT_SIZE, text_color=INIT_BUTTON_TEXT_COLOR,
                 normal_image=None, hover_image=None, active_image=None):
        ClickableObject.__init__(self, size=size, text=text, text_size=text_size, text_color=text_color)

        # 按钮正常颜色, 悬浮颜色, 点击颜色
        self.normal_color = INIT_BUTTON_NORMAL_COLOR
        self.hover_color = INIT_BUTTON_HOVER_COLOR
        self.active_color = INIT_BUTTON_ACTIVE_COLOR

        # 按钮正常图片, 悬浮图片, 点击图片
        self.normal_image = normal_image
        self.hover_image = hover_image
        self.active_image = active_image

        self.init_button()

        self.rect.x, self.rect.y = pos


    # 如果有图片则用图片
    # 没有用纯色
    def init_button(self):
        if self.normal_image:
            self.normal_image = pygame.transform.scale(self.normal_image, self.size)
            self.hover_image = pygame.transform.scale(self.hover_image, self.size)
            self.active_image = pygame.transform.scale(self.active_image, self.size)
        else:
            self.normal_image = pygame.Surface(self.size)
            self.normal_image.fill(WHITE)
            # 鼠标指针浮动在按钮上时， 按钮的背景图片
            self.hover_image = pygame.Surface(self.size)
            self.hover_image.fill(self.hover_color)
            # 鼠标点击时， 按钮的背景图片
            self.active_image = pygame.Surface(self.size)
            self.active_image.fill(self.active_color)

        self.image = self.normal_image.copy()
        self.rect = self.image.get_rect()

        self.set_image(self.normal_image)

        self.status = NORMAL


    # 状态转为普通状态
    def change_to_normal(self):
        self.set_image(self.normal_image)


    # 状态转为悬浮状态
    def change_to_hover(self):
        self.set_image(self.hover_image)


    # 状态转为点击状态
    def change_to_active(self):
        self.set_image(self.active_image)

