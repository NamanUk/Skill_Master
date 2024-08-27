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

class PythonCourseFrame(tk.Frame):
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

        self.label_header = tk.Label(scroll_frame.scrollable_frame, text="Python Course", font=("Arial", 18, "bold"), bg='white', fg='black')
        self.label_header.pack(pady=(20, 10))

        details_text = (
            "This course covers the Python programming language, one of the most popular "
            "and versatile languages used today. You'll learn about Python syntax, libraries, "
            "and how to develop applications ranging from simple scripts to complex systems."
        )
        self.label_details = tk.Label(scroll_frame.scrollable_frame, text=details_text, font=("Arial", 14), bg='white', fg='black', wraplength=400, justify="left")
        self.label_details.pack(pady=(10, 20))

        # Module Buttons
        modules = {
            "Module 1: Introduction to Python": self.open_module1,
            "Module 2: Python Syntax": self.open_module2,
            "Module 3: Python Libraries": self.open_module3,
            "Module 4: Python Applications": self.open_module4,
        }

        for module, command in modules.items():
            button = tk.Button(scroll_frame.scrollable_frame, text=module, font=("Arial", 14), bg='deep sky blue', fg='white', width=30, pady=5, command=command)
            button.pack(pady=5)

        # Adding some quiz/MCQ at the end of the course
        self.label_quiz_header = tk.Label(scroll_frame.scrollable_frame, text="Quiz: Test Your Knowledge", font=("Arial", 16, "bold"), bg='white', fg='black')
        self.label_quiz_header.pack(pady=(20, 10))

        self.label_question1 = tk.Label(scroll_frame.scrollable_frame, text="1. What is the correct file extension for Python files?", font=("Arial", 14), bg='white', fg='black')
        self.label_question1.pack(anchor='w', padx=20)
        self.var_q1 = tk.StringVar(value="")

        options_q1 = [".py", ".pt", ".pyt", ".python"]
        for option in options_q1:
            tk.Radiobutton(scroll_frame.scrollable_frame, text=option, variable=self.var_q1, value=option, bg='white', fg='black', font=("Arial", 12)).pack(anchor='w', padx=40)

        self.label_question2 = tk.Label(scroll_frame.scrollable_frame, text="2. How do you create a variable with the numeric value 5 in Python?", font=("Arial", 14), bg='white', fg='black')
        self.label_question2.pack(anchor='w', padx=20)
        self.var_q2 = tk.StringVar(value="")

        options_q2 = ["x = 5", "x = int(5)", "Both of the above", "None of the above"]
        for option in options_q2:
            tk.Radiobutton(scroll_frame.scrollable_frame, text=option, variable=self.var_q2, value=option, bg='white', fg='black', font=("Arial", 12)).pack(anchor='w', padx=40)

        self.button_submit = tk.Button(scroll_frame.scrollable_frame, text="Submit Quiz", font=("Arial", 14), bg='deep sky blue', fg='white', command=self.submit_quiz)
        self.button_submit.pack(pady=20)

        self.button_back = tk.Button(scroll_frame.scrollable_frame, text="Back", font=("Arial", 14), bg='blue', fg='white', command=self.go_back)
        self.button_back.pack(pady=10)

    def submit_quiz(self):
        score = 0
        if self.var_q1.get() == ".py":
            score += 1
        if self.var_q2.get() == "Both of the above":
            score += 1
        messagebox.showinfo("Quiz Result", f"You scored {score}/2.")

    def open_module1(self):
        self.master.switch_frame(Module1Frame)

    def open_module2(self):
        self.master.switch_frame(Module2Frame)

    def open_module3(self):
        self.master.switch_frame(Module3Frame)

    def open_module4(self):
        self.master.switch_frame(Module4Frame)

    def go_back(self):
        from dashboard import DashboardFrame
        self.master.switch_frame(DashboardFrame)

# Define each module frame

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

class Module1Frame(tk.Frame):
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

        self.label_header = tk.Label(scroll_frame.scrollable_frame, text="Module 1: Introduction to Python", font=("Arial", 18, "bold"), bg='white', fg='black')
        self.label_header.pack(pady=(20, 10))

        details_text = (
            "What is Python?\n"
            "Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.\n\n"
            "It is used for:\n"
            "- Web development (server-side)\n"
            "- Software development\n"
            "- Mathematics\n"
            "- System scripting\n\n"
            "What can Python do?\n"
            "- Python can be used on a server to create web applications.\n"
            "- Python can be used alongside software to create workflows.\n"
            "- Python can connect to database systems. It can also read and modify files.\n"
            "- Python can be used to handle big data and perform complex mathematics.\n"
            "- Python can be used for rapid prototyping, or for production-ready software development.\n\n"
            "Why Python?\n"
            "- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).\n"
            "- Python has a simple syntax similar to the English language.\n"
            "- Python has syntax that allows developers to write programs with fewer lines than some other programming languages.\n"
            "- Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.\n"
            "- Python can be treated in a procedural way, an object-oriented way, or a functional way."
        )
        self.label_details = tk.Label(scroll_frame.scrollable_frame, text=details_text, font=("Arial", 14), bg='white', fg='black', wraplength=400, justify="left")
        self.label_details.pack(pady=(10, 20))

        self.button_back = tk.Button(scroll_frame.scrollable_frame, text="Back", font=("Arial", 14), bg='blue', fg='white', command=self.go_back)
        self.button_back.pack(pady=10)

    def go_back(self):
        from python_course import PythonCourseFrame
        self.master.switch_frame(PythonCourseFrame)

class Module2Frame(tk.Frame):
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

        self.label_header = tk.Label(scroll_frame.scrollable_frame, text="Module 2: Python Syntax", font=("Arial", 18, "bold"), bg='white', fg='black')
        self.label_header.pack(pady=(20, 10))

        details_text = (
            "Python Indentation\n\n"
            "Indentation refers to the spaces at the beginning of a code line.\n\n"
            "Where in other programming languages the indentation in code is for readability only, "
            "the indentation in Python is very important.\n\n"
            "Python uses indentation to indicate a block of code.\n\n"
            "Example:\n"
            "if 5 > 2:\n"
            "  print(\"Five is greater than two!\")\n\n"
            "Python will give you an error if you skip the indentation:\n\n"
            "Example (Syntax Error):\n"
            "if 5 > 2:\n"
            "print(\"Five is greater than two!\")\n\n"
            "The number of spaces is up to you as a programmer; the most common use is four, but it has to be at least one.\n\n"
            "Example:\n"
            "if 5 > 2:\n"
            "  print(\"Five is greater than two!\")\n"
            "if 5 > 2:\n"
            "    print(\"Five is greater than two!\")\n\n"
            "You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:\n\n"
            "Example (Syntax Error):\n"
            "if 5 > 2:\n"
            "  print(\"Five is greater than two!\")\n"
            "    print(\"Five is greater than two!\")"
        )
        self.label_details = tk.Label(scroll_frame.scrollable_frame, text=details_text, font=("Arial", 14), bg='white', fg='black', wraplength=400, justify="left")
        self.label_details.pack(pady=(10, 20))

        self.button_back = tk.Button(scroll_frame.scrollable_frame, text="Back", font=("Arial", 14), bg='blue', fg='white', command=self.go_back)
        self.button_back.pack(pady=10)

    def go_back(self):
        from python_course import PythonCourseFrame
        self.master.switch_frame(PythonCourseFrame)

class Module3Frame(tk.Frame):
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

        self.label_header = tk.Label(scroll_frame.scrollable_frame, text="Module 3: Python Libraries", font=("Arial", 18, "bold"), bg='white', fg='black')
        self.label_header.pack(pady=(20, 10))

        details_text = (
            "In this module, you'll explore some of the most popular Python libraries for data manipulation and visualization. "
            "These libraries are essential tools for data science, allowing you to efficiently work with large datasets and create meaningful visualizations.\n\n"
            "1. NumPy\n"
            "NumPy (Numerical Python) is a powerful library for numerical computing in Python. It provides support for large multi-dimensional arrays and matrices, "
            "along with a collection of mathematical functions to operate on these arrays.\n\n"
            "Example:\n"
            "import numpy as np\n"
            "arr = np.array([1, 2, 3, 4])\n"
            "print(arr)\n\n"
            "In this example, we import the NumPy library and create a simple array. NumPy's array objects are more efficient than Python lists for numerical operations.\n\n"
            "2. Pandas\n"
            "Pandas is a library used for data manipulation and analysis. It provides data structures like Series (one-dimensional) and DataFrame (two-dimensional) "
            "that make it easier to handle structured data.\n\n"
            "Example:\n"
            "import pandas as pd\n"
            "data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}\n"
            "df = pd.DataFrame(data)\n"
            "print(df)\n\n"
            "In this example, we create a DataFrame from a dictionary. DataFrames are very useful for working with tabular data, allowing for easy data manipulation and analysis.\n\n"
            "3. Matplotlib\n"
            "Matplotlib is a library for creating static, animated, and interactive visualizations in Python. It is highly customizable and can produce publication-quality plots and charts.\n\n"
            "Example:\n"
            "import matplotlib.pyplot as plt\n"
            "plt.plot([1, 2, 3, 4], [1, 4, 9, 16])\n"
            "plt.xlabel('X-axis label')\n"
            "plt.ylabel('Y-axis label')\n"
            "plt.title('Simple Plot')\n"
            "plt.show()\n\n"
            "In this example, we use Matplotlib to create a simple line plot. The plt.show() function displays the plot in a window."
        )
        self.label_details = tk.Label(scroll_frame.scrollable_frame, text=details_text, font=("Arial", 14), bg='white', fg='black', wraplength=400, justify="left")
        self.label_details.pack(pady=(10, 20))

        self.button_back = tk.Button(scroll_frame.scrollable_frame, text="Back", font=("Arial", 14), bg='blue', fg='white', command=self.go_back)
        self.button_back.pack(pady=10)

    def go_back(self):
        self.master.switch_frame(PythonCourseFrame)

class Module4Frame(tk.Frame):
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

        self.label_header = tk.Label(scroll_frame.scrollable_frame, text="Module 4: Python Applications", font=("Arial", 18, "bold"), bg='white', fg='black')
        self.label_header.pack(pady=(20, 10))

        details_text = (
            "Python is a versatile programming language that is widely used across different fields and industries. In this module, we'll explore some of the key applications of Python and how it can be applied in real-world scenarios.\n\n"
            
            "1. Web Development\n"
            "Python is used extensively in web development, thanks to frameworks like Django and Flask. These frameworks allow developers to build scalable, secure, and maintainable web applications quickly and efficiently.\n\n"
            "Example:\n"
            "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is used by companies like Instagram and Pinterest.\n"
            "Flask is a micro-framework that provides the essentials for building web applications and is known for its simplicity and flexibility.\n\n"

            "2. Automation (Scripting)\n"
            "Python is a popular choice for automation and scripting tasks. With its simple syntax and powerful libraries, Python can be used to automate repetitive tasks, manage system operations, and perform batch processing.\n\n"
            "Example:\n"
            "Automating file renaming, web scraping with libraries like BeautifulSoup, and managing system backups are common automation tasks performed using Python.\n\n"

            "3. Data Science and Machine Learning\n"
            "Python has become the go-to language for data science and machine learning due to its rich ecosystem of libraries like Pandas, NumPy, Scikit-learn, and TensorFlow.\n\n"
            "Example:\n"
            "Python is used for data analysis, building machine learning models, and processing large datasets. Companies like Google, Netflix, and Spotify use Python to power their recommendation systems and data-driven decision-making processes.\n\n"

            "4. Web Scraping\n"
            "Python, with libraries like BeautifulSoup and Scrapy, is a popular tool for web scraping. Web scraping involves extracting data from websites for analysis, research, or other purposes.\n\n"
            "Example:\n"
            "Scraping product prices from e-commerce websites or gathering news articles from online sources are typical examples of web scraping tasks performed using Python.\n\n"

            "5. Game Development\n"
            "Python is also used in game development, particularly for prototyping and creating small to medium-sized games. Libraries like Pygame provide functionalities for game design and development.\n\n"
            "Example:\n"
            "Pygame allows developers to create 2D games quickly, with support for handling graphics, sound, and input devices.\n\n"

            "6. Embedded Systems\n"
            "Python can be used in embedded systems, often in conjunction with platforms like Raspberry Pi. Python scripts can control hardware components, sensors, and other devices, making it a good choice for IoT (Internet of Things) projects.\n\n"
            "Example:\n"
            "Building a home automation system that controls lights, temperature, and security using Python and a Raspberry Pi is a common IoT application.\n\n"

            "7. Scientific Computing\n"
            "Python is widely used in scientific computing for tasks such as simulations, modeling, and statistical analysis. Libraries like SciPy and SymPy are specifically designed for scientific computations.\n\n"
            "Example:\n"
            "Researchers use Python for analyzing experimental data, running simulations, and developing models in fields like physics, chemistry, and biology."
        )
        self.label_details = tk.Label(scroll_frame.scrollable_frame, text=details_text, font=("Arial", 14), bg='white', fg='black', wraplength=400, justify="left")
        self.label_details.pack(pady=(10, 20))

        self.button_back = tk.Button(scroll_frame.scrollable_frame, text="Back", font=("Arial", 14), bg='blue', fg='white', command=self.go_back)
        self.button_back.pack(pady=10)

    def go_back(self):
        self.master.switch_frame(PythonCourseFrame)

# For standalone testing
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Python Course")
    app = PythonCourseFrame(master=root)
    app.mainloop()
