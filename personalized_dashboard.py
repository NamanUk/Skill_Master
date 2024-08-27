import tkinter as tk
from tkinter import messagebox

class PersonalizedDashboardFrame(tk.Frame):
    def __init__(self, master=None, return_frame=None):
        super().__init__(master)
        self.master = master
        self.return_frame = return_frame  # Store the frame to return to
        self.config(bg='white')
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.label_header = tk.Label(self, text="Personalized Dashboard", font=("Arial", 18, "bold"), bg='white')
        self.label_header.pack(pady=(20, 10))

        # Course Recommendations
        self.button_course_recs = tk.Button(self, text="Course Recommendations", font=("Arial", 12), bg='deep sky blue', fg= 'white', command=self.open_course_recommendations)
        self.button_course_recs.pack(pady=(10, 5), padx=10, fill='x')

        # Progress in Current Courses
        self.button_course_progress = tk.Button(self, text="Progress in Current Courses", font=("Arial", 12), bg='deep sky blue', fg= 'white', command=self.open_progress_in_courses)
        self.button_course_progress.pack(pady=5, padx=10, fill='x')

        # log out Button
        self.button_next = tk.Button(self, text="Log Out", font=("Arial", 14), bg='red', fg= 'white', command=self.logout)
        self.button_next.pack(pady=(10, 5), padx=10, fill='x')

        # Back Button
        self.button_back = tk.Button(self, text="Back", font=("Arial", 14), bg='deep sky blue', fg= 'white', command=self.go_back)
        self.button_back.pack(pady=(5, 20), padx=10, fill='x')
        
    def open_course_recommendations(self):
        from course_recommendations import CourseRecommendationsFrame
        self.master.switch_frame(CourseRecommendationsFrame)
        
    def open_progress_in_courses(self):
        from progress_in_courses import ProgressInCoursesFrame
        self.master.switch_frame(ProgressInCoursesFrame)
        
    def logout(self):
        # Placeholder function for logout logic
        from login import LoginFrame
        messagebox.showinfo("Logout", "You have been logged out.")
        self.master.switch_frame(LoginFrame)

    def go_back(self):
        from dashboard import DashboardFrame
        self.master.switch_frame(DashboardFrame)  

# For standalone testing
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Personalized Dashboard")
    app = PersonalizedDashboardFrame(master=root)
    app.mainloop()
