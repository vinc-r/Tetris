import pygame
import os
from constants import *
from game import Game
from functions_handdle_state import *


if __name__ == "__main__":

    # initialize pygame window
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % WINDOWS_POSITION
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_icon(pygame.image.load(ICON))

    # initialize sound
    sound = pygame.mixer.Sound(MUSIC)
    sound.play(loops=-1)
    sound.set_volume(VOLUME)

    # initialize bacjground menu
    background = pygame.image.load("img/menu_bg.jpg")

    # initialize game
    game = Game()

    running = True
    state = "menu"

    while running:

        # apply background
        screen.fill(BLACK)

        print(state)

        if state == "playing":
            state, running = handle_state_playing(game=game, screen=screen, sound=sound)
        elif state == "pause":
            state, running = handle_state_pause(game=game, screen=screen, sound=sound)
        elif state == "menu":
            state, running = handle_state_menu(game=game, screen=screen, bg=background, sound=sound)

        # update screen
        pygame.display.flip()

        # check if ended and close game
        if state == "end" and not running:
            sound.stop()
            pygame.quit()
            print("\nGOOD BYE !")
