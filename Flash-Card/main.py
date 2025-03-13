import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
try:
    df =  pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")


french_english_dict = df.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_english_dict)
    canvas.itemconfig(card_title,text="French",fill="Black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="Black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000,flip)

def flip():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title,text="English",fill="White")
    canvas.itemconfig(card_word,text=current_card["English"],fill="White")

def remove_word():
    french_english_dict.remove(current_card)
    new_df = pandas.DataFrame(french_english_dict)
    new_df.to_csv("data/words_to_learn.csv",index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer = window.after(3000,flip)


canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

card_back = PhotoImage("images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
card_image =canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="Black")
card_word = canvas.create_text(400, 263, text="", fill="Black", font=("Arial", 60, "bold"))

canvas.grid(row=0,column=0,columnspan=2)


known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=remove_word)
known_button.grid(row=1, column=0)

unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=1)

next_card()
window.mainloop()
