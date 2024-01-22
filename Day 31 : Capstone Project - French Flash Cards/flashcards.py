from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
def generate_words():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(title_canvas, text="French", fill="black")
    canvas.itemconfig(word_canvas, text=current_word["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=current_word["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_word)
    generate_words()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")

window = Tk()
window.title("Flash Cards For French")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
title_canvas = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=generate_words)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

generate_words()

window.mainloop()
