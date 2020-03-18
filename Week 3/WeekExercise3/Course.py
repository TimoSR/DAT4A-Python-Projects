class Course:

    def __init__(self, name, classroom, teacher, ects, course_taken: bool, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ects = ects

        if course_taken:
            self.grade = grade
        else:
            self.grade = 0
