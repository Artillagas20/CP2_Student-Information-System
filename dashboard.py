import tkinter as tk
from theme import Theme
from view import StudentView
from autotheme import apply_theme


class Dashboard:

    def __init__(self, root):
        self.root = root
        self.theme_mode = "DARK"
        self.theme = Theme.DARK

        root.title("Dashboard")
        root.geometry("500x350")

        self.card = tk.Frame(root)
        self.card.pack(expand=True)

        tk.Label(self.card,
                 text="STUDENT SYSTEM",
                 font=("Arial", 16, "bold")).pack(pady=10)

        self.btn_open = tk.Button(
            self.card,
            text="Open System",
            command=self.open_system
        )
        self.btn_open.pack(pady=5)

        self.btn_theme = tk.Button(
            self.card,
            text="Toggle Theme",
            command=self.toggle_theme
        )
        self.btn_theme.pack(pady=5)

        self.btn_exit = tk.Button(
            self.card,
            text="Exit",
            command=root.destroy
        )
        self.btn_exit.pack(pady=5)

        self.apply()

    # ===== OPEN SYSTEM =====
    def open_system(self):
        self.root.destroy()
        root = tk.Tk()
        StudentView(root)
        root.mainloop()

    # ===== THEME TOGGLE =====
    def toggle_theme(self):
        if self.theme_mode == "DARK":
            self.theme_mode = "LIGHT"
            self.theme = Theme.LIGHT
        else:
            self.theme_mode = "DARK"
            self.theme = Theme.DARK

        self.apply()

    # ===== APPLY THEME =====
    def apply(self):
        self.root.configure(bg=self.theme["bg"])
        apply_theme(self.root, self.theme)