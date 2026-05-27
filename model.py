class StudentModel:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students

    def find_student(self, student_id):

        for student in self.students:
            if student["id"] == student_id:
                return student

        return None

    def delete_student(self, student):
        self.students.remove(student)