# Day 11 - Happy New Year!

## Problem 1
Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.

```
in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True
```

## Problem 2
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. 

```
near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
```

You might need to use the Mod operator. Read here:

### Mod % Operator

    Modulus operator % -- "mod" for short
    e.g. 23 % 10 → 3
    Repeatedly subtract 10 from 23 .. what's left?
    Like the "remainder" after dividing by 10
    Basically all languages use the % symbol for mod 

You're familiar with the 4 arithmetic operations + - * /. The % modulus operator is an additional arithmetic operation: basically the remainder left over after division. For example, what is 73 % 10? The simplest way to think about it is, keep subtracting 10's from 73 until there's less than 10 left (3 in this case).

    Mod yields 0 means divides evenly
      e.g. 30 % 10 → 0
      "N multiple of 5?" → (N % 5) == 0? 

Key Features of Mod

    When mod by N yields 0, N divides in evenly
    Mod by N yields a number in the range 0..N-1 (inclusive)
      e.g. mod by 10 yields 0..9
      e.g. mod by 100 yields 0..99
    Don't mod by 0, it's an error (like divide by 0 is an error)
    Don't use negative numbers ( * -1 as needed)
    
## Problem 3

We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

```
make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
```

### Hints

Here's the original problem statement: We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return true if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. 

Why Is This Hard At All? #1

    Have 2 big bricks and 2 little bricks
    Can you make a 7?
    Can you make a 8?
    Notice: need little bricks to hit the length exactly 

Why Is This Hard At All? #2

    Suppose you have 2 big bricks and 10 little bricks
    Can you make a 16?
    Note: use lots of little bricks instead of a big brick 

Try the link above to give it a try. 

## Problem 4

Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

```
no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
```