class Student:
    def __init__(self, id, name, courses=None):
        self.id = id
        self.name = name

        if courses is None:
            self.courses = []
        else:
            self.courses = courses


class Course:
    def __init__(self, id, name,code, quizzes=None,tmas = None,exams = None,assignments = None):
        self.id = id
        self.name = name
        self.code = code

        if quizzes is None:
            self.quizzes = []
        else:
            self.quizzes = quizzes

        if tmas is None:
            self.tmas = []
        else:
            self.tmas = tmas

        if exams is None:
            self.exams = []
        else:
            self.exams = exams

        if assignments is None:
            self.assignments = []
        else:
            self.assignments = assignments        


class Quiz:
    def __init__(self,id,title,date):
        self.id = id
        self.title = title
        self.date = date


class Exam:
    def __init__(self,id,title,date):
        self.id = id
        self.title = title
        self.date = date
    
        
            
class Tma:
    def __init__(self,id,title,date):
        self.id = id
        self.title = title
        self.date = date
         
        


class Assignment:
    def __init__(self,id,title,date):
        self.id = id
        self.title = title
        self.date = date
        

                