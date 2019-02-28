import pygame
import sys


class GUI():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.offset = (0, 0)
        self.button_group = pygame.sprite.Group()
        self.menubar_group = pygame.sprite.Group()
        self.inputbox_group = pygame.sprite.Group()
        self.widget_group = pygame.sprite.Group()


    def add_button(self, button):
        button.adjust_pos(self.rect.x, self.rect.y)
        button.adjust_pos(self.offset[0], self.offset[1])
        self.button_group.add(button)


    def add_menubar(self, menubar):
        menubar.adjust_pos(self.rect.x, self.rect.y)
        menubar.adjust_pos(self.offset[0], self.offset[1])
        self.menubar_group.add(menubar)


    def add_inputbox(self, inputbox):
        inputbox.adjust_pos(self.rect.x, self.rect.y)
        inputbox.adjust_pos(self.offset[0], self.offset[1])
        self.inputbox_group.add(inputbox)


    def add_widget(self, widget):
        widget.adjust_pos(self.rect.x, self.rect.y)
        widget.adjust_pos(self.offset[0], self.offset[1])
        self.widget_group.add(widget)


    def update(self, screen):
        self.button_group.update()
        self.button_group.draw(screen)
        self.menubar_group.update(screen)
        self.inputbox_group.update()
        self.inputbox_group.draw(screen)
        self.widget_group.update(screen)


    def process_event(self, event):
        for button in self.button_group:
            button.process_event(event)
        for menubar in self.menubar_group:
            menubar.process_event(event)
        for inputbox in self.inputbox_group:
            inputbox.process_event(event)
        for widget in self.widget_group:
            widget.process_event(event)