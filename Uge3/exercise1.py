
import random
from os.path import isfile, join
import os
import csv
from statistics import mean


class Student():
    """A student Class"""

    def __init__(self,  name, gender, data_sheet, image_url):
        """Initialize Student with name, gender, data_sheet and image_url"""
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender,
                                            self.data_sheet, self.image_url)

    def __str__(self):
        return '{name} is {gender} has {data_sheet} and looks like {image_url}.'.format(
            name=self.name, gender=self.gender, data_sheet=self.data_sheet, image_url=self.image_url)

    def get_avg_grade(self):
        """Student - get_avg_grade"""
        list_of_grades= self.data_sheet.get_grades_as_list()
        mean_value = mean(list_of_grades)
        return mean_value


class DataSheet():
    """ DataSheet """

    def __init__(self, courses):
        """Initialize Datasheet with courses"""
        self.courses = courses

    def __repr__(self):
        return 'DataSheet(%r)' % (self.courses)

    def __str__(self):
        return 'DataSheet: courses are {courses}'.format(
            courses=self.courses)

    def get_grades_as_list(self):
        """DataSheet - get_grades_as_list"""
        grades = []
        for grade in self.courses:
            grades.append(int(grade.optional_grade))
        return grades


class Course():
    """Course"""

    def __init__(self, name, classroom, teacher, ETCS, optional_grade=0):
        """Initialize Course with name, classroom, teacher, ETCS and optional grade if course is taken"""
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.optional_grade = optional_grade

    def __repr__(self):
        return 'Course(%r, %r, %r, %r, %r)' % (self.name, self.classroom,
                                               self.teacher, self.ETCS, self.optional_grade)

    def __str__(self):
        return '{name} is in {classroom} has {teacher} which gives {ETCS} and can give optionally {optional_grade}.'.format(
            name=self.name, classroom=self.classroom, teacher=self.teacher, ETCS=self.ETCS, optional_grade=self.optional_grade)


def generate_students(n):
    """ Generate n numbers of students """

    names = ["Borneo", "Gentri", "Jethro", "Morpheus"]
    teachers = ["Hans Jørgensen", "Jens Hansen", "Hans Jensen"]
    courses_list = ["Dansk", "Engelsk", "Matematik"]
    class_rooms = range(1, 20)
    urlLibs = ["1.jpg", "2.jpg", "3.jpg"]
    gender = ["male", "female"]
    grades = [4, 7, 10, 12]

    students = []
    for i in range(n):
        # print("i", i)
        # print("Students", students)
        courses = []
        courses.append(Course(random.choice(courses_list), random.choice(
            class_rooms), random.choice(teachers), 10, random.choice(grades)))
        courses.append(Course(random.choice(courses_list), random.choice(
            class_rooms), random.choice(teachers), 10, random.choice(grades)))
        courses.append(Course(random.choice(courses_list), random.choice(
            class_rooms), random.choice(teachers), 10, random.choice(grades)))
        data_sheet = DataSheet(courses)
        student = Student(random.choice(names)+str(i+1), random.choice(
            gender), data_sheet, random.choice(urlLibs))
        students.append(student)

    return students


def write_list_to_file(output_file, list):
    """can take a list of tuple and write each element to a new line in file"""

    with open(output_file, "w") as output:
        student_writer = csv.writer(
            output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        student_writer.writerow(
            ["stud_name", "course_name", "teacher", "ects", "classroom", "grade", "img_url"])
        for el in list:
            # print("el", el)
            for c in el.data_sheet.courses:
                student_writer.writerow(
                    [el.name, c.name, c.teacher, c.ETCS, c.classroom, c.optional_grade, el.image_url])


def read_students_into_list():
    with open("students.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        old_name = ""
        courses = []
        students = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                stud_name = row[]
                course_name = row[1]
                teacher = row[2]
                ects = row[3]
                classroom = row[4]
                grade = row[5]
                url_lib = row[6]
                gender = ""
                if stud_name != old_name:
                    courses = []
                    courses.append(Course(course_name, classroom, teacher, ects, grade))
                else:
                    courses.append(Course(course_name, classroom, teacher, ects, grade))

                data_sheet = DataSheet(courses)
                student = Student(stud_name, gender, data_sheet, url_lib)
                students.append(student)

                line_count +=   1

        return students


def exercise_1():
    studs = generate_students(22)

    # 7a
    write_list_to_file("students.csv", studs)

    # 8
    # student_list = read_students_into_list()
    student_list =read_students_into_list()
    print(student_list)
    for student in student_list:
        print("Student {name}, Image: {img_url}, average grade: {av_grade}".format(name=student.name, img_url=student.image_url, av_grade=student.get_avg_grade()))


exercise_1()
