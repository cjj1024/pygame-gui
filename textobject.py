import pygame


class TextObject():
    def __init__(self, text, text_size, text_color):
        self.text = text
        self.text_size = text_size
        self.text_color = text_color


    # 把背景图片与文字合并起来
    def merge_text_image(self, text, text_size, text_color, image):
        if not text:
            return

        # 如果文字大小超过控件大小， 则使用控件的size
        if image.get_width() / len(list(text)) > text_size:
            text_size = text_size
        else:
            text_size = int(image.get_width() / len(list(text)))

        font = pygame.font.Font('./res/fatrolling.TTF', text_size)
        text_image = font.render(text, True, text_color)


        # 使用copy(), 避免修改原图片
        self.image = image.copy()
        # 使文字在图片中央
        offset_x = int((self.image.get_width() - text_image.get_width()) / 2)
        offset_y = int((self.image.get_height() - text_image.get_height()) / 2)
        self.image.blit(text_image, (offset_x, offset_y))