import pygame
import random
from button import Button
from cube import Cube
from board import Board
from constants import *
from tetrimino import *
from leaderboard import Leaderboard


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
        self.speed = SPEED_LEVEL[self.level]

        self.grid_list = GRID_INIT.tolist()
        self.grid = []
        x = y = MARGIN
        for line in self.grid_list:
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
                self.grid_nex_tetris.append(Cube(x=x, y=y, type="bg"))
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

        self.leaderboard = Leaderboard()

        shape = random.choice(TETRIMINO_ID)
        if shape == "I":
            self.tetrimino = I()
        elif shape == "O":
            self.tetrimino = O()
        elif shape == "J":
            self.tetrimino = J()
        elif shape == "Z":
            self.tetrimino = Z()
        elif shape == "S":
            self.tetrimino = S()
        elif shape == "I":
            self.tetrimino = I()
        elif shape == "L":
            self.tetrimino = L()

        self.next_tetrimino = NextTetrimino(shape=random.choice(TETRIMINO_ID))

        # pressed keyboard
        self.pressed = {
            pygame.K_RIGHT: False,
            pygame.K_LEFT: False,
            pygame.K_DOWN: False
        }

    def new_game(self):
        self.__init__()

    def update_game(self):
        # Update moving clocks
        self.tetrimino.time_last_move_down += self.tetrimino.clock_down.get_time()
        self.tetrimino.clock_down.tick()
        self.tetrimino.time_last_move_right += self.tetrimino.clock_right.get_time()
        self.tetrimino.clock_right.tick()
        self.tetrimino.time_last_move_left += self.tetrimino.clock_left.get_time()
        self.tetrimino.clock_left.tick()
        if (self.tetrimino.time_last_move_down / 1000 >= self.speed) or \
                (self.pressed[pygame.K_DOWN] and self.tetrimino.time_last_move_down / 1000 >= TIME_BETWEEN_MOVE):
            # try to move down
            #   - if not possible (return position of cubes of triominos)
            #   - if possible (return True)
            positions = self.tetrimino.move_down(self.grid_list)
            # if triomino can't move down => new triomino
            if type(positions) == list:
                # update score
                self.score += SCORING["tetrimino"] * (self.level + 1)
                # add triomino to grid if can't move down
                for pos in positions:
                    self.grid_list[pos[1]][pos[0]] = self.tetrimino.shape.lower()
                self.update_grid()
                shape = self.next_tetrimino.shape
                exec('self.tetrimino = ' + shape + '()')
                if self.tetrimino.is_over_other_cube(self.grid_list):
                    # game over
                    self.leaderboard.new_record(
                        self.score, self.level, self.lines, int(self.APM), int(self.time_playing / 1000)
                    )
                    return "game_over"
                self.next_tetrimino = NextTetrimino(shape=random.choice(TETRIMINO_ID))
                self.check_completed_lines()
        if self.pressed[pygame.K_RIGHT] and not self.pressed[pygame.K_LEFT] and \
                self.tetrimino.time_last_move_right / 1000 >= TIME_BETWEEN_MOVE:
            self.actions += 1
            self.tetrimino.move_right(self.grid_list)
        if self.pressed[pygame.K_LEFT] and not self.pressed[pygame.K_RIGHT] and \
                self.tetrimino.time_last_move_left / 1000 >= TIME_BETWEEN_MOVE:
            self.actions += 1
            self.tetrimino.move_left(self.grid_list)

        self.update_statistics_board()

    def update_grid(self):
        self.grid = []
        x = y = MARGIN
        for line in self.grid_list:
            for cube in line:
                if cube == "w":
                    self.grid.append(Cube(x=x, y=y, type="wall"))
                elif cube == "e":
                    self.grid.append(Cube(x=x, y=y))
                else:
                    self.grid.append(Cube(x=x, y=y, type=cube.upper()))
                x += CUBE_SIZE
            x = MARGIN
            y += CUBE_SIZE

    def update_statistics_board(self):
        self.update_APM()
        self.board[5].update_text(str(self.level))
        self.board[6].update_text(str(self.score))
        self.board[7].update_text(str(self.lines))
        self.board[8].update_text(str(int(self.APM)))
        self.board[9].update_text(str(int(self.get_playing_time())))

    def check_completed_lines(self):
        # caculate number of completed lines by creating bool list of completed lines
        li_completed_lines = (np.array(self.grid_list) != "e").sum(axis=1) == TETRIS_WIDTH + 2
        li_completed_lines = li_completed_lines[1:len(li_completed_lines)-1].tolist()
        nb_lines = sum(li_completed_lines)
        if nb_lines > 0:
            id_completed_lines = np.arange(1, 23)[li_completed_lines].tolist()
            id_completed_lines.reverse()
            for id in id_completed_lines:
                del self.grid_list[id]
            for i in range(nb_lines):
                self.grid_list.insert(1, ['e'] * (TETRIS_WIDTH + 2))
                self.grid_list[1][0], self.grid_list[1][TETRIS_WIDTH + 1] = ("w", "w")
            # update cube position
            self.update_grid()
            # update statistics board
            self.lines += nb_lines
            self.level_score += LEVEL_SCORING[str(nb_lines)+"_line"]
            self.level = self.level_score // 10
            self.score += SCORING[str(nb_lines)+"_line"] * (self.level + 1)
            self.update_speed()

    def get_playing_time(self):
        return self.time_playing / 1000

    def update_APM(self):
        try:
            self.APM = self.actions / (self.get_playing_time() / 60)
        except ZeroDivisionError:
            self.APM = 0

    def update_speed(self):
        try:
            self.speed = SPEED_LEVEL[self.level]
        except KeyError:
            # if level is over 28
            self.speed = SPEED_LEVEL["+"]

    def update_time_out_of_playing(self):
        self.time_out_of_playing += self.clock.get_time()
        self.clock.tick()

    def update_time_playing(self):
        self.time_playing += self.clock.get_time()
        self.clock.tick()

