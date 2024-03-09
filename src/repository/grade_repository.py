class GradeRepositoryError(Exception):
    def __init__(self, msg):
        self._msg = msg


class GradeRepository:
    def __init__(self):
        self._grades = []

    def add(self, grade):
        """
        :param grade: an object of type Grade
        :return: nothing
        Adds a grade to the repository
        """
        self._grades.append(grade)

    def remove(self, grade):
        """
        :param grade: an object of type Grade
        :return: nothing
        Removes a grade from the repository
        """
        self._grades.remove(grade)

    def get_all(self):
        """
        :return: all the grades
        """
        return self._grades

    def get_student_grades(self, student_id):
        return [grade for grade in self._grades if grade.student_id == student_id]

    def get_grades_by_discipline(self, discipline_id):
        return [grade for grade in self._grades if grade.discipline_id == discipline_id]
