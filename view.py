class StudentView:

    def display_menu(self):

        print("===== Student Information System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

    def get_student_input(self):

        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        grade = input("Enter grade: ")

        return {
            "id": student_id,
            "name": name,
            "grade": grade
        }

    def display_students(self, students):

        if len(students) == 0:
            print("No student records.\n")
            return

        print("\n=== Student Records ===")

        for s in students:
            print(f"ID: {s['id']}")
            print(f"Name: {s['name']}")
            print(f"Grade: {s['grade']}")
            print("-------------------")

        print()

    def show_message(self, message):
        print(message)

    def get_student_id(self, text):
        return input(text)