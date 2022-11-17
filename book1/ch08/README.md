# Chapter 8. Recursion Exercises.

---

# Table of contents

1. [Task 1](#task-1)
2. [Task 2](#task-2)

---

# Task 1

[Go to: Table of contents](#table-of-contents)

## Title

Greatest Common Divisor

(Part 1, Exercise 165 from the book)

## Description

Euclid was a Greek mathematician who lived approximately 2,300 years ago. His algorithm for computing the greatest common divisor of two positive integers, a and b, is both efficient and recursive. [...]:

<pre>
If b is 0 then
	Return a
Else
	Set c equal to the remainder when a is divided by b
	Return the greatest common divisor of b and c
</pre>

Write a program that implements Euclid’s algorithm [...].

# Task 2

[Go to: Table of contents](#table-of-contents)

## Title

Recursive Palindrome

(Part 1, Exercise 167 from the book)

## Description

[...]

In this exercise you will write a recursive function that determines whether or not a string is a [palindrome](https://en.wikipedia.org/wiki/Palindrome). The empty string is a palindrome, as is any string containing only one character. Any longer string is a palindrome if its first and last characters match, and if the string formed by removing the first and last characters is also a palindrome [...].
