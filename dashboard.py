import tkinter as tk
from tkinter import messagebox
from personalized_dashboard import PersonalizedDashboardFrame
from learning_path_visualization import LearningPathVisualizationFrame

class DashboardFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(bg='white')  # Set background color to white
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.label_header = tk.Label(self, text="Courses", font=("Arial", 18, "bold"), bg='white', fg='black')  # Text black on white background
        self.label_header.pack(pady=(20, 10))

        courses = {
            "Python": self.open_python_course,
            "Arts And Humanity": self.open_arts_and_humanity,
            "Business": self.open_business,
            "Data Science": self.open_data_science,
            "HTML": self.open_html_course,
            "CSS": self.open_css_course,
        }

        for course, command in courses.items():
            button = tk.Button(self, text=course, relief='solid', font=("Arial", 14), bg='deep sky blue', fg='white', width=20, pady=5, command=command)  # Blue buttons with white text
            button.pack(pady=2, padx=10, fill='x')

        self.button_personalized_dashboard = tk.Button(self, text="Personalized Dashboard", font=("Arial", 14), bg='deep sky blue', fg='white', command=self.open_personalized_dashboard)  # Blue buttons with white text
        self.button_personalized_dashboard.pack(pady=(20, 2), padx=10, fill='x')

        self.button_learning_path = tk.Button(self, text="Learning Path Visualization", font=("Arial", 14), bg='deep sky blue', fg='white', command=self.open_learning_path)  # Blue buttons with white text
        self.button_learning_path.pack(pady=2, padx=10, fill='x')

        self.button_logout = tk.Button(self, text="Logout", font=("Arial", 14), bg='red', fg='white', command=self.logout)  # Red button with white text for logout
        self.button_logout.pack(pady=(20, 10), padx=10, fill='x')

    def open_arts_and_humanity(self):
        from arts_and_humanity import ArtsAndHumanityFrame
        self.master.switch_frame(ArtsAndHumanityFrame)

    def open_business(self):
        from business import BusinessFrame
        self.master.switch_frame(BusinessFrame)

    def open_data_science(self):
        from data_science import DataScienceFrame
        self.master.switch_frame(DataScienceFrame)

    def open_python_course(self):
        from python_course import PythonCourseFrame
        self.master.switch_frame(PythonCourseFrame)

    def open_html_course(self):
        from html_course import HTMLCourseFrame
        self.master.switch_frame(HTMLCourseFrame)

    def open_css_course(self):
        from css_course import CSSCourseFrame
        self.master.switch_frame(CSSCourseFrame)

    def open_personalized_dashboard(self):
        self.master.switch_frame(PersonalizedDashboardFrame)

    def open_learning_path(self):
        self.master.switch_frame(LearningPathVisualizationFrame)

    def logout(self):
        messagebox.showinfo("Logout", "You have been logged out.")
        from login import LoginFrame
        self.master.switch_frame(LoginFrame)  

# For standalone testing
if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("Dashboard")
    app = DashboardFrame(master=root)
    app.mainloop()
