from tkinter import *
import pandas
import random

# File: main.py
# Project: PyFlashCards
# Purpose: This application creates a deck of flash cards from a csv file
#          Cards are drawn and random and shown to the user, and are flipped after a certain delay
#          User can click "known" and "don't know" buttons for each card
#          Cards that are not known are kept in the deck, known are removed from the deck
#          Remaining deck of cards is saved to a separate csv file, which is loaded next time the app is run


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

wait_seconds = 4        # This is the number of seconds the user can look at a card before each answer is shown

try:                                                        # Check if we have a list of to-learn cards
    data = pandas.read_csv("data/my_study_list.csv")
except FileNotFoundError:                                   # If not, read the full source file
    original_data = pandas.read_csv("data/card_source.csv")
    to_learn = original_data.to_dict(orient="records")
else:                                                       # In either case, our to_learn variable will hold the deck
    to_learn = data.to_dict(orient="records")

keys = list(to_learn[0].keys())                             # What are the dictionary keys (column headings)?
from_title = keys[0]                                        # Apply the first column heading to the From cards
to_title = keys[1]                                          # Apply the second column heading to the To cards


# Function: next_card
# Purpose:  Draws the next card from our remaining deck
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text=from_title, fill="black")
    canvas.itemconfig(card_word, text=current_card[from_title], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(wait_seconds * 1000, func=flip_card)


# Function: flip_card
# Purpose:  Reveals the answer side of the card
def flip_card():
    canvas.itemconfig(card_title, text=to_title, fill="white")
    canvas.itemconfig(card_word, text=current_card[to_title], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# Function: is_known
# Purpose:  If the user says they know this card, remove this card from the deck!
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/my_study_list.csv", index=False)
    next_card()


# UI Setup -----------------------------------------
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(wait_seconds * 1000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()



