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
            file.write(
                s["id"] + "," +
                s["name"] + "," +
                s["grade"] + "\n"
            )