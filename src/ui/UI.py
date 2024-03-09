from src.repository.discipline_repository import DisciplineRepositoryError
from src.repository.grade_repository import GradeRepositoryError
from src.repository.student_repository import StudentRepositoryError


class UI:
    def __init__(self, student_service, discipline_service, grade_service):
        self.__student_service = student_service
        self.__discipline_service = discipline_service
        self.__grade_service = grade_service

    def print_menu(self):
        print("as to add student")
        print("ad to add discipline")
        print("rs to remove student")
        print("rd to remove discipline")
        print("us to update student")
        print("ud to update discipline")
        print("ls to list students")
        print("ld to list disciplines")
        print("lg to list grades")
        print("gs to grade student")
        print("ss to search for students")
        print("sd to search for disciplines")
        print("f for students failing at 1 ore more disciplines")
        print("b for students with best school situation in descending order of their aggregated average")
        print("d for disciplines sorted in descending order of the average grades")
        print("x to exit")

    def add_student(self, student_id, student_name):
        try:
            self.__student_service.add(student_id, student_name)
        except StudentRepositoryError as e:
            print(e)

    def add_discipline(self, discipline_id, discipline_name):
        try:
            self.__discipline_service.add(discipline_id, discipline_name)
        except DisciplineRepositoryError as e:
            print(e)

    def add_grade(self, did, sid, value):
        try:
            self.__grade_service.add(did, sid, value)
        except GradeRepositoryError as e:
            print(e)

    def list_students(self):
        print(self.__student_service.get_all())

    def list_disciplines(self):
        print(self.__discipline_service.get_all())

    def list_grades(self):
        print(self.__grade_service.get_all())

    def remove_student(self, student_id):
        try:
            self.__student_service.remove(student_id)
            self.__grade_service.delete_grades_with_student(student_id)
        except StudentRepositoryError as e:
            print(e)

    def remove_discipline(self, discipline_id):
        try:
            self.__discipline_service.remove(discipline_id)
            self.__grade_service.delete_grades_with_discipline(discipline_id)
        except DisciplineRepositoryError as e:
            print(e)

    def update_student(self, student_id, name):
        try:
            self.__student_service.update(student_id, name)
        except StudentRepositoryError as e:
            print(e)

    def update_discipline(self, discipline_id, name):
        try:
            self.__discipline_service.update(discipline_id, name)
        except DisciplineRepositoryError as e:
            print(e)

    def search_student(self, query):
        return self.__student_service.search(query)

    def search_discipline(self, query):
        return self.__discipline_service.search(query)

    def get_failing_students(self):
        return self.__grade_service.get_failing_students()

    def get_students_best_school_situation(self):
        return self.__grade_service.get_students_best_school_situation()

    def get_disciplines_sorted_by_average_grade(self):
        return self.__grade_service.get_disciplines_sorted_by_average_grade()

    def run(self):
        self.__student_service.add20_students()
        self.__discipline_service.add20_disciplines()
        self.__grade_service.add20_grades()
        finish = False
        while not finish:
            self.print_menu()
            option = input(">")
            if option == "x":
                finish = True
            elif option == "as":
                student_id = int(input("Give student id: "))
                student_name = input("Give student name: ")
                self.add_student(student_id, student_name)
            elif option == "ad":
                discipline_id = int(input("Give discipline id: "))
                discipline_name = input("Give discipline name: ")
                self.add_discipline(discipline_id, discipline_name)
            elif option == "ls":
                self.list_students()
            elif option == "ld":
                self.list_disciplines()
            elif option == "lg":
                self.list_grades()
            elif option == "rs":
                student_id = int(input("Give student id: "))
                self.remove_student(student_id)
            elif option == "rd":
                discipline_id = int(input("Give discipline id: "))
                self.remove_discipline(discipline_id)
            elif option == "us":
                student_id = int(input("Give student id: "))
                student_name = input("Give new student name: ")
                self.update_student(student_id, student_name)
            elif option == "ud":
                discipline_id = int(input("Give discipline id: "))
                discipline_name = input("Give new discipline name: ")
                self.update_discipline(discipline_id, discipline_name)
            elif option == "gs":
                discipline_id = int(input("Give discipline id: "))
                student_id = int(input("Give student id: "))
                grade_value = int(input("Give the value of the grade: "))
                self.add_grade(discipline_id, student_id, grade_value)
            elif option == "ss":
                query = input("Search for a student: ")
                print(self.search_student(query))
            elif option == "sd":
                query = input("Search for a discipline: ")
                print(self.search_discipline(query))
            elif option == "f":
                print(self.get_failing_students())
            elif option == "b":
                print(self.get_students_best_school_situation())
            elif option == "d":
                print(self.get_disciplines_sorted_by_average_grade())
            else:
                print("Invalid option")
