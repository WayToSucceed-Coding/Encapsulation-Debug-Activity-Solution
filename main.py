import tkinter as tk
from tkinter import messagebox


class UserAuthenticationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Login System")
        self.root.geometry("500x600")
        self.root.config(bg="#e9ecef")  # Light gray modern background
        self.root.resizable(False, False)

        # Private attributes for user data
        self.__users = {}

        # Header Section
        header = tk.Frame(root, bg="#343a40", height=100)
        header.pack(fill="x")
        tk.Label(
            header,
            text="🔒 Secure Login System",
            font=("Helvetica", 24, "bold"),
            bg="#343a40",
            fg="white",
        ).place(relx=0.5, rely=0.5, anchor="center")

        # Content Frame
        content_frame = tk.Frame(root, bg="white", bd=0, relief="flat")
        content_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)

        # Title
        tk.Label(
            content_frame,
            text="Login to Your Account",
            font=("Helvetica", 16, "bold"),
            bg="white",
            fg="#495057",
        ).pack(pady=20)

        # Username Entry
        tk.Label(
            content_frame, text="Username:", font=("Arial", 12), bg="white", anchor="w"
        ).place(x=40, y=80, width=100)
        self.username_entry = tk.Entry(
            content_frame,
            font=("Arial", 12),
            bd=0,
            relief="flat",
            highlightbackground="#ced4da",
            highlightthickness=1,
        )
        self.username_entry.place(x=150, y=80, width=200)

        # Password Entry
        tk.Label(
            content_frame, text="Password:", font=("Arial", 12), bg="white", anchor="w"
        ).place(x=40, y=130, width=100)
        self.password_entry = tk.Entry(
            content_frame,
            font=("Arial", 12),
            show="*",
            bd=0,
            relief="flat",
            highlightbackground="#ced4da",
            highlightthickness=1,
        )
        self.password_entry.place(x=150, y=130, width=200)

        # Login Button
        self.login_button = tk.Button(
            content_frame,
            text="Login",
            font=("Arial", 12, "bold"),
            bg="#007bff",
            fg="white",
            activebackground="#0056b3",
            activeforeground="white",
            bd=0,
            relief="flat",
            command=self.__authenticate_user,
        )
        self.login_button.place(x=80, y=250, width=100, height=40)

        # Register Button
        self.register_button = tk.Button(
            content_frame,
            text="Register",
            font=("Arial", 12, "bold"),
            bg="#28a745",
            fg="white",
            activebackground="#218838",
            activeforeground="white",
            bd=0,
            relief="flat",
            command=self.__register_user,
        )
        self.register_button.place(x=220, y=250, width=100, height=40)

        # Footer
        footer = tk.Frame(root, bg="#f8f9fa", height=50)
        footer.pack(side="bottom", fill="x")
        tk.Label(
            footer,
            text="© 2025 Secure Systems Inc.",
            font=("Helvetica", 10),
            bg="#f8f9fa",
            fg="#6c757d",
        ).place(relx=0.5, rely=0.5, anchor="center")

    # Private method to authenticate user
    def __authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.__users and self.__users[username] == password:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    # Private method to register a new user
    def __register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.__users:
            messagebox.showerror("Registration Failed", "User already exists.")
            
        elif not username or not password:
            messagebox.showerror(
                "Registration Failed", "Username and password cannot be empty."
            )
        else:
            self.__users[username] = password
            messagebox.showinfo("Registration Successful", "User registered successfully!")
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = UserAuthenticationApp(root)
    root.mainloop()
