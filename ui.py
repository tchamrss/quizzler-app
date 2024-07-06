import tkinter as tk
from tkinter import PhotoImage
from quiz_brain import  QuizBrain

# Definiere eine Theme-Farbe
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, width=400, height=550, bg=THEME_COLOR)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,  # x-Koordinate
            125,  # y-Koordinate
            width= 280,
            text="some question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Labels
        self.score_text = tk.Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_text.grid(column=1, row=0)

        # Bilder und Buttons
        right_img = PhotoImage(file="images/true.png")
        self.right_button = tk.Button(padx=20, pady=20, image=right_img, command=self.true_pressed , bg=THEME_COLOR, highlightthickness=0)
        self.right_button.grid(column=0, row=2)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = tk.Button(image=wrong_img,command=self.false_pressed, bg=THEME_COLOR, highlightthickness=0)
        self.wrong_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_text.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


# quiz_brain = QuizBrain()
# quiz_ui = QuizInterface(quiz_brain)
