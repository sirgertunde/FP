class Discipline:
    def __init__(self, discipline_id: int, name: str):
        self.__discipline_id = discipline_id
        self.__name = name

    @property
    def discipline_id(self):
        return self.__discipline_id

    @discipline_id.setter
    def discipline_id(self, new_discipline_id):
        self.__discipline_id = new_discipline_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return str(self.discipline_id) + " " + self.name

    def __repr__(self):
        return str(self.discipline_id) + " " + self.name
