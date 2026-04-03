from .storage import load_data, save_data


def add_student(name):
    """Adds a new student and returns the generated ID."""
    data = load_data()
    new_id = max([s['id'] for s in data['students']], default=0) + 1
    data['students'].append({"id": new_id, "name": name})
    save_data(data)
    return new_id


def add_course(code, title):
    """Adds a new course."""
    data = load_data()
    data['courses'].append({"code": code, "title": title})
    save_data(data)


def enroll(student_id, course_code):
    """Enrolls a student in a course."""
    data = load_data()
    data['enrollments'].append(
        {"student_id": student_id, "course_code": course_code, "grades": []})
    save_data(data)


def add_grade(student_id, course_code, grade):
    """Adds a grade to a specific enrollment."""
    data = load_data()
    for e in data['enrollments']:
        if e['student_id'] == student_id and e['course_code'] == course_code:
            e['grades'].append(grade)
            save_data(data)
            return
    raise ValueError("Enrollment not found.")


def compute_average(student_id, course_code):
    """Calculates the average grade for a student in a course."""
    data = load_data()
    for e in data['enrollments']:
        if e['student_id'] == student_id and e['course_code'] == course_code:
            return sum(e['grades']) / len(e['grades']) if e['grades'] else 0.0
    return 0.0


def compute_gpa(student_id):
    """Calculates the overall GPA for a student."""
    data = load_data()
    student_enrollments = [e for e in data['enrollments']
                           if e['student_id'] == student_id]
    if not student_enrollments:
        return 0.0

    course_averages = [sum(e['grades']) / len(e['grades'])
                       for e in student_enrollments if e['grades']]
    return sum(course_averages) / len(course_averages) if course_averages else 0.0
