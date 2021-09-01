class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectures(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def avg_grade(self):
        my_list = []
        for grade in self.grades.values():
            for mark in grade:
                my_list.append(mark)
        avg = sum(my_list) / len(my_list)
        return avg

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.avg_grade() < other.avg_grade()

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grade()} \nКурсы в процессе изучения: {",".join(self.courses_in_progress)} \nЗавершенные курсы: {",".join(self.finished_courses)} '
        return res
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}
    def lec_avg_grade(self):
        my_list = []
        for grade in self.grades.values():
            for mark in grade:
                my_list.append(mark)
        lec_avg = sum(my_list) / len(my_list)
        return lec_avg
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.lec_avg_grade()} '
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.lec_avg_grade() < other.lec_avg_grade()


class Reviewer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

bad_student = Student('Ron', 'Nel', 'gender')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Git']

worst_student = Student('Harry', 'Potter', 'gender')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Git']

students = [bad_student, worst_student]

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

one_reviewer = Reviewer('One', 'Rew')
one_reviewer.courses_attached += ['Python']
one_reviewer.courses_attached += ['Git']

viewer = Reviewer('Tim', 'B')
viewer.courses_attached += ['Python']
viewer.courses_attached += ['Git']

one_reviewer.rate_hw(best_student, 'Python', 10)
one_reviewer.rate_hw(best_student, 'Python', 10)
one_reviewer.rate_hw(best_student, 'Python', 10)
one_reviewer.rate_hw(best_student, 'Python', 10)
one_reviewer.rate_hw(best_student, 'Git', 10)
one_reviewer.rate_hw(best_student, 'Python', 10)
one_reviewer.rate_hw(best_student, 'Python', 10)
one_reviewer.rate_hw(best_student, 'Python', 10)
one_reviewer.rate_hw(best_student, 'Git', 10)
one_reviewer.rate_hw(best_student, 'Git', 9)

some_reviewer.rate_hw(bad_student, 'Python', 5)
some_reviewer.rate_hw(bad_student, 'Python', 5)
one_reviewer.rate_hw(bad_student, 'Python', 6)
some_reviewer.rate_hw(bad_student, 'Git', 3)

viewer.rate_hw(worst_student, 'Git', 1)
viewer.rate_hw(worst_student, 'Python', 2)
viewer.rate_hw(bad_student, 'Git', 5)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

one_lecturer = Lecturer('One', 'Guy')
one_lecturer.courses_attached += ['Python']
one_lecturer.courses_attached += ['Git']

lec = Lecturer('Second', 'Guy')
lec.courses_attached += ['Python']
lec.courses_attached += ['Git']

lecturers = [lec, one_lecturer]

cool_student = Student('Some', 'Buddy', 'your_gender')
cool_student.courses_in_progress += ['Python']
cool_student.courses_in_progress += ['Git']

cool_student.rate_lectures(some_lecturer, 'Python', 10)
cool_student.rate_lectures(some_lecturer, 'Python', 10)
cool_student.rate_lectures(some_lecturer, 'Python', 10)
cool_student.rate_lectures(some_lecturer, 'Python', 10)
cool_student.rate_lectures(some_lecturer, 'Git', 10)
cool_student.rate_lectures(some_lecturer, 'Python', 10)
cool_student.rate_lectures(some_lecturer, 'Python', 10)
cool_student.rate_lectures(some_lecturer, 'Python', 10)
cool_student.rate_lectures(some_lecturer, 'Git', 10)
cool_student.rate_lectures(some_lecturer, 'Git', 9)

cool_student.rate_lectures(one_lecturer, 'Python', 7)
cool_student.rate_lectures(one_lecturer, 'Git', 4)

cool_student.rate_lectures(lec, 'Python', 7)
cool_student.rate_lectures(lec, 'Git', 8)
cool_student.rate_lectures(lec, 'Git', 9)

# print(some_reviewer)
# print(best_student)
# print(some_lecturer)
# print(bad_student)
# print(worst_student)
# print(best_student < worst_student)
# print(lec < some_lecturer)



def avg_grade_kurs(students, course):
    mylist = []
    for student in students:
        if student.grades.get(course) != None:
            for kurs in student.grades.get(course):
                mylist.append(kurs)
        else:
            pass
    avg_grade_kurs = sum(mylist) / len(mylist)
    return avg_grade_kurs


avg_grade_kurs = avg_grade_kurs(students, course='Git')
print(f'Средняя оценка по домашнему заданиюпо всем студентам курса "Git" = {avg_grade_kurs}')

def lec_avg_grade_kurs(lecturers, course):
    mylist = []
    for lecturer in lecturers:
        if lecturer.grades.get(course) != None:
            for kurs in lecturer.grades.get(course):
                mylist.append(kurs)
        else:
            pass
    lec_avg_grade_kurs = sum(mylist) / len(mylist)
    return lec_avg_grade_kurs


lec_avg_grade_kurs = lec_avg_grade_kurs(lecturers, course='Git')
print(f'Средняя оценка за лекции всех лекторов в рамках курса "Git" = {lec_avg_grade_kurs}')