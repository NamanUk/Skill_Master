import tkinter as tk
from tkinter import messagebox
from db import create_connection
import mysql.connector

class RegisterFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(bg='white')  # Neutral background
        self.pack(expand=True, fill='both')
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.label_header = tk.Label(self, text="Create New Account", font=("Arial", 18, 'bold'), bg='white', fg='black')
        self.label_header.pack(pady=(50, 20))

        # Full Name Entry
        self.label_full_name = tk.Label(self, text="Full Name", bg='white', font=("Arial", 12))
        self.label_full_name.pack(pady=(10, 5))
        self.entry_full_name = tk.Entry(self, font=("Arial", 12), bd=2, relief='solid')
        self.entry_full_name.pack(padx=50, pady=5, fill='x')

        # Email Entry
        self.label_email = tk.Label(self, text="Email", bg='white', font=("Arial", 12))
        self.label_email.pack(pady=(10, 5))
        self.entry_email = tk.Entry(self, font=("Arial", 12), bd=2, relief='solid')
        self.entry_email.pack(padx=50, pady=5, fill='x')

        # Phone Number Entry
        self.label_phone = tk.Label(self, text="Phone Number", bg='white', font=("Arial", 12))
        self.label_phone.pack(pady=(10, 5))
        self.entry_phone = tk.Entry(self, font=("Arial", 12), bd=2, relief='solid')
        self.entry_phone.pack(padx=50, pady=5, fill='x')

        # Password Entry
        self.label_password = tk.Label(self, text="Password", bg='white', font=("Arial", 12))
        self.label_password.pack(pady=(10, 5))
        self.entry_password = tk.Entry(self, font=("Arial", 12), show="*", bd=2, relief='solid')
        self.entry_password.pack(padx=50, pady=5, fill='x')

        # Sign Up Button
        self.button_sign_up = tk.Button(self, text="Sign Up", font=("Arial", 14), bg='deep sky blue', fg='white', relief='raised', bd=2, padx=10, pady=5, command=self.register)
        self.button_sign_up.pack(pady=(30, 10))
        
        # Back Button
        self.button_back = tk.Button(self, text="Back", font=("Arial", 12), bg='deep sky blue', fg='white', command=self.go_back)
        self.button_back.pack(pady=(10, 20))

    def register(self):
        if not all([self.entry_full_name.get(), self.entry_email.get(), self.entry_phone.get(), self.entry_password.get()]):
            messagebox.showerror("Registration Error", "All fields are required.")
            return

        connection = create_connection()
        if connection is not None:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO users (full_name, email, phone_number, password) VALUES (%s, %s, %s, %s)",
                               (self.entry_full_name.get(), self.entry_email.get(), self.entry_phone.get(), self.entry_password.get()))
                connection.commit()
                from login import LoginFrame
                messagebox.showinfo("Registration Success", "You have successfully registered!")
                self.master.switch_frame(LoginFrame)
            except mysql.connector.Error as error:
                messagebox.showerror("Database Error", f"An error occurred: {error}")
                connection.rollback()
            finally:
                connection.close()
        else:
            messagebox.showerror("Connection Error", "Can't connect to the database")
    
    def go_back(self):
        from welcome import WelcomeFrame
        self.master.switch_frame(WelcomeFrame)
