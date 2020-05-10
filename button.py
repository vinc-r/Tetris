import pygame
from constants import *


class Button(pygame.sprite.Sprite):

    def __init__(self, type):
        super().__init__()
        self.image = pygame.image.load('img/'+type+'.png')
        self.rect = self.image.get_rect()
        if type == "pause":
            self.rect.x, self.rect.y = BUTTON_PAUSE_POS
        elif type == "quit":
            self.rect.x, self.rect.y = BUTTON_QUIT_POS
        elif type == "pause_message":
            self.rect.x, self.rect.y = PAUSE_MESSAGE_POS
        elif type == "sound/sound":
            self.rect.x, self.rect.y = BUTTON_SOUND_POS
        elif type == "sound/mute":
            self.rect.x, self.rect.y = BUTTON_MUTE_POS
        elif type == "sound/sound_up":
            self.rect.x, self.rect.y = BUTTON_SOUNDUP_POS
        elif type == "sound/sound_down":
            self.rect.x, self.rect.y = BUTTON_SOUNDDOWN_POS
        elif type == "menu_buttons/play":
            self.rect.x, self.rect.y = BUTTON_MENU_PLAY_POS
        elif type == "menu_buttons/ai_play":
            self.rect.x, self.rect.y = BUTTON_MENU_AIPLAY_POS
        elif type == "menu_buttons/leaderboard":
            self.rect.x, self.rect.y = BUTTON_MENU_LEADERBOARD_POS
        elif type == "menu_buttons/quit":
            self.rect.x, self.rect.y = BUTTON_MENU_QUIT_POS
