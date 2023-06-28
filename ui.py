from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(pady=20, padx=20)

        self.label_score = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Um texto ai",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )

        button_img_true = PhotoImage(file="./images/true.png")
        self.button_true = Button(image=button_img_true, highlightthickness=0, command=self.true_button)
        self.button_true.grid(row=2, column=0)

        button_img_false = PhotoImage(file="./images/false.png")
        self.button_false = Button(image=button_img_false, highlightthickness=0, command=self.false_button)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.label_score.destroy()
            self.canvas.itemconfig(self.question_text, text=f"Quiz concluído\npontos: {self.quiz.score}/{self.quiz.question_number}")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_button(self):
        self.feedback(self.quiz.check_answer("true"))

    def false_button(self):
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, resposta):
        if resposta:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
