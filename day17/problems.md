# Day 17

More List comprehensions!

Refer to the list comprehension tutorial that you studied on Day 16. 

## Problem 1

Create a list using List comprehension. The contents of this list should represent the ASCII codes of all the characters in your name.

```
Input: 'IronMan'
Output: [73, 114, 111, 110, 77, 97, 110]
```

Hint: `ord('A') returns 65`

## Problem 2

Apply the formula `square(a, b) = square(a) + square(b) + 2 * a * b` on a and b generated from 2 lists.
The first list will go from O up to M
The second list will go from 0 up to N.
Given: M and N

Example:
Input: 10, 11
Output: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
Explaination:
  square(0, 1) = 1
  square(1, 2) = 9
 
Hint: Use `range()` and `zip`. Try to find out what `zip()` does.

## Problem 3

Generate a list of tuples (x, y) where x represents a number, and y represents the square root of that number.
The list should be sorted in descending order. 

Input: 10
Output: `[(10, 4), (9, 3), (8, 3), (7, 3), (6, 3), (5, 3), (4, 2), (3, 2), (2, 2), (1, 1)]`

Hint: Explore the `math` module in the Python standard library. Make sure to convert the square root to its ceiling int value.
