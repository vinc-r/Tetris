import pygame
from constants import *


def handle_state_playing(game, screen, sound, state="playing", running=True):

    # update clock
    game.update_time_playing()

    # update board game
    if game.update_game() == "game_over":
        return "game_over", True

    # apply background
    screen.fill(BLACK)

    # apply grid
    for cube in game.grid:
        screen.blit(cube.image, cube.rect)

    # apply actual tetrimino
    for cube in game.tetrimino.cubes:
        screen.blit(cube.image, cube.rect)

    # apply grid next tetrimino
    for cube in game.grid_nex_tetris:
        screen.blit(cube.image, cube.rect)

    # apply next tetrimino on grid next tetrimino
    for cube in game.next_tetrimino.cubes:
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
                return "pause", running

            elif 0 < event.pos[0] - BUTTON_QUIT_POS[0] < BUTTON_QUIT_SIZE[0] and \
                    0 < event.pos[1] - BUTTON_QUIT_POS[1] < BUTTON_QUIT_SIZE[1]:
                return "menu", running

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

        elif event.type == pygame.KEYDOWN:

            if event.key == AZERTY.K_p:
                state = "pause"

            elif event.key == AZERTY.K_q:
                return "menu", running

            elif event.key == AZERTY.K_SPACE:
                game.tetrimino.drop_tetrimino(game.grid_list)
                game.tetrimino.time_last_move_down = game.speed * 1000
                game.actions += 1
                if game.update_game() == "game_over":
                    return "game_over", running

            elif event.key in [AZERTY.K_LEFT, AZERTY.K_RIGHT, AZERTY.K_DOWN]:
                game.pressed[event.key] = True

            elif event.key == AZERTY.K_UP:
                game.tetrimino.spin_tetrimino(game.grid_list)

        elif event.type == pygame.KEYUP:
            if event.key in [AZERTY.K_LEFT, AZERTY.K_RIGHT, AZERTY.K_DOWN]:
                game.pressed[event.key] = False
                if event.key == AZERTY.K_LEFT:
                    game.tetrimino.time_last_move_left = TIME_BETWEEN_MOVE  # init able to move
                    game.tetrimino.clock_left.tick()
                if event.key == AZERTY.K_RIGHT:
                    game.tetrimino.time_last_move_right = TIME_BETWEEN_MOVE # init able to move
                    game.tetrimino.clock_right.tick()
                if event.key == AZERTY.K_DOWN:
                    game.tetrimino.time_last_move_down = 0                  # init not able to move yet
                    game.tetrimino.clock_down.tick()

        # if window is closed
        elif event.type == pygame.QUIT:
            return "end", False

    return state, running


def handle_state_menu(game, screen, bg, sound, state="menu", running=True):

    # update clock
    game.update_time_out_of_playing()

    screen.blit(bg, BG_MENU_POS)

    # apply buttons
    for button in game.menu_buttons:
        screen.blit(button.image, button.rect)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:
            if 0 < event.pos[0] - BUTTON_MENU_PLAY_POS[0] < BUTTON_MENU_PLAY_SIZE[0] and \
                    0 < event.pos[1] - BUTTON_MENU_PLAY_POS[1] < BUTTON_MENU_PLAY_SIZE[0]:
                state = "playing"
                game.new_game()

            if 0 < event.pos[0] - BUTTON_MENU_QUIT_POS[0] < BUTTON_MENU_QUIT_SIZE[0] and \
                    0 < event.pos[1] - BUTTON_MENU_QUIT_POS[1] < BUTTON_MENU_QUIT_SIZE[1]:
                return "end", False

        # if window is closed
        elif event.type == pygame.QUIT:
            return "end", False

        elif event.type == pygame.KEYUP:

            if event.key == AZERTY.K_p:
                state = "playing"
                game.new_game()

            elif event.key == AZERTY.K_q:
                return "end", False

    return state, running


def handle_state_pause(game, screen, sound, state="pause", running=True):

    # update clock
    game.update_time_out_of_playing()

    # apply pause button
    screen.blit(game.pause_message.image, game.pause_message.rect)

    # apply volume buttons
    for button in game.buttons[2:]:
        screen.blit(button.image, button.rect)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:

            if 0 < event.pos[0] - PAUSE_MESSAGE_POS[0] < PAUSE_MESSAGE_SIZE[0] and \
                    0 < event.pos[1] - PAUSE_MESSAGE_POS[1] < PAUSE_MESSAGE_SIZE[1]:
                state = "playing"

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
            if state == "pause" and event.key == AZERTY.K_r:
                state = "playing"

        # if window is closed
        elif event.type == pygame.QUIT:
            return "end", False

    return state, running


def handle_state_game_over(game, screen, sound, state="game_over", running=True):

    # apply background
    screen.fill(BLACK)

    # apply grid
    for cube in game.grid:
        screen.blit(cube.image, cube.rect)

    # apply actual tetrimino
    for cube in game.tetrimino.cubes:
        screen.blit(cube.image, cube.rect)

    # apply grid next tetrimino
    for cube in game.grid_nex_tetris:
        screen.blit(cube.image, cube.rect)

    # apply next tetrimino on grid next tetrimino
    for cube in game.next_tetrimino.cubes:
        screen.blit(cube.image, cube.rect)

    # apply statistics board
    for text in game.board:
        screen.blit(text.text, text.rect)

    # apply buttons
    for button in game.buttons:
        screen.blit(button.image, button.rect)

    # apply game over image
    screen.blit(pygame.image.load("img/game_over.jpg"), GAME_OVER_IMAGE_POS)
    screen.blit(pygame.image.load("img/menu.png"), GAME_OVER_MENU_IMAGE_POS)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:

            if 0 < event.pos[0] - GAME_OVER_MENU_IMAGE_POS[0] < GAME_OVER_MENU_IMAGE_SIZE[0] and \
                    0 < event.pos[1] - GAME_OVER_MENU_IMAGE_POS[1] < GAME_OVER_MENU_IMAGE_SIZE[1]:
                return "menu", running

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

        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == AZERTY.K_m:
                return "menu", running

        # if window is closed
        elif event.type == pygame.QUIT:
            return "end", False

    return state, running