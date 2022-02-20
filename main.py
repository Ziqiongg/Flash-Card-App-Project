BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

random_word = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")

except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
# Get random word function
def random_words():
    global random_word
    global flip_timer
    window.after_cancel(flip_timer)
    random_card = random.choice(data)
    random_french = random_card["French"]
    random_word = random_card

    canvas.itemconfig(word_change, text=random_french, fill="black")
    canvas.itemconfig(title_change, text="French", fill="black")
    canvas.itemconfig(image_change, image=front_pic)

    window.after(3000, func= flip_card)

def correct_answer():

    data.remove(random_word)

    new_data = pandas.DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    random_words()

# flip the card
def flip_card():
    global random_word

    canvas.itemconfig(image_change, image=back_pic)
    canvas.itemconfig(title_change, text="English", fill="white")
    canvas.itemconfig(word_change, fill="white", text=random_word["English"])


# create window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# canvas items
canvas = Canvas(width=800, height=526)
front_pic = PhotoImage(file="images/card_front.png")
back_pic = PhotoImage(file="images/card_back.png")
image_change = canvas.create_image(400, 263, image=front_pic)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

title_change = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_change = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))

canvas.grid(column=0, columnspan=2, row=0)

# Buttons
wrong_button = PhotoImage(file="images/wrong.png")
but_wrong = Button(image=wrong_button, highlightthickness=0, command=random_words)
but_wrong.grid(column=0, row=1)

right_button = PhotoImage(file="images/right.png")
but_right = Button(image=right_button, highlightthickness=0, command=correct_answer)
but_right.grid(column=1, row=1)

french_word = random_words()


window.mainloop()
