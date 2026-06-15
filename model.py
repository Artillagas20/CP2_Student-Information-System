import sqlite3


class StudentModel:

    def __init__(self):
        self.conn = sqlite3.connect("system.db")
        self.cursor = self.conn.cursor()
        self.create_table()
        self.create_user_table()

    # ===== TABLES =====
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id TEXT PRIMARY KEY,
                name TEXT,
                grade TEXT
            )
        """)
        self.conn.commit()

    def create_user_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """)
        self.conn.commit()

    # ===== USERS =====
    def register_user(self, username, password):
        try:
            self.cursor.execute("""
                INSERT INTO users (username, password)
                VALUES (?, ?)
            """, (username, password))
            self.conn.commit()
            return True
        except:
            return False

    def login_user(self, username, password):
        self.cursor.execute("""
            SELECT * FROM users
            WHERE username=? AND password=?
        """, (username, password))

        return self.cursor.fetchone() is not None

    # ===== STUDENTS (MANUAL ID) =====
    def add_student(self, sid, name, grade):
        try:
            self.cursor.execute("""
                INSERT INTO students (id, name, grade)
                VALUES (?, ?, ?)
            """, (sid, name, grade))

            self.conn.commit()
            return True
        except:
            return False

    def get_students(self):
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()

        return [
            {"id": r[0], "name": r[1], "grade": r[2]}
            for r in rows
        ]

    def update_student(self, sid, name, grade):
        self.cursor.execute("""
            UPDATE students
            SET name=?, grade=?
            WHERE id=?
        """, (name, grade, sid))

        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete_student(self, sid):
        self.cursor.execute("""
            DELETE FROM students
            WHERE id=?
        """, (sid,))

        self.conn.commit()
        return self.cursor.rowcount > 0

    def search_student(self, sid):
        self.cursor.execute("""
            SELECT * FROM students
            WHERE id=?
        """, (sid,))

        row = self.cursor.fetchone()

        if row:
            return {"id": row[0], "name": row[1], "grade": row[2]}
        return None