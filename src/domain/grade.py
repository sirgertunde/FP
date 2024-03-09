class Grade:
    def __init__(self, discipline_id: int, student_id: int, grade_value: int):
        self.__grade_value = grade_value
        self.__discipline_id = discipline_id
        self.__student_id = student_id

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, new_student_id):
        self.__student_id = new_student_id

    @property
    def discipline_id(self):
        return self.__discipline_id

    @discipline_id.setter
    def discipline_id(self, new_discipline_id):
        self.__discipline_id = new_discipline_id

    @property
    def grade_value(self):
        return self.__grade_value

    @grade_value.setter
    def grade_value(self, new_grade_value):
        self.__grade_value = new_grade_value

    def __str__(self):
        return str(self.__discipline_id) + " " + str(self.student_id) + " " + str(self.__grade_value)

    def __repr__(self):
        return str(self.__discipline_id) + " " + str(self.student_id) + " " + str(self.__grade_value)
