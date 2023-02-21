from tkinter import *

COLOR = "#375362"

class Interface:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizz Game")
        
        self.window.config(padx=20, pady=20, background=COLOR)
        
        self.score_label = Label(text="Score", fg="white", bg=COLOR)
        self.score_label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.questions_text = self.canvas.create_text(
            150,
            125,
            text="Question",
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=1, pady=50)
        
        self.window.mainloop()