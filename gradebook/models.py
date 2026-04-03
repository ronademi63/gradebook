class Student:
    def __init__(self, student_id, name):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        self.id = student_id
        self.name = name

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}')"


class Course:
    def __init__(self, code, title):
        if not code or not title:
            raise ValueError("Code and Title are required.")
        self.code = code
        self.title = title

    def __repr__(self):
        return f"Course(code='{self.code}', title='{self.title}')"


class Enrollment:
    def __init__(self, student_id, course_code, grades=None):
        self.student_id = student_id
        self.course_code = course_code
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")
        self.grades.append(grade)

    def __repr__(self):
        return f"Enrollment(student_id={self.student_id}, course_code='{self.course_code}', grades={self.grades})"
