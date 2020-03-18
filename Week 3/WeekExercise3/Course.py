class Course:

    # Each course has name, classroom, teacher, ETCS and optional grade if course is taken.

    def __init__(self, name, classroom, teacher, ects, grade=0):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ects = int(ects)
        self.grade = grade
