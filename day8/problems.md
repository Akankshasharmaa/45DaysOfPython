# Day 8

## Problem 1

Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

```
first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
```

## Problem 2
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

```
non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
```

## Problem 3
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

```
same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
```

## Problem 4
Given an array of ints length 3, return the sum of all the elements.

```
sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
```