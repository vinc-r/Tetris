import pygame
from constants import FONT_ARCADE_IN, FONT_ARCADE_OUT, STATISTICS_BOARD_POS, WHITE

# initialize font
pygame.font.init()


class Board:

    def __init__(self, text="", font_size=40, font=FONT_ARCADE_IN, pos=(0, 0), y_offset=0, x_offset=0):

        self.font = pygame.font.Font(font, font_size)
        self.text = self.font.render(text, True, WHITE)
        self.rect = self.text.get_rect()
        self.rect.x = pos[0] + x_offset
        self.rect.y = pos[1] + y_offset

    def update_text(self, new_text=""):
        self.text = self.font.render(new_text, True, WHITE)
