from WeekExercise3 import Course


class DataSheet:

    # 2(b). A data_sheet has multiple courses in particular order

    def __init__(self, courses):
        self.courses = courses

    # 5. In DataSheet create a method to get_grades_as_list()

    def get_grades_as_list(self):
        grades_as_list = []
        for course in self.courses:
            if course.grade is not None:
                grades_as_list.append(course.grade)
        return grades_as_list
