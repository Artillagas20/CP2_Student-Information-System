import tkinter as tk
from tkinter import messagebox
from dashboard import Dashboard
from controller import StudentController


controller = StudentController()


def open_app():
    root = tk.Tk()
    Dashboard(root)
    root.mainloop()


def signup():
    win = tk.Toplevel()
    win.title("Sign Up")

    tk.Label(win, text="Username").pack()
    u = tk.Entry(win)
    u.pack()

    tk.Label(win, text="Password").pack()
    p = tk.Entry(win, show="*")
    p.pack()

    def register():
        if controller.register_user(u.get(), p.get()):
            messagebox.showinfo("Success", "Account created!")
            win.destroy()

    tk.Button(win, text="Register", command=register).pack()


# ===== LOGIN =====
login = tk.Tk()
login.title("Login")
login.geometry("300x200")

tk.Label(login, text="Username").pack()
user = tk.Entry(login)
user.pack()

tk.Label(login, text="Password").pack()
pw = tk.Entry(login, show="*")
pw.pack()


def check():
    if controller.login_user(user.get(), pw.get()):
        login.destroy()
        open_app()
    else:
        messagebox.showerror("Error", "Invalid login")


tk.Button(login, text="Login", command=check).pack(pady=5)
tk.Button(login, text="Sign Up", command=signup).pack()

login.mainloop()