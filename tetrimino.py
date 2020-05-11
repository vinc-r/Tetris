import pygame
import random
from cube import Cube
from constants import MARGIN, CUBE_SIZE, NEXT_TETRIS_POS, TIME_BETWEEN_MOVE, TETRIMINO_ID, NEXT_TETRIS_CUBES_POS


def convert_pixel_position(positions_pixels):
    return [(int((pos[0]-MARGIN)/CUBE_SIZE), int((pos[1]-MARGIN)/CUBE_SIZE)) for pos in positions_pixels]


class Tetrimino:

    def __init__(self, shape=random.choice(TETRIMINO_ID)):
        self.shape = shape
        # initialize moving clocks
        self.clock_down = pygame.time.Clock()
        self.time_last_move_down = 0                # init 0 sec (not moving yet)
        self.clock_left = pygame.time.Clock()
        self.time_last_move_left = TIME_BETWEEN_MOVE        # init able to move
        self.clock_right = pygame.time.Clock()
        self.time_last_move_right = TIME_BETWEEN_MOVE       # init able to move
        # initialize empty cubes
        self.cubes = []

    def move_down(self, grid):
        positions_pixels = [(cube.rect.x, cube.rect.y) for cube in self.cubes]
        positions = convert_pixel_position(positions_pixels)
        for pos in positions:
            if grid[pos[1]+1][pos[0]] != "e":
                return positions
        for cube in self.cubes:
            cube.rect.y += CUBE_SIZE
        self.time_last_move_down = 0
        self.clock_down.tick()
        return True

    def move_left(self, grid):
        positions_pixels = [(cube.rect.x, cube.rect.y) for cube in self.cubes]
        positions = convert_pixel_position(positions_pixels)
        for pos in positions:
            if grid[pos[1]][pos[0]-1] != "e":
                return False
        for cube in self.cubes:
            cube.rect.x -= CUBE_SIZE
        self.time_last_move_left = 0
        self.clock_left.tick()
        return True

    def move_right(self, grid):
        positions_pixels = [(cube.rect.x, cube.rect.y) for cube in self.cubes]
        positions = convert_pixel_position(positions_pixels)
        for pos in positions:
            if grid[pos[1]][pos[0]+1] != "e":
                return False
        for cube in self.cubes:
            cube.rect.x += CUBE_SIZE
        self.time_last_move_right = 0
        self.clock_right.tick()
        return True

    def drop_tetrimino(self, grid):
        positions = self.move_down(grid)
        while type(positions) == bool and positions:
            positions = self.move_down(grid)
        return positions





class NextTetrimino:

    def __init__(self, shape=random.choice(TETRIMINO_ID)):
        assert shape in TETRIMINO_ID
        self.shape = shape
        self.cubes = [
            Cube(type=shape, x=NEXT_TETRIS_POS[0] + CUBE_SIZE * NEXT_TETRIS_CUBES_POS[shape][0][0],
                 y=NEXT_TETRIS_POS[1] + CUBE_SIZE * NEXT_TETRIS_CUBES_POS[shape][0][1]),
            Cube(type=shape, x=NEXT_TETRIS_POS[0] + CUBE_SIZE * NEXT_TETRIS_CUBES_POS[shape][1][0],
                 y=NEXT_TETRIS_POS[1] + CUBE_SIZE * NEXT_TETRIS_CUBES_POS[shape][1][1]),
            Cube(type=shape, x=NEXT_TETRIS_POS[0] + CUBE_SIZE * NEXT_TETRIS_CUBES_POS[shape][2][0],
                 y=NEXT_TETRIS_POS[1] + CUBE_SIZE * NEXT_TETRIS_CUBES_POS[shape][2][1]),
            Cube(type=shape, x=NEXT_TETRIS_POS[0] + CUBE_SIZE * NEXT_TETRIS_CUBES_POS[shape][3][0],
                 y=NEXT_TETRIS_POS[1] + CUBE_SIZE * NEXT_TETRIS_CUBES_POS[shape][3][1])
        ]


class O(Tetrimino):

    def __init__(self):
        super().__init__(shape="O")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 1),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 1),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 2)
        ]

    def spin_tetrimino(self, grid):
        # TODO
        print("SPIN")


class I(Tetrimino):

    def __init__(self):
        super().__init__(shape="I")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 7, y=MARGIN + CUBE_SIZE * 2)
        ]

    def spin_tetrimino(self, grid):
        # TODO
        print("SPIN")


class J(Tetrimino):

    def __init__(self):
        super().__init__(shape="J")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 1),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 2)
        ]

    def spin_tetrimino(self, grid):
        # TODO
        print("SPIN")

class J(Tetrimino):

    def __init__(self):
        super().__init__(shape="J")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 1),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 2)
        ]

    def spin_tetrimino(self, grid):
        # TODO
        print("SPIN")


class S(Tetrimino):

    def __init__(self):
        super().__init__(shape="S")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 1),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 1)
        ]

    def spin_tetrimino(self, grid):
        # TODO
        print("SPIN")


class T(Tetrimino):

    def __init__(self):
        super().__init__(shape="T")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 1),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 1),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 1)
        ]

    def spin_tetrimino(self, grid):
        # TODO
        print("SPIN")


class Z(Tetrimino):

    def __init__(self):
        super().__init__(shape="Z")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 1),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 1),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 2)
        ]

    def spin_tetrimino(self, grid):
        # TODO
        print("SPIN")


class L(Tetrimino):

    def __init__(self):
        super().__init__(shape="L")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 1),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 1),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 2),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 1)
        ]

    def spin_tetrimino(self, grid):
        # TODO
        print("SPIN")