import pygame
import sys


class GUI():
    def __init__(self):
        self.button_group = pygame.sprite.Group()
        self.menubar_group = pygame.sprite.Group()
        self.inputbox_group = pygame.sprite.Group()


    def add_button(self, button):
        self.button_group.add(button)


    def add_menubar(self, menubar):
        self.menubar_group.add(menubar)


    def add_inputbox(self, inputbox):
        self.inputbox_group.add(inputbox)


    def update(self, screen):
        self.button_group.update()
        self.button_group.draw(screen)
        self.menubar_group.update(screen)
        self.inputbox_group.update()
        self.inputbox_group.draw(screen)
        self.check_event()



    def check_event(self):
        for event in pygame.event.get():
            for button in self.button_group:
                button.process_event(event)
            for menubar in self.menubar_group:
                menubar.process_event(event)
            for inputbox in self.inputbox_group:
                inputbox.process_event(event)