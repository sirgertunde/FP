import random

from src.domain.discipline import Discipline


class DisciplineService:
    def __init__(self, discipline_repository):
        self._discipline_repository = discipline_repository

    def get(self, discipline_id):
        return self._discipline_repository.get(discipline_id)

    def get_all(self):
        return self._discipline_repository.get_all()

    def add(self, discipline_id, name):
        new_discipline = Discipline(discipline_id, name)
        self._discipline_repository.add(new_discipline)

    def remove(self, discipline_id):
        self._discipline_repository.remove(discipline_id)

    def update(self, discipline_id, name):
        self._discipline_repository.update(discipline_id, name)

    def add20_disciplines(self):
        names = ["Computer Science", "Math", "Romanian", "English", "Physics", "Chemistry", "Biology", "History", "Geography"]
        for i in range(1, 21):
            name = random.choice(names)
            discipline = Discipline(i, name)
            self._discipline_repository.add(discipline)

    def search(self, query):
        return self._discipline_repository.search(query)
