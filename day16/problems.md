# Day 16

## Lets learn about List Comprehensions

We will learn about a new way to create lists in Python.

This technique will allow you to write concise and expressive code in a single line
that typically takes you multiple lines to write. 

It is also one of the most well known and loved features of the Python programming language!

### What are List Comprehensions?

A list comprehension is an expression in Python which is a compact way to 

- Either generate a new list, or 
- Process items in an existing list to create a new resulting list.

It looks like the following:

```
my_numbers = [item for item in range(10)]
```

You can modify the generated output.

```
my_square_nums = [i * i for i in range(10)]
```

And you can also have list comprehensions with conditions

```
my_even_numbers = [i for i in range(10) if i % 2 == 0]
```

### List Comprehension Problems.

Now that you understand what List Comprehensions are, try the following problems.
You are not allowed to use a regular for loop.

Use these variables for the questions below:

```
nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."
```

## Problem 1
Find all of the numbers from 1–1000 that are divisible by 8

## Problem 1
Find all of the numbers from 1–1000 that have a 6 in them

## Problem 1
Count the number of spaces in a string (use string above)

## Problem 1
Remove all of the vowels in a string (use string above)

## Problem 1
Find all of the words in a string that are less than 5 letters (use string above)
