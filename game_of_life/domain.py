from texttable import Texttable


class Board:
    def __init__(self):
        self.board = [[" ", " ", " ", " ", " ", " ", " ", " "]for _ in range(8)]

    def __str__(self):
        self.table = Texttable()
        self.table.add_rows(self.board, [])
        return self.table.draw()

