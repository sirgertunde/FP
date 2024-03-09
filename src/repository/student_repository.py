from src.domain.student import Student


class StudentRepositoryError(Exception):
    def __init__(self, msg):
        self._msg = msg


class StudentRepository:
    def __init__(self):
        self._students = {}

    def add(self, new_student: Student):
        """
        :param new_student: an object of type Student
        :return: nothing
        Adds a student if its id does not already exist
        """
        if new_student.student_id in self._students.keys():
            raise StudentRepositoryError("Student already exists")
        self._students[new_student.student_id] = new_student

    def remove(self, student_id):
        """
        :param student_id: int, the id of a student
        :return: nothing
        Removes a student, if its id exists
        """
        if student_id in self._students.keys():
            del self._students[student_id]
        else:
            raise StudentRepositoryError("Student does not exist")

    def update(self, student_id, name):
        """
        :param student_id: int, the id of a student
        :param name: string, the name of a student
        :return: nothing
        Updates the name of the student
        """
        new_student = Student(student_id, name)
        if student_id in self._students.keys():
            self._students[student_id] = new_student
        else:
            raise StudentRepositoryError("Student does not exist")

    def get(self, student_id: str):
        try:
            return self._students[student_id]
        except KeyError:
            raise StudentRepositoryError("Student does not exist")

    def search(self, query):
        results = []
        query = query.lower()
        for id, student in self._students.items():
            if query in str(id) or query in student.name.lower():
                results.append(student.name)
        return results

    def get_all(self):
        """
        :return: all the students
        """
        return list(self._students.values())

    def __len__(self):
        return len(self._students)
