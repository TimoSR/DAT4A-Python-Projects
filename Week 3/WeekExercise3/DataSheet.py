from WeekExercise3 import Course


class DataSheet:

    def __init__(self, courses):
        self.courses = courses

    def get_grades_as_list(self):
        grades_as_list = []
        for course in self.courses:
            if course.grade is not None:
                grades_as_list.append(course.grade)
        return grades_as_list
