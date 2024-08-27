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

class ArtsAndHumanityFrame(tk.Frame):
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

        # Display course name as header
        self.label_header = tk.Label(scroll_frame.scrollable_frame, text="Arts and Humanity", font=("Arial", 18, "bold"), bg='white', fg='black')
        self.label_header.pack(pady=(20, 10))

        # Details about the course
        details_text = (
            "This course covers a broad range of topics in the humanities, "
            "including literature, history, philosophy, and the arts. You will "
            "learn about the cultural and historical contexts that have shaped "
            "human thought and creativity. The course is designed to encourage "
            "critical thinking, creativity, and an understanding of the diverse "
            "human experience."
        )
        self.label_details = tk.Label(scroll_frame.scrollable_frame, text=details_text, font=("Arial", 14), bg='white', fg='black', wraplength=400, justify="center")
        self.label_details.pack(pady=(10, 20))

        # Adding some quiz/MCQ at the end of the course
        self.label_quiz_header = tk.Label(scroll_frame.scrollable_frame, text="Quiz: Test Your Knowledge", font=("Arial", 16, "bold"), bg='white', fg='black')
        self.label_quiz_header.pack(pady=(20, 10))

        self.label_question1 = tk.Label(scroll_frame.scrollable_frame, text="1. Which period is known as the Renaissance?", font=("Arial", 14), bg='white', fg='black')
        self.label_question1.pack(anchor='w', padx=20)
        self.var_q1 = tk.StringVar(value="")

        options_q1 = ["14th to 17th century", "5th to 15th century", "19th century", "21st century"]
        for option in options_q1:
            tk.Radiobutton(scroll_frame.scrollable_frame, text=option, variable=self.var_q1, value=option, bg='white', fg='black', font=("Arial", 12)).pack(anchor='w', padx=40)

        self.label_question2 = tk.Label(scroll_frame.scrollable_frame, text="2. Who wrote 'The Republic'?", font=("Arial", 14), bg='white', fg='black')
        self.label_question2.pack(anchor='w', padx=20)
        self.var_q2 = tk.StringVar(value="")

        options_q2 = ["Plato", "Aristotle", "Socrates", "Homer"]
        for option in options_q2:
            tk.Radiobutton(scroll_frame.scrollable_frame, text=option, variable=self.var_q2, value=option, bg='white', fg='black', font=("Arial", 12)).pack(anchor='w', padx=40)

        self.button_submit = tk.Button(scroll_frame.scrollable_frame, text="Submit Quiz", font=("Arial", 14), bg='blue', fg='white', command=self.submit_quiz)
        self.button_submit.pack(pady=20)

        # Back button to return to the dashboard
        self.button_back = tk.Button(scroll_frame.scrollable_frame, text="Back", font=("Arial", 14), bg='blue', fg='white', command=self.go_back)
        self.button_back.pack(pady=10)

    def submit_quiz(self):
        score = 0
        if self.var_q1.get() == "14th to 17th century":
            score += 1
        if self.var_q2.get() == "Plato":
            score += 1
        messagebox.showinfo("Quiz Result", f"You scored {score}/2.")

    def go_back(self):
        # Switch back to the dashboard frame
        from dashboard import DashboardFrame
        self.master.switch_frame(DashboardFrame)

# This part is only for testing this frame independently
if __name__ == "__main__":
    class MainApp(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Arts and Humanity Course")
            self.geometry("400x500")
            self.switch_frame(ArtsAndHumanityFrame)

        def switch_frame(self, frame_class, **kwargs):
            # Destroy current frame and replace with a new one
            new_frame = frame_class(self, **kwargs)
            if hasattr(self, "_frame"):
                self._frame.destroy()
            self._frame = new_frame
            self._frame.pack(fill='both', expand=True)

    app = MainApp()
    app.mainloop()
