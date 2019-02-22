import pygame
import sys

from clickableobjectconstant import *


class ClickableObject(pygame.sprite.Sprite):
    def __init__(self, size=INIT_CLICKABLE_OBJECT_SIZE, pos=INIT_CLICKABLE_OBJECT_POS):
        pygame.sprite.Sprite.__init__(self)


        self.size = size
        self.image = pygame.Surface(self.size)
        self.image.fill(INIT_CLICKABLE_OBJECT_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

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

    def check_event(self, event):
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


    # 判断x, y是否在按钮区域
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