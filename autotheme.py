def apply_theme(widget, theme):
    try:
        widget.configure(bg=theme["bg"])
    except:
        pass

    for child in widget.winfo_children():

        # Frame / LabelFrame
        if isinstance(child, (tk.Frame, tk.LabelFrame)):
            try:
                child.configure(bg=theme["card"])
            except:
                pass

        # Label
        if isinstance(child, tk.Label):
            try:
                child.configure(bg=theme["card"], fg=theme["text"])
            except:
                pass

        # Button
        if isinstance(child, tk.Button):
            try:
                child.configure(
                    bg=theme["primary"],
                    fg="white",
                    activebackground=theme["active"]
                )
            except:
                pass

        # Entry
        if isinstance(child, tk.Entry):
            try:
                child.configure(bg="white", fg="black")
            except:
                pass

        apply_theme(child, theme)