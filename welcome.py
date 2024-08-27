import tkinter as tk
from register import RegisterFrame
from login import LoginFrame

class WelcomeFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='#FFFFFF')
        self.master = master
        self.pack(expand=True, fill='both')
        self.create_widgets()

    def create_widgets(self):
        self.label_header = tk.Label(self, text="SkillMaster", font=("Helvetica", 28, 'bold'), bg='#FFFFFF', fg='black')
        self.label_header.pack(pady=(100, 50))

        self.button_login = tk.Button(self, text="Log In", font=("Helvetica", 16), bg='lightblue', fg='#FFFFFF', padx=15, pady=5, command=self.open_login)
        self.button_login.pack(pady=20, ipadx=10, ipady=5)

        self.label_sign_up = tk.Label(self, text="New to Skillmaster? Sign Up", fg="black", bg='#FFFFFF', font=("Helvetica", 14), cursor="hand2")
        self.label_sign_up.pack(pady=(30, 20))
        self.label_sign_up.bind("<Button-1>", lambda e: self.master.switch_frame(RegisterFrame))

    def open_login(self):
        self.master.switch_frame(LoginFrame)
