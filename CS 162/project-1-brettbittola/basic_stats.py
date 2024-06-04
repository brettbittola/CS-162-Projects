# Author: Brett Bittola
# GitHub username: brettbittola
# Date: 9/28/2023
# Description: Creates a Student class and finds the mean, median and mode of grades
#              using an imported statistics module.

from statistics import mean, median, mode
class Student:
    """Represents a student with a name and grade"""
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        """Returns the student's grade"""
        return self._grade

def basic_stats(student_list):
    """Creates a list of grades from the Student class and returns the mean, median and mode"""
    grades = [student.get_grade() for student in student_list]
    return mean(grades), median(grades), mode(grades)
