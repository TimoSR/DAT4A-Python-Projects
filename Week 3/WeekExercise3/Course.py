class Course:

    def __init__(self, name, classroom, teacher, ects, grade=0):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCs = int(ects)
        self.grade = grade
