from utils.models import Student,Course,Quiz,Exam,Tma,Assignment
from services.mock_data import fake_students

def fetch_student(student_id):
    
    student_data = fake_students.get(student_id)
    if student_data is None:
        return None

    return build_student(student_data)




def build_student(student_data):
    course_objects = []
    

    for course_data in student_data.get("courses")or[]:
        quiz_objects = []
        for quiz_data in course_data.get("quizzes")or[]:
            quiz = Quiz(
              id=  quiz_data["id"],
               title= quiz_data["title"],
               date= quiz_data["date"]
            )
            quiz_objects.append(quiz)

        exam_objects = []
        for exam_data in course_data.get("exams")or[]:
            exam = Exam(
               id= exam_data["id"],
               title= exam_data["title"],
               date= exam_data["date"]
            )    
            exam_objects.append(exam)

        tma_objects = []
        for tma_data in course_data.get("tmas")or []:
            tma = Tma(
               id= tma_data["id"],
                title=tma_data["title"],
                date=tma_data["date"]
            )
            tma_objects.append(tma)


        assignments_objects = []
        for assignments_data in course_data.get("assignments")or[]:
            assignment = Assignment(
               id= assignments_data["id"],
               title= assignments_data["title"],
               date= assignments_data["date"]
            )
            assignments_objects.append(assignment)            

        course = Course(
        id= course_data["id"],
        name = course_data["name"],
        code = course_data["code"],
        quizzes = quiz_objects,
        tmas = tma_objects,
        exams = exam_objects,
         assignments = assignments_objects
        )
        course_objects.append(course)    

    student = Student(
        id = student_data["id"],
        name=student_data["name"],
        courses= course_objects
)
    return student
    