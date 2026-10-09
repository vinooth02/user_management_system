import tkinter as tk
from tkinter import messagebox
from user_manager import UserManager


class TkinterApp:

    def __init__(self, root):
        self.root = root
        self.user_manager = UserManager()

        # Color theme
        self.background_color = "#F3F6FB"
        self.primary_color = "#4F46E5"
        self.text_color = "#1F2937"
        self.secondary_text = "#6B7280"
        self.button_hover_color = "#4338CA"

        # Window settings
        self.root.title("User Management System")
        self.root.geometry("600x650")
        self.root.minsize(500, 550)
        self.root.resizable(True, True)
        self.root.configure(bg=self.background_color)

        self.show_main_screen()

    # Clear existing widgets
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Create a styled button
    def create_button(self, parent, text, command, color=None):
        if color is None:
            color = self.primary_color

        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 11, "bold"),
            bg=color,
            fg="white",
            activebackground=self.button_hover_color,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            pady=12,
            bd=0
        )

        return button

    # Create a styled input field
    def create_entry(self, parent, show=None):
        entry = tk.Entry(
            parent,
            font=("Segoe UI", 12),
            relief="flat",
            bg="#FFFFFF",
            fg=self.text_color,
            insertbackground=self.text_color,
            show=show,
            bd=1
        )

        return entry

    # Create screen heading
    def create_title(self, parent, title, subtitle):
        tk.Label(
            parent,
            text=title,
            font=("Segoe UI", 23, "bold"),
            bg=self.background_color,
            fg=self.text_color
        ).pack(pady=(10, 8))

        tk.Label(
            parent,
            text=subtitle,
            font=("Segoe UI", 10),
            bg=self.background_color,
            fg=self.secondary_text
        ).pack(pady=(0, 30))

    # Main screen
    def show_main_screen(self):
        self.clear_screen()

        container = tk.Frame(
            self.root,
            bg=self.background_color
        )
        container.pack(
            expand=True,
            fill="both",
            padx=40,
            pady=30
        )

        # Application title
        tk.Label(
            container,
            text="USER MANAGEMENT",
            font=("Segoe UI", 25, "bold"),
            bg=self.background_color,
            fg=self.text_color
        ).pack(pady=(70, 10))

        tk.Label(
            container,
            text="Welcome! Choose an option to continue.",
            font=("Segoe UI", 11),
            bg=self.background_color,
            fg=self.secondary_text
        ).pack(pady=(0, 40))

        # Register button
        self.create_button(
            container,
            "Create New Account",
            self.show_add_user
        ).pack(fill="x", padx=70, pady=10)

        # Login button
        self.create_button(
            container,
            "Login to Your Account",
            self.show_login
        ).pack(fill="x", padx=70, pady=10)

        # Exit button
        self.create_button(
            container,
            "Exit Application",
            self.root.destroy,
            "#DC2626"
        ).pack(fill="x", padx=70, pady=10)

        tk.Label(
            container,
            text="User Registration and Login System",
            font=("Segoe UI", 9),
            bg=self.background_color,
            fg=self.secondary_text
        ).pack(side="bottom", pady=10)

    # Registration screen
    def show_add_user(self):
        self.clear_screen()

        container = tk.Frame(
            self.root,
            bg=self.background_color
        )
        container.pack(
            expand=True,
            fill="both",
            padx=70,
            pady=30
        )

        self.create_title(
            container,
            "Create Account",
            "Enter your details to register"
        )

        # Username label
        tk.Label(
            container,
            text="Username",
            font=("Segoe UI", 11, "bold"),
            bg=self.background_color,
            fg=self.text_color
        ).pack(anchor="w", pady=(5, 6))

        # Username field
        self.username_entry = self.create_entry(container)
        self.username_entry.pack(
            fill="x",
            ipady=10,
            pady=(0, 20)
        )

        # Password label
        tk.Label(
            container,
            text="Password",
            font=("Segoe UI", 11, "bold"),
            bg=self.background_color,
            fg=self.text_color
        ).pack(anchor="w", pady=(0, 6))

        # Password field
        self.password_entry = self.create_entry(
            container,
            show="*"
        )
        self.password_entry.pack(
            fill="x",
            ipady=10
        )

        # Show password checkbox
        self.show_password_var = tk.BooleanVar(value=False)

        tk.Checkbutton(
            container,
            text="Show password",
            variable=self.show_password_var,
            command=self.toggle_password,
            font=("Segoe UI", 9),
            bg=self.background_color,
            fg=self.secondary_text,
            activebackground=self.background_color,
            selectcolor=self.background_color
        ).pack(anchor="w", pady=8)

        # Register button
        self.create_button(
            container,
            "REGISTER",
            self.register
        ).pack(fill="x", pady=(20, 10))

        # Back button
        tk.Button(
            container,
            text="← Back to Home",
            command=self.show_main_screen,
            font=("Segoe UI", 10),
            bg=self.background_color,
            fg=self.primary_color,
            relief="flat",
            cursor="hand2"
        ).pack(pady=5)

        self.username_entry.focus_set()

    # Login screen
    def show_login(self):
        self.clear_screen()

        container = tk.Frame(
            self.root,
            bg=self.background_color
        )
        container.pack(
            expand=True,
            fill="both",
            padx=70,
            pady=30
        )

        self.create_title(
            container,
            "Welcome Back!",
            "Login to access your account"
        )

        # Username label
        tk.Label(
            container,
            text="Username",
            font=("Segoe UI", 11, "bold"),
            bg=self.background_color,
            fg=self.text_color
        ).pack(anchor="w", pady=(5, 6))

        # Username field
        self.username_entry = self.create_entry(container)
        self.username_entry.pack(
            fill="x",
            ipady=10,
            pady=(0, 20)
        )

        # Password label
        tk.Label(
            container,
            text="Password",
            font=("Segoe UI", 11, "bold"),
            bg=self.background_color,
            fg=self.text_color
        ).pack(anchor="w", pady=(0, 6))

        # Password field
        self.password_entry = self.create_entry(
            container,
            show="*"
        )
        self.password_entry.pack(
            fill="x",
            ipady=10
        )

        # Show password checkbox
        self.show_password_var = tk.BooleanVar(value=False)

        tk.Checkbutton(
            container,
            text="Show password",
            variable=self.show_password_var,
            command=self.toggle_password,
            font=("Segoe UI", 9),
            bg=self.background_color,
            fg=self.secondary_text,
            activebackground=self.background_color,
            selectcolor=self.background_color
        ).pack(anchor="w", pady=8)

        # Login button
        self.create_button(
            container,
            "LOGIN",
            self.login
        ).pack(fill="x", pady=(20, 10))

        # Back button
        tk.Button(
            container,
            text="← Back to Home",
            command=self.show_main_screen,
            font=("Segoe UI", 10),
            bg=self.background_color,
            fg=self.primary_color,
            relief="flat",
            cursor="hand2"
        ).pack(pady=5)

        self.username_entry.focus_set()

    # Show or hide password
    def toggle_password(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    # Register user
    def register(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning(
                "Missing Details",
                "Please enter both username and password."
            )
            return

        success, message = self.user_manager.register_user(
            username,
            password
        )

        if success:
            messagebox.showinfo(
                "Registration Successful",
                message
            )
            self.show_main_screen()
        else:
            messagebox.showerror(
                "Registration Failed",
                message
            )

    # Login user
    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning(
                "Missing Details",
                "Please enter both username and password."
            )
            return

        success, message = self.user_manager.login_user(
            username,
            password
        )

        if success:
            messagebox.showinfo(
                "Login Successful",
                message
            )
        else:
            messagebox.showerror(
                "Login Failed",
                message
            )


# Start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterApp(root)
    root.mainloop()