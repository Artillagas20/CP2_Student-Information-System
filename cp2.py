students = []

def load_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 3:
                    student = {
                        "id": data[0],
                        "name": data[1],
                        "grade": data[2]
                    }
                    students.append(student)

    except FileNotFoundError:
        pass


def save_students():
    with open("students.txt", "w") as file:
        for s in students:
            file.write(s["id"] + "," + s["name"] + "," + s["grade"] + "\n")


def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    grade = input("Enter grade: ")

    for s in students:
        if s["id"] == student_id:
            print("Student ID already exists!\n")
            return

    student = {
        "id": student_id,
        "name": name,
        "grade": grade
    }

    students.append(student)
    save_students()
    print("Student added successfully!\n")


def view_students():
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


def update_student():
    sid = input("Enter student ID to update: ")

    for s in students:
        if s["id"] == sid:
            s["name"] = input("Enter new name: ")
            s["grade"] = input("Enter new grade: ")

            save_students()
            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    sid = input("Enter student ID to delete: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)

            save_students()
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def search_student():
    sid = input("Enter student ID to search: ")

    for s in students:
        if s["id"] == sid:
            print("\nStudent Found:")
            print("ID:", s["id"])
            print("Name:", s["name"])
            print("Grade:", s["grade"])
            print()
            return

    print("Student not found.\n")


load_students()

while True:
    print("===== STUDENT INFORMATION SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

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
        search_student()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.\n")