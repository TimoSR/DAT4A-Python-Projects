from WeekExercise3 import DataSheet


class Student:

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):

        average_grade = sum(self.data_sheet.get_grades_as_list()) / len(self.data_sheet.get_grades_as_list())

        return average_grade

    def get_progression(self):
        ects = 0
        for course in self.data_sheet.courses:
            if course.grade > 0:
                ects += course.ETCs
        return (ects / 150) * 100

    def get_courses(self):
        return self.data_sheet.courses

