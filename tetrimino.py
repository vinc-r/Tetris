import pygame
import random
from cube import Cube
from constants import MARGIN, CUBE_SIZE, NEXT_TETRIS_POS, TIME_BETWEEN_MOVE, TETRIMINO_ID, NEXT_TETRIS_CUBES_POS


def convert_pixel_positions(positions_pixels):
    return [convert_pixel_position(pos) for pos in positions_pixels]


def convert_pixel_position(positions_pixels):
    return int((positions_pixels[0] - MARGIN) / CUBE_SIZE), int((positions_pixels[1] - MARGIN) / CUBE_SIZE)


# translation_dict to spin tetrimino who can hold in 3*3 square (L, J, S, T, Z)
SPIN_3X3 = {
    "top_left": (2, 0, "top_right"),
    "top": (1, 1, "right"),
    "top_right": (0, 2, "bottom_right"),
    "right": (-1, 1, "bottom"),
    "bottom_right": (-2, 0, "bottom_left"),
    "bottom": (-1, -1, "left"),
    "bottom_left": (0, -2, "top_left"),
    "left": (1, -1, "top")
}

# translation_dict to spin tetrimino who can hold in 4*4 square => only for I
# ex : line_1_col_0 will be change to line_0_col_2 after spin
SPIN_4X4 = {
    "l0_c1": (2, 1, "l1_c3"),
    "l0_c2": (1, 2, "l2_c3"),
    "l1_c3": (-1, 2, "l3_c2"),
    "l2_c3": (-2, 1, "l3_c1"),
    "l3_c2": (-2, -1, "l2_c0"),
    "l3_c1": (-1, -2, "l1_c0"),
    "l2_c0": (1, -2, "l0_c1"),
    "l1_c0": (2, -1, "l0_c2"),
    "l1_c1": (1, 0, "l1_c2"),
    "l1_c2": (0, 1, "l2_c2"),
    "l2_c2": (-1, 0, "l2_c1"),
    "l2_c1": (0, -1, "l1_c1")
}


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
        self.spin_state = 0

    def move_down(self, grid):
        positions_pixels = [(cube.rect.x, cube.rect.y) for cube in self.cubes]
        positions = convert_pixel_positions(positions_pixels)
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
        positions = convert_pixel_positions(positions_pixels)
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
        positions = convert_pixel_positions(positions_pixels)
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

    def spin_tetrimino_3X3(self, grid):
        movement_allowed = True

        for cube in self.cubes:
            if cube.pos != "center":
                future_pos = convert_pixel_position((
                    cube.rect.x + CUBE_SIZE * SPIN_3X3[cube.pos][0],
                    cube.rect.y + CUBE_SIZE * SPIN_3X3[cube.pos][1]
                ))
                if grid[future_pos[1]][future_pos[0]] != "e":
                    movement_allowed = False
                    break

        if movement_allowed:

            for cube in self.cubes:
                if cube.pos != "center":
                    cube.rect.x += CUBE_SIZE * SPIN_3X3[cube.pos][0]
                    cube.rect.y += CUBE_SIZE * SPIN_3X3[cube.pos][1]
                    cube.pos = SPIN_3X3[cube.pos][2]
            print("SPIN")


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
        # no spin for Tetrimino O (always the same position)
        pass


class I(Tetrimino):

    def __init__(self):
        super().__init__(shape="I")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 2, pos="l1_c0"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2, pos="l1_c1"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 2, pos="l1_c2"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 7, y=MARGIN + CUBE_SIZE * 2, pos="l1_c3")
        ]

    def spin_tetrimino(self, grid):
        movement_allowed = True

        for cube in self.cubes:
            future_pos = convert_pixel_position((
                cube.rect.x + CUBE_SIZE * SPIN_4X4[cube.pos][0],
                cube.rect.y + CUBE_SIZE * SPIN_4X4[cube.pos][1]
            ))
            if grid[future_pos[1]][future_pos[0]] != "e":
                movement_allowed = False
                break

        if movement_allowed:
            for cube in self.cubes:
                cube.rect.x += CUBE_SIZE * SPIN_4X4[cube.pos][0]
                cube.rect.y += CUBE_SIZE * SPIN_4X4[cube.pos][1]
                cube.pos = SPIN_4X4[cube.pos][2]
            self.spin_state = (self.spin_state + 1) % 4

            print("SPIN")


class J(Tetrimino):

    def __init__(self):
        super().__init__(shape="J")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 1, pos="top_left"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 2, pos="left"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2, pos="center"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 2, pos="right")
        ]

    def spin_tetrimino(self, grid):
        self.spin_tetrimino_3X3(grid)


class S(Tetrimino):

    def __init__(self):
        super().__init__(shape="S")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 2, pos="left"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2, pos="center"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 1, pos="top"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 1, pos="top_right")
        ]

    def spin_tetrimino(self, grid):
        self.spin_tetrimino_3X3(grid)


class T(Tetrimino):

    def __init__(self):
        super().__init__(shape="T")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 2, pos="left"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2, pos="center"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 1, pos="top"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 2, pos="right")
        ]

    def spin_tetrimino(self, grid):
        self.spin_tetrimino_3X3(grid)


class Z(Tetrimino):

    def __init__(self):
        super().__init__(shape="Z")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 1, pos="top_left"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 1, pos="top"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2, pos="center"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 2, pos="right")
        ]

    def spin_tetrimino(self, grid):
        self.spin_tetrimino_3X3(grid)


class L(Tetrimino):

    def __init__(self):
        super().__init__(shape="L")
        self.cubes = [
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 4, y=MARGIN + CUBE_SIZE * 2, pos="left"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 5, y=MARGIN + CUBE_SIZE * 2, pos="center"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 2, pos="right"),
            Cube(type=self.shape, x=MARGIN + CUBE_SIZE * 6, y=MARGIN + CUBE_SIZE * 1, pos="top_right")
        ]

    def spin_tetrimino(self, grid):
        self.spin_tetrimino_3X3(grid)