import pygame
from constants import *


def handle_state_playing(game, screen, sound, state="playing", running=True):
    # apply background
    screen.fill(BLACK)

    # apply grid
    for cube in game.grid:
        screen.blit(cube.image, cube.rect)

    # apply grid next tetrimino
    for cube in game.grid_nex_tetris:
        screen.blit(cube.image, cube.rect)

    # apply statistics board
    for text in game.board:
        screen.blit(text.text, text.rect)

    # apply buttons
    for button in game.buttons:
        screen.blit(button.image, button.rect)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:

            if 0 < event.pos[0] - BUTTON_PAUSE_POS[0] < BUTTON_PAUSE_SIZE[0] and \
                    0 < event.pos[1] - BUTTON_PAUSE_POS[1] < BUTTON_PAUSE_SIZE[1]:
                state = "pause"
                game.pause()

            elif 0 < event.pos[0] - BUTTON_QUIT_POS[0] < BUTTON_QUIT_SIZE[0] and \
                    0 < event.pos[1] - BUTTON_QUIT_POS[1] < BUTTON_QUIT_SIZE[1]:
                return "end", False

            elif 0 < event.pos[0] - BUTTON_SOUND_POS[0] < VOLUME_BUTTON_SIZE and \
                    0 < event.pos[1] - BUTTON_SOUND_POS[1] < VOLUME_BUTTON_SIZE:
                sound.set_volume(VOLUME)

            elif 0 < event.pos[0] - BUTTON_MUTE_POS[0] < VOLUME_BUTTON_SIZE and \
                    0 < event.pos[1] - BUTTON_MUTE_POS[1] < VOLUME_BUTTON_SIZE:
                sound.set_volume(0)

            elif 0 < event.pos[0] - BUTTON_SOUNDUP_POS[0] < VOLUME_BUTTON_SIZE and \
                    0 < event.pos[1] - BUTTON_SOUNDUP_POS[1] < VOLUME_BUTTON_SIZE:
                sound.set_volume(sound.get_volume() + 0.1)

            elif 0 < event.pos[0] - BUTTON_SOUNDDOWN_POS[0] < VOLUME_BUTTON_SIZE and \
                    0 < event.pos[1] - BUTTON_SOUNDDOWN_POS[1] < VOLUME_BUTTON_SIZE:
                sound.set_volume(sound.get_volume() - 0.1)

        elif event.type == pygame.KEYUP:

            if event.key == AZERTY.K_p:
                state = "pause"
                game.pause()

            elif event.key == AZERTY.K_q:
                return "end", False

        # if window is closed
        elif event.type == pygame.QUIT:
            return "end", False

    return state, running


def handle_state_menu(game, screen, bg, sound, state="menu", running=True):

    screen.blit(bg, BG_MENU_POS)

    # apply buttons
    for button in game.menu_buttons:
        screen.blit(button.image, button.rect)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:
            pass

        # if window is closed
        elif event.type == pygame.QUIT:
            return "end", False

    return state, running


def handle_state_pause(game, screen, sound, state="pause", running=True):

    # apply pause button
    screen.blit(game.pause_message.image, game.pause_message.rect)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if 0 < event.pos[0] - PAUSE_MESSAGE_POS[0] < PAUSE_MESSAGE_SIZE[0] and \
                 0 < event.pos[1] - PAUSE_MESSAGE_POS[1] < PAUSE_MESSAGE_SIZE[1]:
                state = "playing"
                game.resume()

        elif event.type == pygame.KEYUP:
            if state == "pause" and event.key == AZERTY.K_r:
                state = "playing"
                game.resume()

        # if window is closed
        elif event.type == pygame.QUIT:
            return "end", False

    return state, running
