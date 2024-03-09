from copy import deepcopy

from repo import Repository


class Service:
    def __init__(self):
        self.repo = Repository()

    def update_board(self):
        board = deepcopy(self.repo.board.board)
        for x in range(8):
            for y in range(8):
                count_alive = 0
                count_dead = 0
                if x >= 1 and y >= 1:
                    if board[x - 1][y - 1] == "X":
                        count_alive += 1
                    count_dead += 1
                if x >= 1:
                    if board[x - 1][y] == "X":
                        count_alive += 1
                    count_dead += 1
                if y >= 1:
                    if board[x][y - 1] == "X":
                        count_alive += 1
                    count_dead += 1
                if x < 7 and y < 7:
                    if board[x + 1][y + 1] == "X":
                        count_alive += 1
                    count_dead += 1
                if x < 7:
                    if board[x + 1][y] == "X":
                        count_alive += 1
                    count_dead += 1
                if y < 7:
                    if board[x][y + 1] == "X":
                        count_alive += 1
                    count_dead += 1
                if x >= 1 and y < 7:
                    if board[x - 1][y + 1] == "X":
                        count_alive += 1
                    count_dead += 1
                if x < 7 and y >= 1:
                    if board[x + 1][y - 1] == "X":
                        count_alive += 1
                    count_dead += 1
                if board[x][y] == "X":
                    if count_alive > 3 or count_alive < 2:
                        self.repo.board.board[x][y] = " "
                if board[x][y] == " ":
                    if count_alive == 3:
                        self.repo.board.board[x][y] = "X"

    def tick(self, parameter):
        for index in range(int(parameter)):
            self.update_board()

    def place(self, parameters):
        old_board = deepcopy(self.repo.board.board)
        patterns = self.repo.patterns
        params = parameters.split()
        if len(params) != 2:
            raise ValueError("The format of the command is invalid")
        if len(params[1]) != 3:
            raise ValueError("The format of the command is invalid")
        if params[1][1] != ",":
            raise ValueError("The format of the command is invalid")
        x = int(params[1][0])
        y = int(params[1][2])
        if x > 7 or y > 7:
            raise IndexError("Outside the board")
        if params[0] in patterns:
            for i in range(len(patterns)):
                if patterns[i] == params[0]:
                    for j in range(len(patterns[i+1])):
                        for k in range(len(patterns[i+1][j])):
                            if patterns[i+1][j][k] == "X":
                                if x+j > 7 or y+k > 7:
                                    self.repo.board.board = old_board
                                    raise IndexError("Outside the board")
                                if self.repo.board.board[x+j][y+k] == "X":
                                    self.repo.board.board = old_board
                                    raise ValueError("Live cells cannot overlap")
                                else:
                                    self.repo.board.board[x+j][y+k] = patterns[i+1][j][k]
                            if patterns[i+1][j][k] == "-":
                                if x+j > 7 or y+k > 7:
                                    self.repo.board.board = old_board
                                    raise IndexError("Outside the board")
                                if self.repo.board.board[x+j][y+k] == "X":
                                    self.repo.board.board = old_board
                                    raise ValueError("Live cells cannot overlap")
                                self.repo.board.board[x+j][y+k] = " "
        else:
            raise ValueError("Non-existent pattern")
