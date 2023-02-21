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
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        self.true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=self.true_image, highlightthickness=0)
        self.button_true.grid(row=2, column=0)
        self.false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=self.false_image, highlightthickness=0)
        self.button_false.grid(row=2, column=1)
        
        self.window.mainloop()