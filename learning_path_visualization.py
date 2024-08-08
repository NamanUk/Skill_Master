import tkinter as tk
from tkinter import messagebox
from login import LoginFrame

class LearningPathVisualizationFrame(tk.Frame):
    def __init__(self, master=None, return_frame=None):
        super().__init__(master)
        self.master = master
        self.return_frame = return_frame
        self.config(bg='lightblue')
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.label_header = tk.Label(self, text="Learning Path Visualization", font=("Arial", 16, "bold"), bg='lightblue')
        self.label_header.pack(pady=(20, 10))

        # Visual Representation Button
        self.button_visual_path = tk.Button(self, text="Visual Representation of Learning Path", font=("Arial", 12), bg='lightgreen', command=self.show_visual_path)
        self.button_visual_path.pack(pady=(10, 5), padx=10, fill='x')

        # Modules Progress Button
        self.button_modules = tk.Button(self, text="Completed/Ongoing/Upcoming Modules", font=("Arial", 12), bg='lightgreen', command=self.show_modules)
        self.button_modules.pack(pady=5, padx=10, fill='x')

        # Adaptive Difficulty Adjustments Button
        self.button_difficulty = tk.Button(self, text="Adaptive Difficulty Adjustments", font=("Arial", 12), bg='lightgreen', command=self.adjust_difficulty)
        self.button_difficulty.pack(pady=5, padx=10, fill='x')

        # Log Out Button
        self.button_logout = tk.Button(self, text="Log Out", font=("Arial", 14), bg='red', command=self.logout)
        self.button_logout.pack(pady=(10, 2), padx=10, fill='x')

        # Back Button
        self.button_back = tk.Button(self, text="Back", font=("Arial", 14), bg='yellow', command=self.go_back)
        self.button_back.pack(pady=(2, 20), padx=10, fill='x')

    def show_visual_path(self):
        messagebox.showinfo("Visual Path", "This would display a visual representation of the learning path.")

    def show_modules(self):
        messagebox.showinfo("Modules", "This would show details of completed, ongoing, and upcoming modules.")

    def adjust_difficulty(self):
        messagebox.showinfo("Difficulty Adjustments", "Here, users can make adjustments to the difficulty of their learning modules.")

    def logout(self):
        # Placeholder function for logout logic
        messagebox.showinfo("Logout", "You have been logged out.")
        self.master.switch_frame(LoginFrame) 

    def go_back(self):
        from dashboard import DashboardFrame
        self.master.switch_frame(DashboardFrame)

# For standalone testing
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Learning Path Visualization")
    app = LearningPathVisualizationFrame(master=root)
    app.mainloop()
