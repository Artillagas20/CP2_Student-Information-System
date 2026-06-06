import model
import view
import controller

model.load_students()

while True:
    view.menu()

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
        print("Exiting program...")
        break

    else:
        print("Invalid choice.\n")