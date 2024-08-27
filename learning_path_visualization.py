import tkinter as tk
from tkinter import messagebox
from login import LoginFrame
from PIL import Image, ImageTk

class LearningPathVisualizationFrame(tk.Frame):
    def __init__(self, master=None, return_frame=None):
        super().__init__(master)
        self.master = master
        self.return_frame = return_frame
        self.config(bg='white')
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.label_header = tk.Label(self, text="Learning Path Visualization", font=("Arial", 16, "bold"), bg='white')
        self.label_header.pack(pady=(10, 5))

        # Graph 1: Display an image of the progress graph
        self.display_graph_image("progress_graph.png", (300, 200))

        # Graph 2: Display an image of the learning path coverage graph
        self.display_graph_image("coverage_graph.png", (200, 170))

        # Log Out Button
        self.button_logout = tk.Button(self, text="Log Out", font=("Arial", 12), bg='red', fg= 'white', command=self.logout)
        self.button_logout.pack(pady=(5, 2), padx=10, fill='x')

        # Back Button
        self.button_back = tk.Button(self, text="Back", font=("Arial", 12), bg='deep sky blue', fg= 'white', command=self.go_back)
        self.button_back.pack(pady=(2, 10), padx=10, fill='x')

    def display_graph_image(self, image_path, size):
        # Load the image using PIL
        image = Image.open(image_path)

        # Resize the image to fit the specified size
        resized_image = image.resize(size, Image.LANCZOS)

        # Display the resized image
        photo = ImageTk.PhotoImage(resized_image)
        label = tk.Label(self, image=photo, bg='white')
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack(pady=5)

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
