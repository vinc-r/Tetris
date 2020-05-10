import pygame
from button import Button
from cube import Cube
from statistics_borad import Board
from constants import CUBE_SIZE, GRID_INIT, MARGIN, STATISTICS_BOARD_POS, STATISTICS_BOARD_LINE_HEIGHT
from constants import STATISTICS_BOARD_COL_WIDTH, NEXT_TETRIS_POS, NEXT_TETRIS_TEXT_POS


class Game:
    """
    Game class
    """

    def __init__(self):
        self.level = 0
        self.level_score = 0      # only to see when next level is achieve
        self.score = 0
        self.lines = 0
        self.clock = pygame.time.Clock()
        self.time_out_of_playing = 0
        self.time_playing = 0
        self.actions = 0
        self.APM = 0

        self.grid = []
        x = y = MARGIN
        for line in GRID_INIT.tolist():
            for cube in line:
                if cube == "w":
                    self.grid.append(Cube(x=x, y=y, type="wall"))
                elif cube == "e":
                    self.grid.append(Cube(x=x, y=y))
                x += CUBE_SIZE
            x = MARGIN
            y += CUBE_SIZE

        self.grid_nex_tetris = []
        x, y = NEXT_TETRIS_POS
        # add grid for next tetrimino
        for i in range(4):
            for j in range(4):
                self.grid.append(Cube(x=x, y=y, type="bg"))
                x += CUBE_SIZE
            x = NEXT_TETRIS_POS[0]
            y += CUBE_SIZE

        self.buttons = [
            Button("pause"),
            Button("quit"),
            Button("sound/sound"),
            Button("sound/mute"),
            Button("sound/sound_up"),
            Button("sound/sound_down")
        ]

        self.menu_buttons = [
            Button("menu_buttons/play"),
            Button("menu_buttons/ai_play"),
            Button("menu_buttons/leaderboard"),
            Button("menu_buttons/quit")
        ]

        self.pause_message = Button("pause_message")

        x_offset = STATISTICS_BOARD_COL_WIDTH
        y_offset = STATISTICS_BOARD_LINE_HEIGHT
        self.board = [
            Board("Level", pos=STATISTICS_BOARD_POS, y_offset=0),
            Board("Score", pos=STATISTICS_BOARD_POS, y_offset=y_offset*1),
            Board("Lines", pos=STATISTICS_BOARD_POS, y_offset=y_offset*2),
            Board("APM", pos=STATISTICS_BOARD_POS, y_offset=y_offset*3),
            Board("Time", pos=STATISTICS_BOARD_POS, y_offset=y_offset*4),

            Board(str(self.level), pos=STATISTICS_BOARD_POS, x_offset=x_offset, y_offset=0),
            Board(str(self.score), pos=STATISTICS_BOARD_POS, x_offset=x_offset, y_offset=y_offset * 1),
            Board(str(self.lines), pos=STATISTICS_BOARD_POS, x_offset=x_offset, y_offset=y_offset * 2),
            Board(str(self.APM), pos=STATISTICS_BOARD_POS, x_offset=x_offset, y_offset=y_offset * 3),
            Board(str(self.time_playing), pos=STATISTICS_BOARD_POS, x_offset=x_offset, y_offset=y_offset * 4),

            Board("Next Tetrimino", pos=NEXT_TETRIS_TEXT_POS)
        ]

    def update_board(self):
        self.board[0].update_text("Level")

    def get_playing_time(self):
        return self.time_playing / 1000

    def update_APM(self):
        self.APM = self.actions / self.get_playing_time()

    def pause(self):
        # self.pause_clock = pygame.time.Clock()
        self.clock.tick()

    def resume(self):
        self.time_out_of_playing += self.clock.get_time()
        self.clock.tick()


