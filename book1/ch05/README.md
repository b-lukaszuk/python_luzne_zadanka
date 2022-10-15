---

# Table of contents

1. [Task 1](#task-1)
2. [Task 2](#task-2)
3. [Task 3](#task-3)
4. [Task 4](#task-4)
5. [Task 5](#task-5)
6. [Task 6](#task-6)
7. [Task 7](#task-7)
8. [Task 8](#task-8)

---

# Task 1

[Go to: Table of contents](#table-of-contents)

## Title

Negatives, Zeros and Positives

(Part 1, Exercise 108 from the book)

## Description

Create a program that reads integers from the user until a blank line is entered. Once all of the integers have been read your program should display all of the negative numbers, followed by all of the zeros, followed by all of the positive numbers. Within each group the numbers should be displayed in the same order that they were entered by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program should display each value on its own line.

# Task 2

[Go to: Table of contents](#table-of-contents)

## Title

Perfect Numbers

(Part 1, Exercise 110 from the book)

## Description

Write a function that determines whether or not a positive integer is [perfect](https://en.wikipedia.org/wiki/Perfect_number). [...] In addition, write a main program that uses your function to identify and display all of the perfect numbers between 1 and 10,000.

# Task 3

[Go to: Table of contents](#table-of-contents)

## Title

Random Lottery Numbers

(Part 1, Exercise 114 from the book)

## Description

Write a program that generates a random selection of 6 numbers for a lottery ticket (numbers 1 to 49 without a repetition).

# Task 4

[Go to: Table of contents](#table-of-contents)

## Title

Line of Best Fit

(Part 1, Exercise 117 from the book)

## Description

Write a program that accepts x,y coordinates of n-points and returns formula for the line of best fit (linear regression):

<pre>
 y = mx + b
</pre>

where:

$$m = {{\sum xy - {(\sum x) (\sum y) \over n}} \over \sum x^2 - {{(\sum x)^2} \over n}}$$

and

$$b = \overline{y} - m \overline{x}$$

Input is taken from the user, the result is printed on the screen.

# Task 5

[Go to: Table of contents](#table-of-contents)

## Title

Count the Elements

(Part 1, Exercise 121 from the book)

## Description

Create a function named `countRange` which determines and returns the number of elements within a list that are greater than or equal to some minimum value and less than some maximum value.

Signature:

<pre>
def countRange(ints: List[int], min: int, max: int) -> int:
# or
def countRange(floats: List[float], min: float, max: float) -> int:
</pre>

# Task 6

Tokenizing a String

(Part 1, Exercise 122 from the book)

## Description

Tokenizing is the process of converting a string into a list of substrings, known as tokens.

[...]

Write a function that takes a string containing a mathematical expression as its only parameter and breaks it into a list of tokens. Each token should be a parenthesis, an operator, or a number with an optional leading + or - (for simplicity we will only work with integers in this problem). Return the list of tokens as the function’s result.

[...] assume that the string passed to your function always contains a valid mathematical expression consisting of parentheses, operators and integers. 

# Task 7

Generate All Sublists of a List

(Part 1, Exercise 126 from the book)

## Description

[...] write a function that returns a list containing every possible sublist of a list. For example, the sublists of [1, 2, 3] are [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]. Note that your func- tion will always return a list containing at least the empty list because the empty list is a sublist of every list.

# Task 8

The Sieve of Eratosthenes

(Part 1, Exercise 127 from the book)

## Description

Create a Python program that uses [this algorithm](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) to display all of the prime numbers between 2 and a limit entered by the user. If you implement the algorithm correctly you should be able to display all of the prime numbers less than 1,000,000 in a few seconds.

## My notes

Getting the input from the user is boring (I did it many times in the previous exercises from the book), so I will skip that part. I will also limit myself to some smaller number (it is boring to write down so many numbers on the screen and then read it to check the corectness of the input).
