def menu():
    print("===== STUDENT INFORMATION SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")


def show_message(message):
    print(message)


def display_students(students):
    if len(students) == 0:
        print("No student records.\n")
    else:
        print("\nStudent List:")
        for s in students:
            print(
                "ID:", s["id"],
                "| Name:", s["name"],
                "| Grade:", s["grade"]
            )
        print()


def display_student(student):
    print("\nStudent Found:")
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Grade:", student["grade"])
    print()