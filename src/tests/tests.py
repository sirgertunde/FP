import unittest

from src.repository.discipline_repository import DisciplineRepository, DisciplineRepositoryError
from src.repository.student_repository import StudentRepository, StudentRepositoryError
from src.services.discipline_service import DisciplineService
from src.services.student_service import StudentService


class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.student_repository = StudentRepository()
        self.student_service = StudentService(self.student_repository)

    def test_add_student(self):
        self.student_service.add(student_id="1", name="Andrei")
        self.assertEqual(len(self.student_repository), 1)
        with self.assertRaises(StudentRepositoryError):
            self.student_service.add(student_id="1", name="Andrei")

    def test_remove_student(self):
        self.student_service.add(student_id="1", name="Andrei")
        self.student_service.remove(student_id="1")
        self.assertEqual(len(self.student_repository), 0)
        with self.assertRaises(StudentRepositoryError):
            self.student_service.remove(student_id="2")

    def test_update_student(self):
        self.student_service.add(student_id="1", name="Andrei")
        self.student_service.update(student_id="1", name="Paul")
        updated_student = self.student_repository.get(student_id="1")
        self.assertEqual(updated_student.name, "Paul")
        with self.assertRaises(StudentRepositoryError):
            self.student_service.update(student_id="2", name="Paul")


class TestDisciplineManagement(unittest.TestCase):
    def setUp(self):
        self.discipline_repository = DisciplineRepository()
        self.discipline_service = DisciplineService(self.discipline_repository)

    def test_add_discipline(self):
        self.discipline_service.add(discipline_id="1", name="Math")
        self.assertEqual(len(self.discipline_repository), 1)
        with self.assertRaises(DisciplineRepositoryError):
            self.discipline_service.add(discipline_id="1", name="Physics")

    def test_remove_discipline(self):
        self.discipline_service.add(discipline_id="1", name="Math")
        self.discipline_service.remove(discipline_id="1")
        self.assertEqual(len(self.discipline_repository), 0)
        with self.assertRaises(DisciplineRepositoryError):
            self.discipline_service.remove(discipline_id="2")

    def test_update_discipline(self):
        self.discipline_service.add(discipline_id="1", name="Math")
        self.discipline_service.update(discipline_id="1", name="Physics")
        updated_discipline = self.discipline_repository.get(discipline_id="1")
        self.assertEqual(updated_discipline.name, "Physics")
        with self.assertRaises(DisciplineRepositoryError):
            self.discipline_service.update(discipline_id="2", name="Chemistry")

    def test_list_disciplines(self):
        self.discipline_service.add(discipline_id="1", name="Math")
        self.discipline_service.add(discipline_id="2", name="Physics")
        disciplines = self.discipline_service.get_all()
        self.assertEqual(len(disciplines), 2)


if __name__ == '__main__':
    unittest.main()
