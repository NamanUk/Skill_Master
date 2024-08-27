import tkinter as tk

class CourseRecommendationsFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(bg='white')
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.label_header = tk.Label(self, text="Course Recommendations", font=("Arial", 18, "bold"), bg='white')
        self.label_header.pack(pady=(20, 10))

        # Recommended Course 1
        recommendation_1 = (
            "1. Advanced Data Science\n"
            "   - Why Recommended: Based on your interest in data analysis and "
            "   machine learning, this course will help you advance your skills.\n"
            "   - Cost: $299"
        )
        self.label_details = tk.Label(self, text=recommendation_1, font=("Arial", 14), bg='white', wraplength=250, justify="left")
        self.label_details.pack(pady=(10, 20))

        # Recommended Course 2
        recommendation_2 = (
            "2. Full-Stack Web Development\n"
            "   - Why Recommended: Given your background in Python and HTML, this course "
            "   will equip you with the skills to build complete web applications.\n"
            "   - Cost: $399"
        )
        
        self.label_details = tk.Label(self, text=recommendation_2, font=("Arial", 14), bg='white', wraplength=250, justify="left")
        self.label_details.pack(pady=(10, 20))

        # Back button to return to the dashboard
        self.button_back = tk.Button(self, text="Back", font=("Arial", 14), bg='deep sky blue', fg= 'white', command=self.go_back)
        self.button_back.pack(pady=10)

    def go_back(self):
        from personalized_dashboard import PersonalizedDashboardFrame
        self.master.switch_frame(PersonalizedDashboardFrame)
