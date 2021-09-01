# PyFlashCards Application
This is an application which takes a list of items as a csv file and uses it to create interactive flash cards!

## User Experience

- **Example**: Here's an example of the application's interface. The X and Checkmark buttons respond to clicks:

  ![Program Example Image](/doc/pyflashcardspic.png)
  
## Features

* This application creates a deck of flash cards from a csv file, where the first column is question and the second column is answers.
* Cards are drawn at random from the deck and shown to the user, and are flipped to to show the answer after a delay of several seconds.
* User can click "know" (green checkmark) and "don't know" (red x) buttons for each card.
* Cards that the user clicks "don't know" are kept in the deck, while known are removed from the deck.
* When the application is closed, the remaining deck of cards is saved to a separate csv file. This file is loaded as the starting deck next time the app is run!
* csv serialization is done using the Pandas library.

## Purpose

This was an exercise in learning Python.
This is a modified version of Day 31 curriculum as part of [Angela Yu's 100 Days of Code](https://www.udemy.com/course/100-days-of-code/) course on Udemy
For this version, I added functionality where the names of the card categories are read from the headers of the columns on the csv file and set the card flip delay to work from a variable so it is easier to modify. For the card deck, I added a starting csv file containing states with corresponding names of their captiols. The curriculum provided a French-to-English csv file. For a stress test, I also created a Latin to English file, which the serializer has difficulty loading.
