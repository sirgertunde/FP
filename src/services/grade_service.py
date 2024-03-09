import random

from src.domain.grade import Grade
from src.repository.grade_repository import GradeRepositoryError


class GradeService:
    def __init__(self, grade_repository, student_repository, discipline_repository):
        self._grade_repository = grade_repository
        self._student_repository = student_repository
        self._discipline_repository = discipline_repository

    def get(self, grade_id):
        return self._grade_repository.get(grade_id)

    def get_all(self):
        return self._grade_repository.get_all()

    def add20_grades(self):
        for i in range(1, 21):
            sid = random.randint(1, 20)
            did = random.randint(1, 20)
            value = random.randint(1, 10)
            grade = Grade(did, sid, value)
            self._grade_repository.add(grade)

    def add(self, did, sid, value):
        exists_discipline = False
        exists_student = False
        for discipline in self._discipline_repository.get_all():
            if discipline.discipline_id == did:
                exists_discipline = True
        for student in self._student_repository.get_all():
            if student.student_id == sid:
                exists_student = True
        if exists_discipline and exists_student:
            grade = Grade(did, sid, value)
            self._grade_repository.add(grade)
        else:
            raise GradeRepositoryError("The student and discipline must exist in order to add grade")

    def delete_grades_with_discipline(self, did):
        for grade in self.get_all():
            if grade.discipline_id == did:
                self._grade_repository.remove(grade)

    def delete_grades_with_student(self, sid):
        for grade in self.get_all():
            if grade.student_id == sid:
                self._grade_repository.remove(grade)

    def get_failing_students(self):
        failing_students = []
        all_students = self._student_repository.get_all()
        all_disciplines = self._discipline_repository.get_all()
        for student in all_students:
            student_grades = self._grade_repository.get_student_grades(student.student_id)
            for discipline in all_disciplines:
                discipline_grades = [grade for grade in student_grades if grade.discipline_id == discipline.discipline_id]
                if discipline_grades:
                    average_grade = sum([grade.grade_value for grade in discipline_grades]) / len(discipline_grades)
                    if average_grade < 5:
                        failing_students.append(student)
                        break
        return failing_students

    def get_students_best_school_situation(self):
        all_students = self._student_repository.get_all()
        students_with_aggregated_average = []
        for student in all_students:
            student_grades = self._grade_repository.get_student_grades(student.student_id)
            if student_grades:
                average_grades = sum(grade.grade_value for grade in student_grades) / len(student_grades)
                students_with_aggregated_average.append((student, average_grades))
        sorted_students = sorted(students_with_aggregated_average, key=lambda x: x[1], reverse=True)
        return [student[0] for student in sorted_students]

    def get_discipline_grades(self, discipline_id):
        return self._grade_repository.get_grades_by_discipline(discipline_id)

    def get_disciplines_sorted_by_average_grade(self):
        all_disciplines = self._discipline_repository.get_all()
        disciplines_with_average_grade = []
        for discipline in all_disciplines:
            discipline_grades = self.get_discipline_grades(discipline.discipline_id)
            if discipline_grades:
                average_grade = sum(grade.grade_value for grade in discipline_grades) / len(discipline_grades)
                disciplines_with_average_grade.append((discipline, average_grade))
        sorted_disciplines = sorted(disciplines_with_average_grade, key=lambda x: x[1], reverse=True)
        return [discipline[0] for discipline in sorted_disciplines]
