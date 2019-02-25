from button import *
from gui import *
from menuitem import *
from menubar import *
from menu import *
from inputbox import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('GUI')


def main():
    gui = GUI()
    button1 = Button()
    # gui.add_button(button1)
    img1 = pygame.image.load('./res/button_light_blue.png')
    img2 = pygame.image.load('./res/button_yellow.png')
    img3 = pygame.image.load('./res/button_blue.png')
    button2 = Button(pos=(0, 100), normal_image=img1, hover_image=img3, active_image=img2)
    # gui.add_button(button2)

    # menuitem = MenuItem(pos=(200, 0), text='菜单项')
    # gui.add_button(menuitem)

    menubar = MenuBar()

    menu = Menu(text='文件')
    menubar.add_menu(menu)
    menuitem2 = MenuItem(text='保存')
    menuitem3 = MenuItem(text='另存为')
    menu.add_menuitem(menuitem2)
    menu.add_menuitem(menuitem3)

    menu2 = Menu(text='帮助')
    menubar.add_menu(menu2)
    menu2.add_menuitem(MenuItem(text='About'))
    menu2.add_menuitem(MenuItem(text='退出'))

    gui.add_menubar(menubar)


    inputbox = InputBox()
    gui.add_inputbox(inputbox)



    clock = pygame.time.Clock()
    while True:
        screen.fill((230,230,250), (0, 0, 800, 600))
        gui.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        pygame.display.update()

        clock.tick(60)


if __name__ == '__main__':
    main()


