students = []

def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    grade = input("Enter grade: ")

    student = {
        "id": student_id,
        "name": name,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No student records.\n")
    else:
        print("\nStudent List:")
        for s in students:
            print("ID:", s["id"], "| Name:", s["name"], "| Grade:", s["grade"])
        print()


def update_student():
    sid = input("Enter student ID to update: ")

    for s in students:
        if s["id"] == sid:
            s["name"] = input("Enter new name: ")
            s["grade"] = input("Enter new grade: ")
            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    sid = input("Enter student ID to delete: ")

    for s in students:
        students.remove(s)
        print("Student deleted successfully!\n")
        return

    print("Student not found.\n")


while True:
    print("=== Student Information System ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program closed.")
        break
    else:
        print("Invalid choice.\n")