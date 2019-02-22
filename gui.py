import pygame
import sys


class GUI():
    def __init__(self):
        self.button_group = pygame.sprite.Group()


    def add_button(self, button):
        self.button_group.add(button)


    def update(self):
        self.button_group.update()
        self.check_event()


    def draw(self, screen):
        self.button_group.draw(screen)


    def check_event(self):
        for event in pygame.event.get():
            for button in self.button_group:
                button.check_event(event)