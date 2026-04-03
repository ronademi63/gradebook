import unittest
from gradebook import service


class TestGradebookService(unittest.TestCase):

    def test_add_student(self):
        """Happy-path: verify adding a student returns a valid ID."""
        student_id = service.add_student("Test Student")
        self.assertIsInstance(student_id, int)

    def test_add_grade(self):
        """Happy-path: verify adding a grade to an enrolled student."""
        student_id = service.add_student("Grade User")
        course_code = "PY101"
        service.add_course(course_code, "Python Basics")
        service.enroll(student_id, course_code)

        service.add_grade(student_id, course_code, 95)

    def test_compute_average_edge_case(self):
        """Edge case: compute GPA for a student with no grades."""
        lonely_student = service.add_student("New Student")
        gpa = service.compute_gpa(lonely_student)

        self.assertEqual(gpa, 0.0)


if __name__ == '__main__':
    unittest.main()
