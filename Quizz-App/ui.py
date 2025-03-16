from quiz_brain import QuizBrain
from tkinter import *
THEME_COLOR = "#375362"

class QuizzInterface():

    def __init__(self,quizz_brain : QuizBrain):
        self.quiz= quizz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.label_score = Label(text=f"Score:{self.score}",justify="center",bg=THEME_COLOR)
        self.label_score.grid(row=0,column=1,padx=20,pady=20)

        self.canvas = Canvas(bg="white",height=250, width=300,highlightthickness=0)
        self.question = self.canvas.create_text(150, 125,width=280, text="some text", font=("Arial", 20, "italic"), fill="black")
        self.canvas.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

        correct_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_image,highlightthickness=0,highlightbackground=THEME_COLOR,command=self.true_pressed)
        self.correct_button.grid(row=2,column=0,padx=20,pady=20)

        incorrect_image = PhotoImage(file="images/false.png")
        self.incorrect_button = Button(image=incorrect_image,highlightthickness=0,highlightbackground=THEME_COLOR,command=self.false_pressed)
        self.incorrect_button.grid(row=2, column=1,padx=20,pady=20)

        self.get_next_question()



        self.window.mainloop()




    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text =q_text )
        else:
            self.canvas.itemconfig(self.question,text ="you have reached the end of the quiz \n Thankyou!" )
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self,is_right):
        if is_right :
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)

        else:
            self.canvas.config(bg="red")
            self.window.after(1000,self.get_next_question)

        self.score = self.quiz.score
        self.label_score.config(text=f"Score:{self.score}")