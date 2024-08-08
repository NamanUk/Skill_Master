import tkinter as tk
from welcome import WelcomeFrame

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Skill Master")
        self.geometry("300x550")
        self._frame = None
        self.switch_frame(WelcomeFrame)

    def switch_frame(self, frame_class):
        if self._frame is not None:
            self._frame.destroy()
        self._frame = frame_class(self) 
        self._frame.pack(expand=True, fill='both')

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
