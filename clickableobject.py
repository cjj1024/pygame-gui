import pygame
import sys

from constant import *


# 可点击控件
# 有三种状态
# normal 普通状态
# hover 鼠标悬浮在控件上方
# active 鼠标点击控件
# 当发生状态改变时会调用相应的状态改变函数和状态函数
class ClickableObject(pygame.sprite.Sprite):
    def __init__(self, size=INIT_CLICKABLE_OBJECT_SIZE, pos=INIT_CLICKABLE_OBJECT_POS,
                 color=INIT_CLICKABLE_OBJECT_COLOR,
                 text=None, text_size=INIT_MENUITEM_TEXT_SIZE, text_color=INIT_MENUITEM_TEXT_COLOR):
        pygame.sprite.Sprite.__init__(self)

        # 控件大小
        self.size = size
        # 控件背景色
        self.color = color
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.text_image = None
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        # 标记状态是否发生改变
        self.change_status = False

        if text != None:
            # 按钮文字
            self.text = text
            # 按钮文字大小
            self.text_size = text_size
            # 按钮文字颜色
            self.text_color = text_color
            self.init_text()
            self.set_image(self.image)



    def init_text(self):
        if self.text == '':
            return

        # 如果文字大小超过控件大小， 则使用控件的size
        if self.rect.width / len(list(self.text)) > self.text_size:
            self.text_size = self.text_size
        else:
            self.text_size = int(self.rect.width / len(list(self.text)))

        self.font = pygame.font.Font('./res/fatrolling.TTF', self.text_size)
        self.text_image = self.font.render(self.text, True, self.text_color)


    # 把背景图片与文字合并起来
    def set_image(self, img):
        if not self.text_image:
            return

        # 使用copy(), 避免修改原图片
        self.image = img.copy()
        # 使文字在图片中央
        offset_x = int((self.image.get_width() - self.text_image.get_width()) / 2)
        offset_y = int((self.image.get_height() - self.text_image.get_height()) / 2)
        self.image.blit(self.text_image, (offset_x, offset_y))


    def update(self, *args):
        # 没有状态变化则返回
        if not self.change_status:
            return

        if self.status == NORMAL:
            self.change_to_normal()
            self.normal()
        elif self.status == HOVER:
            self.change_to_hover()
            self.hover()
        elif self.status == ACTIVE:
            self.change_to_active()
            self.active()
        self.change_status = False


    # 处理事件
    # 当有鼠标移动事件时, 判断鼠标是否在控件区域内, 如果在, 则状态改为hover, 否则改为normal
    # 当有鼠标点击事件时, 判断鼠标是否在控件区域内, 如果在, 则状态改为active
    # 当有鼠标按键松开事件时, 判断鼠标是否在控件区域内, 如果在, 则状态改为hover, 否则改为normal
    def process_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if self.is_in_object_area(x, y):
                self.status = HOVER
                self.change_status = True
            else:
                self.status = NORMAL
                self.change_status = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if self.is_in_object_area(x, y):
                    self.status = ACTIVE
                    self.change_status = True
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if self.is_in_object_area(x, y):
                self.status = HOVER
                self.change_status = True
            else:
                self.status = NORMAL
                self.change_status = True


    # 判断x, y是否在控件区域内
    def is_in_object_area(self, x, y):
        if x > self.rect.left and x < self.rect.right \
            and y > self.rect.top and y < self.rect.bottom:
            return True
        else:
            return False


    # 状态转为普通状态
    def change_to_normal(self):
        pass


    # 普通状态
    def normal(self):
        pass


    # 状态转为普通状态
    def change_to_hover(self):
        pass


    # 鼠标指针悬浮在控件上方
    def hover(self):
        pass


    # 状态转为点击状态
    def change_to_active(self):
        pass


    # 点击状态
    def active(self):
        pass