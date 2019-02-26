import pygame
import sys


class GUI():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.button_group = pygame.sprite.Group()
        self.menubar_group = pygame.sprite.Group()
        self.inputbox_group = pygame.sprite.Group()
        self.widget_group = pygame.sprite.Group()


    def add_button(self, button):
        button.rect.x += self.rect.x
        button.rect.y += self.rect.y
        self.button_group.add(button)


    def add_menubar(self, menubar):
        menubar.rect.x += self.rect.x
        menubar.rect.y += self.rect.y
        self.menubar_group.add(menubar)


    def add_inputbox(self, inputbox):
        inputbox.rect.x += self.rect.x
        inputbox.rect.y += self.rect.y
        self.inputbox_group.add(inputbox)


    def add_widget(self, widget):
        widget.rect.x += self.rect.x
        widget.rect.y += self.rect.y
        self.widget_group.add(widget)


    def update(self, screen):
        self.button_group.update()
        self.button_group.draw(screen)
        self.menubar_group.update(screen)
        self.inputbox_group.update()
        self.inputbox_group.draw(screen)
        self.widget_group.update(screen)

        self.check_event()



    def check_event(self):
        for event in pygame.event.get():
            for button in self.button_group:
                button.process_event(event)
            for menubar in self.menubar_group:
                menubar.process_event(event)
            for inputbox in self.inputbox_group:
                inputbox.process_event(event)
            for widget in self.widget_group:
                widget.process_event(event)