from src.domain.discipline import Discipline


class DisciplineRepositoryError(Exception):
    def __init__(self, msg):
        self._msg = msg


class DisciplineRepository:
    def __init__(self):
        self._disciplines = {}

    def add(self, discipline):
        """
        :param discipline: an object of type Discipline
        :return: nothing
        Adds a new discipline if its id does not already exist
        """
        if discipline.discipline_id in self._disciplines.keys():
            raise DisciplineRepositoryError("Discipline already exists")
        self._disciplines[discipline.discipline_id] = discipline

    def remove(self, discipline_id):
        """
        :param discipline_id: int, the id of a discipline
        :return: nothing
        Removes a discipline by id, if it exists
        """
        if discipline_id in self._disciplines.keys():
            del self._disciplines[discipline_id]
        else:
            raise DisciplineRepositoryError("Discipline does not exist")

    def update(self, discipline_id, name):
        """
        :param discipline_id: int, the id of a discipline
        :param name: string, the name of a discipline
        :return: nothing
        Updates the name of a discipline
        """
        new_discipline = Discipline(discipline_id, name)
        if discipline_id in self._disciplines.keys():
            self._disciplines[discipline_id] = new_discipline
        else:
            raise DisciplineRepositoryError("Discipline does not exist")

    def get_all(self):
        """
        :return: all the disciplines
        """
        return list(self._disciplines.values())

    def search(self, query):
        results = []
        query = query.lower()
        for id, discipline in self._disciplines.items():
            if query in str(id) or query in discipline.name.lower():
                results.append(discipline.name)
        return results

    def get(self, discipline_id):
        try:
            return self._disciplines[discipline_id]
        except KeyError:
            raise DisciplineRepositoryError("Discipline does not exist")

    def __len__(self):
        return len(self._disciplines)
