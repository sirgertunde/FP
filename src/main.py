from src.repository.discipline_repository import DisciplineRepository
from src.repository.grade_repository import GradeRepository
from src.repository.student_repository import StudentRepository
from src.services.discipline_service import DisciplineService
from src.services.grade_service import GradeService
from src.services.student_service import StudentService
from src.ui.UI import UI

if __name__ == "__main__":
    student_repository = StudentRepository()
    discipline_repository = DisciplineRepository()
    grade_repository = GradeRepository()
    student_service = StudentService(student_repository)
    discipline_service = DisciplineService(discipline_repository)
    grade_service = GradeService(grade_repository, student_repository, discipline_repository)
    console = UI(student_service, discipline_service, grade_service)
    console.run()
