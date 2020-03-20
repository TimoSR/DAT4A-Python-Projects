class Course:

    # 3. Each course has name, classroom, teacher, ETCS and optional grade if course is taken.

    def __init__(self, course_name, classroom, teacher, ECTS, grade=0):
        self.name = course_name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = int(grade)
