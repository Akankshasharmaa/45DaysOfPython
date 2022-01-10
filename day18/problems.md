# Day 18

## Problem 1 - Password Generator

Write a password generator in Python. Be creative with how you generate passwords - strong passwords
have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Bonus: Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

You will need to use Python’s random module.

## Problem 2 - Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

## Problem 3 - Caesar Cipher

A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a letter found by moving n places down the alphabet. 

For example, assume the input plain text is the following:

`abcd xyz`

If the shift value, n, is 4, then the encrypted text would be the following:

`efgh bcd`

You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in the cipher. 
The function will return an encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged.

Note: You can assume the plain text is all lowercase ASCII except for whitespace and punctuation.

