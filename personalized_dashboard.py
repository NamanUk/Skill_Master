import tkinter as tk
from tkinter import messagebox

class PersonalizedDashboardFrame(tk.Frame):
    def __init__(self, master=None, return_frame=None):
        super().__init__(master)
        self.master = master
        self.return_frame = return_frame  # Store the frame to return to
        self.config(bg='lightblue')
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.label_header = tk.Label(self, text="Personalized Dashboard", font=("Arial", 18, "bold"), bg='lightblue')
        self.label_header.pack(pady=(20, 10))

        # Course Recommendations
        self.button_course_recs = tk.Button(self, text="Course Recommendations", font=("Arial", 12), bg='lightgreen', command=self.show_course_recommendations)
        self.button_course_recs.pack(pady=(10, 5), padx=10, fill='x')

        # Progress in Current Courses
        self.button_course_progress = tk.Button(self, text="Progress in Current Courses", font=("Arial", 12), bg='lightgreen', command=self.show_course_progress)
        self.button_course_progress.pack(pady=5, padx=10, fill='x')

        # Notifications for Real-Time Feedback
        self.button_notifications = tk.Button(self, text="Notifications for Real-Time Feedback", font=("Arial", 12), bg='lightgreen', command=self.show_notifications)
        self.button_notifications.pack(pady=5, padx=10, fill='x')

        # Click Next Button
        self.button_next = tk.Button(self, text="Click Next", font=("Arial", 14), bg='red', command=self.next_page)
        self.button_next.pack(pady=(10, 5), padx=10, fill='x')

        # Back Button
        self.button_back = tk.Button(self, text="Back", font=("Arial", 14), bg='yellow', command=self.go_back)
        self.button_back.pack(pady=(5, 20), padx=10, fill='x')

    def show_course_recommendations(self):
        messagebox.showinfo("Course Recommendations", "Displaying course recommendations...")

    def show_course_progress(self):
        messagebox.showinfo("Progress in Courses", "Displaying progress in current courses...")

    def show_notifications(self):
        messagebox.showinfo("Notifications", "Displaying notifications for real-time feedback...")

    def next_page(self):
        messagebox.showinfo("Next Page", "Moving to the next page...")
        # Implement the logic to switch to another frame or close current popup

    def go_back(self):
        from dashboard import DashboardFrame
        self.master.switch_frame(DashboardFrame)  

# For standalone testing
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Personalized Dashboard")
    app = PersonalizedDashboardFrame(master=root)
    app.mainloop()
