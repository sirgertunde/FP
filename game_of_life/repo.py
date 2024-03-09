from domain import Board


class Repository:
    def __init__(self, file_name="patterns.txt"):
        self.board = Board()
        self.file_name = file_name
        self.patterns = self.load_patterns(self.file_name)

    def load_patterns(self, file_name):
        patterns = []
        with open(file_name, "r") as patterns_file:
            lines = patterns_file.readlines()
            newlines = []
            for line in lines:
                newlines.append(line.strip())
            lines = newlines
            for index in range(len(lines)):
                if lines[index] == "block":
                    block_data = []
                    line = [lines[index + 1][0], lines[index + 1][1]]
                    block_data.append(line)
                    line = [lines[index + 2][0], lines[index + 2][1]]
                    block_data.append(line)
                    patterns.append("block")
                    patterns.append(block_data)
                if lines[index] == "tub":
                    tub_data = []
                    line = [lines[index + 1][0], lines[index + 1][1], lines[index + 1][2]]
                    tub_data.append(line)
                    line = [lines[index + 2][0], lines[index + 2][1], lines[index + 2][2]]
                    tub_data.append(line)
                    line = [lines[index + 3][0], lines[index + 3][1], lines[index + 3][2]]
                    tub_data.append(line)
                    patterns.append("tub")
                    patterns.append(tub_data)
                if lines[index] == "blinker":
                    blinker_data = []
                    line = [lines[index + 1][0], lines[index + 1][1], lines[index + 1][2]]
                    blinker_data.append(line)
                    line = [lines[index + 2][0], lines[index + 2][1], lines[index + 2][2]]
                    blinker_data.append(line)
                    line = [lines[index + 3][0], lines[index + 3][1], lines[index + 3][2]]
                    blinker_data.append(line)
                    patterns.append("blinker")
                    patterns.append(blinker_data)
                if lines[index] == "beacon":
                    beacon_data = []
                    line = [lines[index + 1][0], lines[index + 1][1], lines[index + 1][2], lines[index + 1][3]]
                    beacon_data.append(line)
                    line = [lines[index + 2][0], lines[index + 2][1], lines[index + 2][2], lines[index + 2][3]]
                    beacon_data.append(line)
                    line = [lines[index + 3][0], lines[index + 3][1], lines[index + 3][2], lines[index + 3][3]]
                    beacon_data.append(line)
                    line = [lines[index + 4][0], lines[index + 4][1], lines[index + 4][2], lines[index + 4][3]]
                    beacon_data.append(line)
                    patterns.append("beacon")
                    patterns.append(beacon_data)
                if lines[index] == "spaceship":
                    spaceship_data = []
                    line = [lines[index + 1][0], lines[index + 1][1], lines[index + 1][2], lines[index + 1][3]]
                    spaceship_data.append(line)
                    line = [lines[index + 2][0], lines[index + 2][1], lines[index + 2][2], lines[index + 2][3]]
                    spaceship_data.append(line)
                    line = [lines[index + 3][0], lines[index + 3][1], lines[index + 3][2], lines[index + 3][3]]
                    spaceship_data.append(line)
                    line = [lines[index + 4][0], lines[index + 4][1], lines[index + 4][2], lines[index + 4][3]]
                    spaceship_data.append(line)
                    patterns.append("spaceship")
                    patterns.append(spaceship_data)
        patterns_file.close()
        return patterns

    def load_board(self, file_name):
        with open(file_name, 'r') as board_file:
            lines = board_file.readlines()
            i = 0
            for line in lines:
                for j in range(8):
                    if line[j] == "-":
                        self.board.board[i][j] = " "
                    elif line[j] == "X":
                        self.board.board[i][j] = "X"
                i = i + 1
        board_file.close()

    def save_board(self, file_name):
        with open(file_name, "w") as board_file:
            for line in self.board.board:
                for element in line:
                    if element == " ":
                        board_file.write("-")
                    else:
                        board_file.write(element)
                board_file.write("\n")
        board_file.close()
