from service import Service


class UI:
    def __init__(self):
        self.service = Service()
        self.board = self.service.repo.board

    def run(self):
        print(self.service.repo.board)
        cmd = input(">")
        cmd = cmd.split(" ", 1)
        while True:
            if cmd[0] == "exit":
                break
            if cmd[0] == "tick":
                if len(cmd) == 1:
                    try:
                        self.service.tick('1')
                    except ValueError as ve:
                        print(ve)
                else:
                    try:
                        self.service.tick(cmd[1])
                    except ValueError as ve:
                        print(ve)
            elif cmd[0] == "save":
                self.service.repo.save_board(cmd[1])
            elif cmd[0] == "load":
                self.service.repo.load_board(cmd[1])
            elif cmd[0] == "place":
                try:
                    self.service.place(cmd[1])
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)
            else:
                print("Wrong command")
            print(self.service.repo.board)
            cmd = input(">")
            cmd = cmd.split(" ", 1)
