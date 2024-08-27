import tkinter as tk
from tkinter import messagebox

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, bg='white')
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg='white')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class HTMLCourseFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(bg='white')
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Create the scrollable frame
        scroll_frame = ScrollableFrame(self)
        scroll_frame.pack(fill='both', expand=True)

        self.label_header = tk.Label(scroll_frame.scrollable_frame, text="HTML", font=("Arial", 18, "bold"), bg='white', fg='black')
        self.label_header.pack(pady=(20, 10))

        details_text = (
            "This course covers the essentials of HTML, the fundamental language of the web. "
            "You'll learn how to structure web pages, create links, embed images and videos, "
            "and use various HTML tags to enhance the presentation of content."
        )
        self.label_details = tk.Label(scroll_frame.scrollable_frame, text=details_text, font=("Arial", 14), bg='white', fg='black', wraplength=400, justify="left")
        self.label_details.pack(pady=(10, 20))

        # Adding some quiz/MCQ at the end of the course
        self.label_quiz_header = tk.Label(scroll_frame.scrollable_frame, text="Quiz: Test Your Knowledge", font=("Arial", 16, "bold"), bg='white', fg='black')
        self.label_quiz_header.pack(pady=(20, 10))

        self.label_question1 = tk.Label(scroll_frame.scrollable_frame, text="1. What does HTML stand for?", font=("Arial", 14), bg='white', fg='black')
        self.label_question1.pack(anchor='w', padx=20)
        self.var_q1 = tk.StringVar(value="")

        options_q1 = ["Hyper Text Markup Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language", "None of the above"]
        for option in options_q1:
            tk.Radiobutton(scroll_frame.scrollable_frame, text=option, variable=self.var_q1, value=option, bg='white', fg='black', font=("Arial", 12)).pack(anchor='w', padx=40)

        self.label_question2 = tk.Label(scroll_frame.scrollable_frame, text="2. Choose the correct HTML element for the largest heading:", font=("Arial", 14), bg='white', fg='black')
        self.label_question2.pack(anchor='w', padx=20)
        self.var_q2 = tk.StringVar(value="")

        options_q2 = ["<h1>", "<head>", "<h6>", "<header>"]
        for option in options_q2:
            tk.Radiobutton(scroll_frame.scrollable_frame, text=option, variable=self.var_q2, value=option, bg='white', fg='black', font=("Arial", 12)).pack(anchor='w', padx=40)

        self.button_submit = tk.Button(scroll_frame.scrollable_frame, text="Submit Quiz", font=("Arial", 14), bg='blue', fg='white', command=self.submit_quiz)
        self.button_submit.pack(pady=20)

        self.button_back = tk.Button(scroll_frame.scrollable_frame, text="Back", font=("Arial", 14), bg='blue', fg='white', command=self.go_back)
        self.button_back.pack(pady=10)

    def submit_quiz(self):
        score = 0
        if self.var_q1.get() == "Hyper Text Markup Language":
            score += 1
        if self.var_q2.get() == "<h1>":
            score += 1
        messagebox.showinfo("Quiz Result", f"You scored {score}/2.")

    def go_back(self):
        from dashboard import DashboardFrame
        self.master.switch_frame(DashboardFrame)

# This part is only for testing this frame independently
if __name__ == "__main__":
    class MainApp(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("HTML Course")
            self.geometry("400x500")
            self.switch_frame(HTMLCourseFrame)

        def switch_frame(self, frame_class, **kwargs):
            # Destroy current frame and replace with a new one
            new_frame = frame_class(self, **kwargs)
            if hasattr(self, "_frame"):
                self._frame.destroy()
            self._frame = new_frame
            self._frame.pack(fill='both', expand=True)

    app = MainApp()
    app.mainloop()
