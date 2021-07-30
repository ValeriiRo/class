import random


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def evaluation_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum_ratings = 0
        number_ratings = 0
        for list_ratings in lecturer.grades.values():
            for rating in list_ratings:
                sum_ratings += rating
                number_ratings += 1
        lecturer.average_rating = sum_ratings / number_ratings

    def __str__(self):

        object = f"Студент: \nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: " \
                 f"{self.average_rating}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
                 f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return object

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Character!')
            return
        return self.power < other.power

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = 0
        self.grades = {}

    def __str__(self):
        object = f'Лектор: \nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return object

class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum_ratings = 0
        number_ratings = 0
        for list_ratings in student.grades.values():
            for rating in list_ratings:
                sum_ratings += rating
                number_ratings += 1
        student.average_rating = sum_ratings / number_ratings

    def __str__(self):
        object = f'Проверяющий: \nИмя: {self.name}\nФамилия: {self.surname}'
        return object



Ruoy_Eman_student = Student('Ruoy', 'Eman', 'your_gender')
Ruoy_Eman_student.courses_in_progress += ['python', 'Git']
Ruoy_Eman_student.finished_courses += ['Введение в программирование']

Robert_Paulsen_student = Student('Robert', 'Paulsen', 'your_gender')
Robert_Paulsen_student.courses_in_progress += ['python', 'Git']
Robert_Paulsen_student.finished_courses += ['Введение в программирование']

Some_Buddy_Lecturer = Lecturer('Some', 'Buddy')
Some_Buddy_Lecturer.courses_attached += ['python']

Tailer_Durden_Lecturer = Lecturer('Tailer', 'Durden')
Tailer_Durden_Lecturer.courses_attached += ['Git']

Mike_Vazovsky_Reviewer = Reviewer('Mike', 'Vazovsky')
Mike_Vazovsky_Reviewer.courses_attached += ['Git']

Peter_Pedigree_Reviewer = Reviewer('Peter', 'Pedigree')
Peter_Pedigree_Reviewer.courses_attached += ['python']

for estimation in [10, 9, 10, 10, 10]:
    Mike_Vazovsky_Reviewer.rate_hw(Ruoy_Eman_student, 'Git', estimation)

for estimation in [10, 9, 9, 8, 9]:
    Mike_Vazovsky_Reviewer.rate_hw(Robert_Paulsen_student, 'Git', estimation)

for estimation in [10, 9, 10, 9, 10]:
    Peter_Pedigree_Reviewer.rate_hw(Ruoy_Eman_student, 'python', estimation)

for estimation in [10, 9, 10, 9, 10]:
    Peter_Pedigree_Reviewer.rate_hw(Robert_Paulsen_student, 'python', estimation)

for estimation in [10, 10, 10, 10, 10]:
    Ruoy_Eman_student.evaluation_lecture(Some_Buddy_Lecturer, 'python', estimation)

for estimation in [9, 9, 10, 10, 10]:
    Robert_Paulsen_student.evaluation_lecture(Some_Buddy_Lecturer, 'python', estimation)

for estimation in [10, 10, 10, 10, 10]:
    Ruoy_Eman_student.evaluation_lecture(Tailer_Durden_Lecturer, 'Git', estimation)

for estimation in [9, 9, 8, 9, 10]:
    Robert_Paulsen_student.evaluation_lecture(Tailer_Durden_Lecturer, 'Git', estimation)

print(Mike_Vazovsky_Reviewer, '\n')
print(Peter_Pedigree_Reviewer, '\n')
print(Some_Buddy_Lecturer, '\n')
print(Tailer_Durden_Lecturer, '\n')
print(Ruoy_Eman_student, '\n')
print(Robert_Paulsen_student, '\n')


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
#
# print(best_student.grades)
