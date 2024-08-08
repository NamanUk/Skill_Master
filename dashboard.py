import tkinter as tk
from tkinter import messagebox
from personalized_dashboard import PersonalizedDashboardFrame
from learning_path_visualization import LearningPathVisualizationFrame

class DashboardFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(bg='lightblue')
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Header for the courses section
        self.label_header = tk.Label(self, text="Courses", font=("Arial", 18, "bold"), bg='lightblue')
        self.label_header.pack(pady=(20, 10))

        # Buttons for each course category
        courses = ["Arts And Humanity", "Business", "Data Science", "Python", "HTML", "CSS"]
        for course in courses:
            button = tk.Button(self, text=course, relief='solid', font=("Arial", 14), bg=self.random_color(), width=20, pady=5, command=lambda c=course: self.open_course(c))
            button.pack(pady=2, padx=10, fill='x')

        # Personalized Dashboard Button
        self.button_personalized_dashboard = tk.Button(self, text="Personalized Dashboard", font=("Arial", 14), bg=self.random_color(), command=self.open_personalized_dashboard)
        self.button_personalized_dashboard.pack(pady=(20, 2), padx=10, fill='x')

        # Learning Path Visualization Button
        self.button_learning_path = tk.Button(self, text="Learning Path Visualization", font=("Arial", 14), bg=self.random_color(), command=self.open_learning_path)
        self.button_learning_path.pack(pady=2, padx=10, fill='x')

        # Logout Button
        self.button_logout = tk.Button(self, text="Logout", font=("Arial", 14), bg='red', command=self.logout)
        self.button_logout.pack(pady=(20, 10), padx=10, fill='x')

    def random_color(self):
        # Function to generate random light colors for buttons
        import random
        return f'#{random.randint(160,255):02x}{random.randint(160,255):02x}{random.randint(160,255):02x}'

    def open_course(self, course):
        # Placeholder function to handle course button click
        messagebox.showinfo("Course Selected", f"You have selected {course}.")

    def open_personalized_dashboard(self):
        # Assume you have a way to switch to the PersonalizedDashboardFrame
        self.master.switch_frame(PersonalizedDashboardFrame)

    def open_learning_path(self):
        # Assume you have a way to switch to the LearningPathVisualizationFrame
        self.master.switch_frame(LearningPathVisualizationFrame)

    def logout(self):
        # Placeholder function for logout logic
        messagebox.showinfo("Logout", "You have been logged out.")
        from login import LoginFrame
        self.master.switch_frame(LoginFrame)  

# For standalone testing
if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("Dashboard")
    app = DashboardFrame(master=root)
    app.mainloop()
