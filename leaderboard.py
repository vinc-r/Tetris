import pandas as pd
import os
from board import Board
import pygame
from constants import LEADERBOARD_MENU_POS, LEADERBOARD_POS, LEADERBOARD_BG_POS, MAX_NAME_LENGTH
from constants import LEADERBOARD_COL_WIDTH, LEADERBOARD_ROW_HEIGHT, MAX_LEADERBOARD, SUPP_COL_OFFSET


def get_leaderboard():
    return pd.read_csv("data/leaderboard.csv")


def save_leaderboard(df):
    df.to_csv('data/leaderboard.csv', index=False)


def new_record(score, level, lines, APM, time, name=os.getlogin()):

    # limit name size
    if len(name) > MAX_NAME_LENGTH:
        name = name[:MAX_NAME_LENGTH]

    df = get_leaderboard().append(
        pd.DataFrame([name, score, level, lines, APM, time], index=["name", "score", "level", "lines", "APM", "time"]).T
    ).sort_values(by="score", ascending=False).head(MAX_LEADERBOARD)

    save_leaderboard(df)


def return_to_zero_leaderboard():
    pd.DataFrame({
        "name": [""] * 5,
        "score": [0] * 5,
        "level": [0] * 5,
        "lines": [0] * 5,
        "APM": [0] * 5,
        "time": [0] * 5
    }).to_csv('data/leaderboard.csv', index=False)


class Leaderboard:

    def __init__(self):

        self.bg = pygame.image.load('img/leaderboard_bg.png')
        self.bg_pos = LEADERBOARD_BG_POS

        self.botton_menu = pygame.image.load('img/menu.png')
        self.botton_menu_pos = LEADERBOARD_MENU_POS

        self.board = [
            Board("Name", pos=LEADERBOARD_POS, x_offset=0, font_size=35),
            Board("Score", pos=LEADERBOARD_POS, x_offset=LEADERBOARD_COL_WIDTH*1, font_size=35),
            Board("Level", pos=LEADERBOARD_POS, x_offset=LEADERBOARD_COL_WIDTH*2+SUPP_COL_OFFSET, font_size=35),
            Board("Lines", pos=LEADERBOARD_POS, x_offset=LEADERBOARD_COL_WIDTH*3+SUPP_COL_OFFSET, font_size=35),
            Board("APM", pos=LEADERBOARD_POS, x_offset=LEADERBOARD_COL_WIDTH*4+SUPP_COL_OFFSET, font_size=35),
            Board("Time", pos=LEADERBOARD_POS, x_offset=LEADERBOARD_COL_WIDTH*5+SUPP_COL_OFFSET, font_size=35),
        ]

        df = get_leaderboard()

        # rows
        for i in range(df.shape[0]):
            # columns
            for j in range(df.shape[1]):
                # larger col for score
                if j > 1:
                    supp_col_offset = SUPP_COL_OFFSET
                else: supp_col_offset = 0
                self.board.append(
                    Board(
                        str(df.iloc[i, j]),
                        pos=LEADERBOARD_POS,
                        x_offset=LEADERBOARD_COL_WIDTH*j + supp_col_offset,
                        y_offset=LEADERBOARD_ROW_HEIGHT*(i+1),
                        font_size=30
                        )
                )

    def new_record(self, score, level, lines, APM, time, name=os.getlogin()):
        new_record(score, level, lines, APM, time, name)
        self.update_leaderboard()

    def update_leaderboard(self):
        self.__init__()

