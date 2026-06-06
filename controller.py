import model
import view


def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    grade = input("Enter grade: ")

    for s in model.students:
        if s["id"] == student_id:
            view.show_message(
                "Student ID already exists!\n"
            )
            return

    student = {
        "id": student_id,
        "name": name,
        "grade": grade
    }

    model.students.append(student)
    model.save_students()

    view.show_message(
        "Student added successfully!\n"
    )


def view_students():
    view.display_students(model.students)


def update_student():
    sid = input("Enter student ID to update: ")

    for s in model.students:
        if s["id"] == sid:
            s["name"] = input(
                "Enter new name: "
            )
            s["grade"] = input(
                "Enter new grade: "
            )

            model.save_students()

            view.show_message(
                "Student updated successfully!\n"
            )
            return

    view.show_message("Student not found.\n")


def delete_student():
    sid = input("Enter student ID to delete: ")

    for s in model.students:
        if s["id"] == sid:
            model.students.remove(s)

            model.save_students()

            view.show_message(
                "Student deleted successfully!\n"
            )
            return

    view.show_message("Student not found.\n")


def search_student():
    sid = input("Enter student ID to search: ")

    for s in model.students:
        if s["id"] == sid:
            view.display_student(s)
            return

    view.show_message("Student not found.\n")