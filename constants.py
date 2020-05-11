import numpy as np
import pygame


###################
# INTERFACE INFOS #
###################

TITLE = "Tetris"
ICON = 'img/icone_tetris_2.png'
MUSIC = "sound/Tetris-99-Theme.wav"
# MUSIC = "sound/Original-Tetris-Theme.wav"
VOLUME = .1

WINDOWS_POSITION = (200, 30)
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 700
MARGIN = 10

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# FONTS
FONT_ARCADE_IN = 'font/8-bit Arcade In.ttf'
FONT_ARCADE_OUT = 'font/8-bit Arcade OUT.ttf'

####################
# BUTTONS SIZE/POS #
####################

# MENU SIZE POS
BG_MENU_POS = (-225.5, 60)
BUTTON_MENU_PLAY_POS = (172, 340)
BUTTON_MENU_AIPLAY_POS = (172, 420)
BUTTON_MENU_LEADERBOARD_POS = (80, 500)
BUTTON_MENU_QUIT_POS = (225, 580)
BUTTON_MENU_PLAY_SIZE = (372, 65)
BUTTON_MENU_AIPLAY_SIZE = (372, 65)
BUTTON_MENU_LEADERBOARD_SIZE = (575, 65)
BUTTON_MENU_QUIT_SIZE = (279, 65)

# PLAYING SIZE POS
BUTTON_QUIT_SIZE = (105, 40)
BUTTON_PAUSE_SIZE = (164, 40)
PAUSE_MESSAGE_SIZE = (500, 182)
VOLUME_BUTTON_SIZE = 30
BUTTON_QUIT_POS = (490, 600)
BUTTON_PAUSE_POS = (460, 550)
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
NEXT_TETRIS_CUBES_POS = {
    "O": ((1, 1), (2, 1), (1, 2), (2, 2)),
    "I": ((0, 1), (1, 1), (2, 1), (3, 1)),
    "J": ((0, 1), (0, 2), (1, 2), (2, 2)),
    "S": ((0, 2), (1, 2), (1, 1), (2, 1)),
    "T": ((0, 2), (1, 2), (1, 1), (2, 2)),
    "Z": ((0, 1), (1, 1), (1, 2), (2, 2)),
    "L": ((0, 2), (1, 2), (2, 2), (2, 1))
}

# PAUSE SIZE POS
PAUSE_MESSAGE_POS = (110, 250)

# GAME OVER SIZE POS
GAME_OVER_IMAGE_POS = (210, 180)
GAME_OVER_MENU_IMAGE_POS = (255, 580)
GAME_OVER_MENU_IMAGE_SIZE = (210, 50)

##################
# GAMEPLAY INFOS #
##################

# official dim by Tetris Guidelines
TETRIS_WIDTH = 10
TETRIS_HEIGHT = 22

# SIze of tetrimino cube (in pixels)
CUBE_SIZE = 28

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
GRID_INIT = np.array([["w"] * (TETRIS_WIDTH + 2)] * (TETRIS_HEIGHT + 2))
GRID_INIT[1:-1, 1:-1] = "e"
# GRID_INIT.tolist()

TETRIMINO_ID = ["I", "J", "O", "S", "T", "Z", "L"]

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
# time between move when keyboard is maintain
TIME_BETWEEN_MOVE = 5 / 60

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
    K_m = pygame.K_SEMICOLON
    K_SPACE = pygame.K_SPACE
    K_LEFT = pygame.K_LEFT
    K_RIGHT = pygame.K_RIGHT
    K_UP = pygame.K_UP
    K_DOWN = pygame.K_DOWN
