import tkinter as tk
import mysql.connector
from tkinter import messagebox
from db import create_connection

class LoginFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(bg='white')  # Use a neutral background color
        self.pack(expand=True, fill='both')
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.label_header = tk.Label(self, text="SkillMaster", font=("Arial", 24, 'bold'), bg='white', fg='deep sky blue')
        self.label_header.pack(pady=(50, 20))

        # Email Entry
        self.label_email = tk.Label(self, text="Email", bg='white', font=("Arial", 12))
        self.label_email.pack(pady=(10, 5))
        self.entry_email = tk.Entry(self, font=("Arial", 12), bd=2, relief='solid')
        self.entry_email.pack(padx=50, pady=5, fill='x')

        # Password Entry
        self.label_password = tk.Label(self, text="Password", bg='white', font=("Arial", 12))
        self.label_password.pack(pady=(10, 5))
        self.entry_password = tk.Entry(self, font=("Arial", 12), show="*", bd=2, relief='solid')
        self.entry_password.pack(padx=50, pady=5, fill='x')

        # Login Button
        self.button_login = tk.Button(self, text="Log In", font=("Arial", 14), bg='deep sky blue', fg='white', relief='raised', bd=2, padx=10, pady=5, command=self.login)
        self.button_login.pack(pady=(20, 10))

        # Sign Up Link
        self.label_sign_up = tk.Label(self, text="New to Skillmaster? Sign Up", fg="dodger blue", bg='white', font=("Arial", 12), cursor="hand2")
        self.label_sign_up.pack(pady=(20, 10))
        from register import RegisterFrame
        self.label_sign_up.bind("<Button-1>", lambda e: self.master.switch_frame(RegisterFrame))

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        connection = create_connection()

        if connection is not None:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
                account = cursor.fetchone()
                if account:
                    from dashboard import DashboardFrame
                    messagebox.showinfo("Login Success", "You have successfully logged in!")
                    self.master.switch_frame(DashboardFrame)  # Assuming DashboardFrame is correctly set up to be called
                else:
                    messagebox.showerror("Login Failed", "Invalid email or password")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
            finally:
                connection.close()  # Ensure connection is closed after operation
        else:
            messagebox.showerror("Connection Error", "Can't connect to the database")
