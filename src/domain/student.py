class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, new_student_id):
        self.__student_id = new_student_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return str(self.student_id) + " " + self.name

    def __repr__(self):
        return str(self.student_id) + " " + self.name
