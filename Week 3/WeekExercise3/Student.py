from WeekExercise3 import DataSheet


class Student:

    def __init__(self, name, gender, data_sheet: DataSheet):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
