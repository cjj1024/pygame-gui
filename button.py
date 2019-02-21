import sys

import pygame

from button_constant import *


class Button(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), size=(120, 40), text='Button', text_size=32, text_color=(0, 0, 0), image=None):
        pygame.sprite.Sprite.__init__(self)

        self.size = size
        self.text = text
        self.text_size = text_size
        self.text_color = text_color
        self.background = image

        self.init_button()

        self.rect.x, self.rect.y = pos


    def init_button(self):
        if self.background:
            self.background = pygame.transform.scale(self.background, self.size)
        else:
            self.background = pygame.Surface(self.size)
            self.background.fill((255, 255, 255))
            self.hover_image = pygame.Surface(self.size)
            self.hover_image.fill((0, 191, 255))
            self.click_image = pygame.Surface(self.size)
            self.click_image.fill((127, 255, 0))

        self.image = self.background.copy()

        self.rect = self.image.get_rect()

        if self.rect.width / len(list(self.text)) > self.text_size:
            self.text_size = self.text_size
        else:
            self.text_size = int(self.rect.width / len(list(self.text)))

        self.font = pygame.font.Font('./minicanton.TTF', self.text_size)
        self.text_image = self.font.render(self.text, True, self.text_color)

        self.set_image(self.background)

        self.status = HOVER


    def set_image(self, img):
        self.image = img.copy()
        offset_x = int((self.image.get_width() - self.text_image.get_width()) / 2)
        offset_y = int((self.image.get_height() - self.text_image.get_height()) / 2)
        self.image.blit(self.text_image, (offset_x, offset_y))


    def update(self, *args):
        self.check_event()

        if self.status == NORMAL:
            self.normal()
        elif self.status == HOVER:
            self.hover()
        elif self.status == ACTIVE:
            self.click()


    def normal(self):
        self.set_image(self.background)


    def click(self):
        self.set_image(self.click_image)


    def hover(self):
        self.set_image(self.hover_image)


    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if self.is_in_button(x, y):
                    self.status = HOVER
                else:
                    self.status = NORMAL
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if self.is_in_button(x, y):
                        self.status = ACTIVE
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if self.is_in_button(x, y):
                    self.status = HOVER



    def is_in_button(self, x, y):
        if x > self.rect.left and x < self.rect.right\
                and y > self.rect.top and y < self.rect.bottom:
            return True
        else:
            return False