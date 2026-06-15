from model import StudentModel


class StudentController:

    def __init__(self):
        self.model = StudentModel()

    # USERS
    def register_user(self, u, p):
        return self.model.register_user(u, p)

    def login_user(self, u, p):
        return self.model.login_user(u, p)

    # STUDENTS
    def add_student(self, sid, name, grade):
        return self.model.add_student(sid, name, grade)

    def get_students(self):
        return self.model.get_students()

    def update_student(self, sid, name, grade):
        return self.model.update_student(sid, name, grade)

    def delete_student(self, sid):
        return self.model.delete_student(sid)

    def search_student(self, sid):
        return self.model.search_student(sid)