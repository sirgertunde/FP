import random

from src.domain.student import Student


class StudentService:
    def __init__(self, student_repository):
        self._student_repository = student_repository

    def get(self, student_id):
        return self._student_repository.get(student_id)

    def get_all(self):
        return self._student_repository.get_all()

    def add(self, student_id, name):
        new_student = Student(student_id, name)
        self._student_repository.add(new_student)

    def update(self, student_id, name):
        self._student_repository.update(student_id, name)

    def remove(self, student_id):
        self._student_repository.remove(student_id)

    def add20_students(self):
        names = ["Andrei", "Carina", "Marius", "Tudor", "Daria", "Sara", "Radu", "Oana", "Miruna", "Paul", "Iulia", "Bianca"]
        for i in range(1, 21):
            name = random.choice(names)
            student = Student(i, name)
            self._student_repository.add(student)

    def search(self, query):
        return self._student_repository.search(query)
