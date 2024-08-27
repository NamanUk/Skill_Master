import tkinter as tk

class ProgressInCoursesFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(bg='white')
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.label_header = tk.Label(self, text="Progress in Current Courses", font=("Arial", 18, "bold"), bg='white')
        self.label_header.pack(pady=(20, 10))

        # Course 1 Progress
        progress_1 = "Python Programming - 75% complete"
        self.label_progress_1 = tk.Label(self, text=progress_1, font=("Arial", 14), bg='white')
        self.label_progress_1.pack(pady=(10, 10))

        # Course 2 Progress
        progress_2 = "Data Science - 60% complete"
        self.label_progress_2 = tk.Label(self, text=progress_2, font=("Arial", 14), bg='white')
        self.label_progress_2.pack(pady=(10, 10))

        # Course 3 Progress
        progress_3 = "Web Development - 40% complete"
        self.label_progress_3 = tk.Label(self, text=progress_3, font=("Arial", 14), bg='white')
        self.label_progress_3.pack(pady=(10, 10))

        # Back button to return to the dashboard
        self.button_back = tk.Button(self, text="Back", font=("Arial", 14), bg='deep sky blue', fg= 'white', command=self.go_back)
        self.button_back.pack(pady=10)

    def go_back(self):
        from personalized_dashboard import PersonalizedDashboardFrame
        self.master.switch_frame(PersonalizedDashboardFrame)
