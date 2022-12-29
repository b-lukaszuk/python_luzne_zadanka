# Part 2. Exercises 1-50 (selected).

---

# Table of contents

0. [Web Page](#web-page)
1. [Task 1](#task-1)
2. [Task 2](#task-2)
3. [Task 3](#task-3)
4. [Task 4](#task-4)
5. [Task 5](#task-5)

---

# Web Page

Tasks from [w3resource.com](https://www.w3resource.com/python-exercises/basic/)

# Side Note

In general the tasks in this section were a bit too easy for me. Still, I solved a few of them just for practice and to be systematic with the tasks.

# Task 1

[Go to: Table of contents](#table-of-contents)

## Original Exercise Number

Exercise 2

## Description

Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

## My Notes

I will return all the strings for 'a', 'e', 'i', since `factorial(len("aeiou")) = 120` (too many to print), and `factorial(len("aei")) = 6` (good enough to check visually).

# Task 2

[Go to: Table of contents](#table-of-contents)

## Original Exercise Number

Exercise 14

## Description

Write a Python program to add two positive integers without using the '+' operator.

Note: Use bit wise operations to add two numbers.

## My Notes

As for now (23-12-2022) it adds only two positive integers, maybe I will extend it in the future for negative numbers as well.

Actually, yesterday I did not notice that the task description says only about adding two positive integers.

Therefore, I think I will consider my task done (24-12-2022). Still I simplified my solution in version 2 of the program.

# Task 3

[Go to: Table of contents](#table-of-contents)

## Original Exercise Number

Exercise 18

## Description

Write a Python program to find the median among three given numbers.

## My Notes

I'll write a program to find the median among any number of given numbers (finite data set of numbers) according to the [definition](https://en.wikipedia.org/wiki/Median#Finite_data_set_of_numbers).

# Task 4

[Go to: Table of contents](#table-of-contents)

## Original Exercise Number

Exercise 25

## Description

Write a Python program to find the digits which are absent in a given mobile number.

# Task 5

[Go to: Table of contents](#table-of-contents)

## Original Exercise Number

Exercise 27

## Description

Write a Python program to find the type of the progression (arithmetic
progression/geometric progression) and the next successive member of a given
three successive members of a sequence.

According to Wikipedia, an arithmetic progression (AP) is a sequence of numbers
such that the difference of any two successive members of the sequence is a
constant. For instance, the sequence 3, 5, 7, 9, 11, 13, . . . is an arithmetic
progression with common difference 2. For this problem, we will limit ourselves
to arithmetic progression whose common difference is a non-zero integer.  On the
other hand, a geometric progression (GP) is a sequence of numbers where each
term after the first is found by multiplying the previous one by a fixed
non-zero number called the common ratio. For example, the sequence 2, 6, 18, 54,
. . . is a geometric progression with common ratio 3. For this problem, we will
limit ourselves to geometric progression whose common ratio is a non-zero
integer.
