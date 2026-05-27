from model import StudentModel
from view import StudentView


class StudentController:

    def __init__(self):

        self.model = StudentModel()
        self.view = StudentView()

    def add_student(self):

        student = self.view.get_student_input()

        if student["name"] == "" or student["id"] == "" or student["grade"] == "":
            self.view.show_message("All fields are required.\n")
            return

        existing = self.model.find_student(student["id"])

        if existing:
            self.view.show_message("Student ID already exists.\n")
            return

        self.model.add_student(student)

        self.view.show_message("Student added successfully!\n")

    def view_students(self):

        students = self.model.get_students()

        self.view.display_students(students)

    def update_student(self):

        sid = self.view.get_student_id("Enter student ID to update: ")

        student = self.model.find_student(sid)

        if student:

            new_name = input("Enter new name: ")
            new_grade = input("Enter new grade: ")

            student["name"] = new_name
            student["grade"] = new_grade

            self.view.show_message("Student updated successfully!\n")

        else:
            self.view.show_message("Student not found.\n")

    def delete_student(self):

        sid = self.view.get_student_id("Enter student ID to delete: ")

        student = self.model.find_student(sid)

        if student:

            self.model.delete_student(student)

            self.view.show_message("Student deleted successfully!\n")

        else:
            self.view.show_message("Student not found.\n")

    def search_student(self):

        sid = self.view.get_student_id("Enter student ID to search: ")

        student = self.model.find_student(sid)

        if student:

            print("\n=== Student Found ===")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Grade: {student['grade']}\n")

        else:
            self.view.show_message("Student not found.\n")