import pygame
from constants import *
from game import Game

def handle_state_playing(game, screen, state="playing", running=True):
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

    # update screen
    pygame.display.flip()

    # if window is closed
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONUP:

            if 0 < event.pos[0] - BUTTON_PAUSE_POS[0] < BUTTON_PAUSE_SIZE[0] and \
                    0 < event.pos[1] - BUTTON_PAUSE_POS[1] < BUTTON_PAUSE_SIZE[1]:
                state = "pause"
                game.pause()

            elif 0 < event.pos[0] - BUTTON_QUIT_POS[0] < BUTTON_QUIT_SIZE[0] and \
                    0 < event.pos[1] - BUTTON_QUIT_POS[1] < BUTTON_QUIT_SIZE[1]:
                running = False
                sound.stop()
                pygame.quit()
                print("\nGOOD BYE !")

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
                running = False
                sound.stop()
                pygame.quit()
                print("\nGOOD BYE !")

        elif event.type == pygame.QUIT:
            running = False
            sound.stop()
            pygame.quit()
            print("\nGOOD BYE !")

    return state, running



if __name__ == "__main__":

    # initialize pygame window
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_icon(pygame.image.load(ICON))

    # initialize sound
    sound = pygame.mixer.Sound(MUSIC)
    sound.play(loops=-1)
    sound.set_volume(VOLUME)

    # initialize game
    game = Game()

    running = True
    state = "playing"

    while running:

        """
        if state == "playing":
            handle_state_playing(game=game, screen=screen)
            """

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

        # update screen
        pygame.display.flip()

        # if window is closed
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:

                if state == "playing" and 0 < event.pos[0] - BUTTON_PAUSE_POS[0] < BUTTON_PAUSE_SIZE[0] and \
                        0 < event.pos[1] - BUTTON_PAUSE_POS[1] < BUTTON_PAUSE_SIZE[1]:
                    state = "pause"
                    game.pause()

                elif state == "playing" and 0 < event.pos[0] - BUTTON_QUIT_POS[0] < BUTTON_QUIT_SIZE[0] and \
                        0 < event.pos[1] - BUTTON_QUIT_POS[1] < BUTTON_QUIT_SIZE[1]:
                    running = False
                    sound.stop()
                    pygame.quit()
                    print("\nGOOD BYE !")

                elif state == "playing" and 0 < event.pos[0] - BUTTON_SOUND_POS[0] < VOLUME_BUTTON_SIZE and \
                        0 < event.pos[1] - BUTTON_SOUND_POS[1] < VOLUME_BUTTON_SIZE:
                    sound.set_volume(VOLUME)

                elif state == "playing" and 0 < event.pos[0] - BUTTON_MUTE_POS[0] < VOLUME_BUTTON_SIZE and \
                        0 < event.pos[1] - BUTTON_MUTE_POS[1] < VOLUME_BUTTON_SIZE:
                    sound.set_volume(0)

                elif state == "playing" and 0 < event.pos[0] - BUTTON_SOUNDUP_POS[0] < VOLUME_BUTTON_SIZE and \
                        0 < event.pos[1] - BUTTON_SOUNDUP_POS[1] < VOLUME_BUTTON_SIZE:
                    sound.set_volume(sound.get_volume() + 0.1)

                elif state == "playing" and 0 < event.pos[0] - BUTTON_SOUNDDOWN_POS[0] < VOLUME_BUTTON_SIZE and \
                        0 < event.pos[1] - BUTTON_SOUNDDOWN_POS[1] < VOLUME_BUTTON_SIZE:
                    sound.set_volume(sound.get_volume() - 0.1)

                elif state == "pause" and 0 < event.pos[0] - PAUSE_MESSAGE_POS[0] < PAUSE_MESSAGE_SIZE[0] and \
                                            0 < event.pos[1] - PAUSE_MESSAGE_POS[1] < PAUSE_MESSAGE_SIZE[1]:
                    state = "playing"
                    game.resume()

            elif event.type == pygame.KEYUP:

                if state == "pause" and event.key == AZERTY.K_r:
                    state = "playing"
                    game.resume()

                elif state == "playing" and event.key == AZERTY.K_p:
                    state = "pause"
                    game.pause()

                elif state == "playing" and event.key == AZERTY.K_q:
                    running = False
                    sound.stop()
                    pygame.quit()
                    print("\nGOOD BYE !")

            elif event.type == pygame.QUIT:
                running = False
                sound.stop()
                pygame.quit()
                print("\nGOOD BYE !")

    pygame.quit()
