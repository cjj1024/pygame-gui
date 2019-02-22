import sys

from clickableobject import *

from button_constant import *


class Button(ClickableObject):
    def __init__(self, pos=INIT_BUTTON_POS, size=INIT_BUTTON_SIZE, text=INIT_BUTTON_TEXT,
                 text_size=INIT_BUTTON_TEXT_SIZE, text_color=INIT_BUTTON_TEXT_COLOR,
                 normal_image=None, hover_image=None, active_image=None):
        ClickableObject.__init__(self, size=size, pos=pos)

        # 按钮文字
        self.text = text
        # 按钮文字大小
        self.text_size = text_size
        # 按钮文字颜色
        self.text_color = text_color

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

        self.change_status = False


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

        self.init_text()

        self.set_image(self.normal_image)

        self.status = NORMAL


    def init_text(self):
        # 如果文字大小超过按钮大小， 则使用按钮的size
        if self.rect.width / len(list(self.text)) > self.text_size:
            self.text_size = self.text_size
        else:
            self.text_size = int(self.rect.width / len(list(self.text)))

        self.font = pygame.font.Font('./res/minicanton.TTF', self.text_size)
        self.text_image = self.font.render(self.text, True, self.text_color)


    # 把背景图片与按钮上的文字合并起来
    def set_image(self, img):
        self.image = img.copy()
        # 使文字在图片中央
        offset_x = int((self.image.get_width() - self.text_image.get_width()) / 2)
        offset_y = int((self.image.get_height() - self.text_image.get_height()) / 2)
        self.image.blit(self.text_image, (offset_x, offset_y))


    # 状态转为普通状态
    def change_to_normal(self):
        self.set_image(self.normal_image)
        self.change_status = False


    # 状态转为悬浮状态
    def change_to_hover(self):
        self.set_image(self.hover_image)
        self.change_status = False


    # 状态转为点击状态
    def change_to_active(self):
        self.set_image(self.active_image)
        self.change_status = False


