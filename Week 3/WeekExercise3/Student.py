from WeekExercise3 import DataSheet


class Student:

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):

        total_sum = sum(self.data_sheet.get_grades_as_list()) / len(self.data_sheet.get_grades_as_list())

        return total_sum
