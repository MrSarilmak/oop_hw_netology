# #


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # def __str__(self):
    #     return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating_all_lections = 0

    def __str__(self):
        if len(self.grades):
            all_ratings = [grade for grades in self.grades.values() for grade in grades]
            if all_ratings:
                average_homework_grade = int(sum(all_ratings) / len(all_ratings))
            else:
                average_homework_grade = 0
        else:
            average_homework_grade = 0
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_homework_grade}"

    def __lt__(self, other) -> bool | None:
        if isinstance(other, Lecturer):
            return self.average_rating_all_lections < other.average_rating_all_lections
        else:
            return None

    def __le__(self, other) -> bool | None:
        if isinstance(other, Lecturer):
            return self.average_rating_all_lections <= other.average_rating_all_lections
        else:
            return None

    def __gt__(self, other) -> bool | None:
        if isinstance(other, Lecturer):
            return self.average_rating_all_lections > other.average_rating_all_lections
        else:
            return None

    def __ge__(self, other) -> bool | None:
        if isinstance(other, Lecturer):
            return self.average_rating_all_lections >= other.average_rating_all_lections
        else:
            return None

    def update_avarage_rating_all_lections(self):
        all_ratings = [grade for grades in self.grades.values() for grade in grades]
        if all_ratings:
            self.average_rating_all_lections = int(sum(all_ratings) / len(all_ratings))
        else:
            self.average_rating_all_lections = 0

    # def rate_(self):
    #     pass


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade) -> bool:
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                return True
            else:
                student.grades[course] = [grade]
                return True
        else:
            return False

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating_all_hw = 0

    def __str__(self):
        if len(self.grades):
            average_homework_grade = sum(self.grades.values()) / len(self.grades)
        else:
            average_homework_grade = 0
        if self.courses_in_progress:
            courses_in_progress = ", ".join(self.courses_in_progress)
        else:
            courses_in_progress = "Нет"
        if self.finished_courses:
            finished_courses = ", ".join(self.finished_courses)
        else:
            finished_courses = "Нет"
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_homework_grade}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def __lt__(self, other) -> bool | None:
        if isinstance(other, Student):
            return self.average_rating_all_hw < other.average_rating_all_hw
        else:
            return None

    def __le__(self, other) -> bool | None:
        if isinstance(other, Student):
            return self.average_rating_all_hw <= other.average_rating_all_hw
        else:
            return None

    def __gt__(self, other) -> bool | None:
        if isinstance(other, Student):
            return self.average_rating_all_hw > other.average_rating_all_hw
        else:
            return None

    def __ge__(self, other) -> bool | None:
        if isinstance(other, Student):
            return self.average_rating_all_hw >= other.average_rating_all_hw
        else:
            return None

    def __eq__(self, other) -> bool | None:
        if isinstance(other, Student):
            return self.average_rating_all_hw == other.average_rating_all_hw
        else:
            return None

    def __ne__(self, other) -> bool | None:
        if isinstance(other, Student):
            return self.average_rating_all_hw != other.average_rating_all_hw
        else:
            return None

    def update_avarage_rating_all_hw(self):
        all_ratings = [grade for grades in self.grades.values() for grade in grades]
        if all_ratings:
            self.average_rating_all_hw = int(sum(all_ratings) / len(all_ratings))
            print(self.average_rating_all_hw)
        else:
            self.average_rating_all_hw = 0

    def rate_lecturer(self, lecturer, course, grade) -> bool:
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                return True
            else:
                lecturer.grades[course] = [grade]
                return True
        else:
            return False


def average_grade_students(students: list[Student], course: str) -> int:
    students_grades = []
    for student in students:
        if course in student.grades:
            course_grade = student.grades[course]
            students_grades += course_grade if course_grade else []
    return sum(students_grades) / len(students_grades)


def average_grade_lecturers(lecturers: list[Lecturer], course: str) -> int:
    lecturers_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            course_grade = lecturer.grades[course]
            lecturers_grades += course_grade if course_grade else []
    return sum(lecturers_grades) / len(lecturers_grades)


student1 = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student('Ruoy', 'Eman', 'your_gender')

lecturer1 = Lecturer('Some', 'Buddy')
lecturer2 = Lecturer('Some', 'Buddy')

reviewer1 = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('Some', 'Buddy')

reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student2, "Python", 10)
reviewer2.rate_hw(student1, "Python", 10)
reviewer2.rate_hw(student2, "Python", 10)

reviewer1.rate_hw(student1, "Git", 10)
reviewer1.rate_hw(student2, "Git", 10)
reviewer2.rate_hw(student1, "Git", 10)
reviewer2.rate_hw(student2, "Git", 10)

student1.courses_in_progress += ["Python", "Java", "Git"]
student2.courses_in_progress += ["Python", "Java", "Git"]

lecturer1.courses_attached += ["Python", "Git"]
lecturer2.courses_attached += ["Python", "Git"]

reviewer1.rate_hw(student1, "Python", 10)
reviewer2.rate_hw(student1, "Python", 10)

student1.rate_lecturer(lecturer1, "Python", 10)
student1.rate_lecturer(lecturer2, "Python", 10)
student2.rate_lecturer(lecturer1, "Python", 10)
student2.rate_lecturer(lecturer2, "Python", 10)

student1.rate_lecturer(lecturer1, "Git", 10)
student1.rate_lecturer(lecturer2, "Git", 10)
student2.rate_lecturer(lecturer1, "Git", 10)
student2.rate_lecturer(lecturer2, "Git", 10)

lecturer1.update_avarage_rating_all_lections()
lecturer2.update_avarage_rating_all_lections()

student1.update_avarage_rating_all_hw()
student2.update_avarage_rating_all_hw()

print(f"student1 < student2 = {student1 < student2}")
print(f"student1 > student2 = {student1 > student2}")
print(f"student1 == student2 = {student1 == student2}")
print(f"student1 != student2 = {student1 != student2}")
print(f"student1 <= student2 = {student1 <= student2}")
print(f"student1 >= student2 = {student1 >= student2}")
print(f"student1 <= lecturer2 = {student1 <= student2}")

print("=" * 30)

print(f"lecturer1 < lecturer2 = {lecturer1 < lecturer2}")
print(f"lecturer1 > lecturer2 = {lecturer1 > lecturer2}")
print(f"lecturer1 == lecturer2 = {lecturer1 == lecturer2}")
print(f"lecturer1 != lecturer2 = {lecturer1 != lecturer2}")
print(f"lecturer1 <= lecturer2 = {lecturer1 <= lecturer2}")
print(f"lecturer1 >= lecturer2 = {lecturer1 >= lecturer2}")

print(f"=\n:student1:\n{student1}")
print(f"=\n:student2:\n{student2}")
print(f"=\n:lecturer1:\n{lecturer1}")
print(f"=\n:lecturer2:\n{lecturer2}")
print(f"=\n:reviewer1:\n{reviewer1}")
print(f"=\n:reviewer2:\n{reviewer2}\n=")
