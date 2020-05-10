import numpy as np
import pygame


###################
# INTERFACE INFOS #
###################

TITLE = "Tetris"
ICON = 'img/icone_tetris_2.png'
MUSIC = "sound/Tetris-99-Theme.wav"
# MUSIC = "sound/Original-Tetris-Theme.wav"
VOLUME = .5

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
MARGIN = 10

BUTTON_QUIT_SIZE = (105, 40)
BUTTON_PAUSE_SIZE = (164, 40)
PAUSE_MESSAGE_SIZE = (500, 182)
VOLUME_BUTTON_SIZE = 30

BUTTON_QUIT_POS = (490, 600)
BUTTON_PAUSE_POS = (460, 550)
PAUSE_MESSAGE_POS = (110, 250)
STATISTICS_BOARD_POS = (410, 80)
STATISTICS_BOARD_LINE_HEIGHT = 40
STATISTICS_BOARD_COL_WIDTH = 150
BUTTON_SOUND_POS = (SCREEN_WIDTH - 7 * MARGIN - 4 * VOLUME_BUTTON_SIZE,
                    SCREEN_HEIGHT - MARGIN - VOLUME_BUTTON_SIZE)
BUTTON_MUTE_POS = (SCREEN_WIDTH - 5 * MARGIN - 3 * VOLUME_BUTTON_SIZE,
                   SCREEN_HEIGHT - MARGIN - VOLUME_BUTTON_SIZE)
BUTTON_SOUNDUP_POS = (SCREEN_WIDTH - 3 * MARGIN - 2 * VOLUME_BUTTON_SIZE,
                      SCREEN_HEIGHT - MARGIN - VOLUME_BUTTON_SIZE)
BUTTON_SOUNDDOWN_POS = (SCREEN_WIDTH - MARGIN - VOLUME_BUTTON_SIZE,
                        SCREEN_HEIGHT - MARGIN - VOLUME_BUTTON_SIZE)
NEXT_TETRIS_TEXT_POS = (410, 320)
NEXT_TETRIS_POS = (480, 365)

# official dim by Tetris Guidelines
TETRIS_WIDTH = 10
TETRIS_HEIGHT = 22

# SIze of tetrimino cube (in pixels)
CUBE_SIZE = 30

GRID_LEGEND = {
    "e": "empty",
    "w": "wall",
    "I": "tetrimino I",
    "J": "tetrimino J",
    "O": "tetrimino O",
    "S": "tetrimino S",
    "T": "tetrimino T",
    "Z": "tetrimino Z",
    "L": "tetrimino L",
}
GRID_INIT = np.array([["w"] * (TETRIS_WIDTH + 1)] * (TETRIS_HEIGHT + 1))
GRID_INIT[1:-1, 1:-1] = "e"
# GRID_INIT.tolist()


# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# FONTS
FONT_ARCADE_IN = 'font/8-bit Arcade In.ttf'
FONT_ARCADE_OUT = 'font/8-bit Arcade OUT.ttf'


##################
# GAMEPLAY INFOS #
##################

# https://tetris.wiki/Tetris_(NES,_Nintendo)
FPS_NITENDO = 60.0988
SPEED_LEVEL = {
    0: 48 / FPS_NITENDO,
    1: 43 / FPS_NITENDO,
    2: 38 / FPS_NITENDO,
    3: 33 / FPS_NITENDO,
    4: 28 / FPS_NITENDO,
    5: 23 / FPS_NITENDO,
    6: 18 / FPS_NITENDO,
    7: 13 / FPS_NITENDO,
    8: 8 / FPS_NITENDO,
    9: 6 / FPS_NITENDO,
    10: 5 / FPS_NITENDO,
    11: 5 / FPS_NITENDO,
    12: 5 / FPS_NITENDO,
    13: 4 / FPS_NITENDO,
    14: 4 / FPS_NITENDO,
    15: 4 / FPS_NITENDO,
    16: 3 / FPS_NITENDO,
    17: 3 / FPS_NITENDO,
    18: 3 / FPS_NITENDO,
    19: 2 / FPS_NITENDO,
    20: 2 / FPS_NITENDO,
    21: 2 / FPS_NITENDO,
    22: 2 / FPS_NITENDO,
    23: 2 / FPS_NITENDO,
    24: 2 / FPS_NITENDO,
    25: 2 / FPS_NITENDO,
    26: 2 / FPS_NITENDO,
    27: 2 / FPS_NITENDO,
    28: 2 / FPS_NITENDO,
    "+": 1 / FPS_NITENDO,
}

# each scoring point multiplied by (level + 1)     + 1 so that points are still scored at level 0
# https://tetris.fandom.com/wiki/Scoring#Guideline_scoring_system
SCORING = {
    "1_line": 40,
    "2_line": 100,
    "3_line": 300,
    "4_line": 1200,
    "tetrimino": 4
}

# https://tetris.fandom.com/wiki/Tetris_Guideline
# count when next level is past (by clearing lines)
NEXT_LEVEL = 10
LEVEL_SCORING = {
    "1_line": 1,
    "2_line": 3,
    "3_line": 5,
    "4_line": 8,
}


##############################
# AZERTY KEYBORD TRANSLATION #
##############################

class AZERTY:
    """AZERTY TRANSLATION"""
    K_p = pygame.K_p
    K_r = pygame.K_r
    K_q = pygame.K_a
