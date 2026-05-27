from controller import StudentController


controller = StudentController()

while True:

    controller.view.display_menu()

    choice = input("Enter choice: ")

    if choice == "1":
        controller.add_student()

    elif choice == "2":
        controller.view_students()

    elif choice == "3":
        controller.update_student()

    elif choice == "4":
        controller.delete_student()

    elif choice == "5":
        controller.search_student()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice.\n")