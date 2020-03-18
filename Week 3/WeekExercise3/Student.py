from WeekExercise3 import DataSheet


class Student:

    # 2(a). A student has a data_sheet
    # 4. In Student create init() so that a Student can be initiated with name, gender, data_sheet and image_url

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    # 6. In student create a method: get_avg_grade()

    def get_avg_grade(self):

        average_grade = sum(self.data_sheet.get_grades_as_list()) / len(self.data_sheet.get_grades_as_list())

        return average_grade

    # 9. Make a method on Student class that can show progression of the study in % (add up ECTS from all passed
    # courses divided by total of 150 total points (equivalent to 5 semesters))

    def get_progression(self):
        ects = 0
        for course in self.data_sheet.courses:
            if course.grade > 0:
                ects += course.ects
        return (ects / 150) * 100

    def get_courses(self):
        return self.data_sheet.courses

