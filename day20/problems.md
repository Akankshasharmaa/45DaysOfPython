# Day 20

The main topic for this week is the concept of a dictionary. 
In Python they are called dictionaries, but in other languages they may be called maps or hashmaps. 
The concept is the same: it is a way to use a key to access some value. 
It is mapping one set of data (the keys) to another set of data (the values).
The only way to access the value part of the dictionary is to use the key.

## Problem 1

For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information 
based on their name. Create a dictionary (in your file) of names and birthdays.

When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 
The interaction should look something like this:

```
>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
```

Happy coding!

## Problem 2

You will write a small interactive Knock Knock video game.

```
python knock_knock.py

GAME: Knock Knock!
USER: Who's There?
GAME: Tank
USER: Tank Who?
GAME: You're Welcome!
```

Your task is to design the game that does the following:

- Game starts the Knock Knock joke
- User types "Who's There?"
- Game comes up with a follow-up reply to this. All possible replies for the knock knock jokes should be stored in a Dictionary.
- User types "<reply> who?"
- Game looks into the dictionary for the corresponding joke finish for the reply!
  
At any time during the game, when the user is asked for the Input, she can type `exit()` and end the game.

Make sure to use dictionaries and functions for your code.
  
Happy Coding!
