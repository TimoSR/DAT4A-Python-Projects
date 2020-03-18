from WeekExercise3 import Course


class DataSheet:

    def __init__(self, courses: Course = []):
        self.courses = courses

    def get_grades_as_list(self):