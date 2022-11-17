# Chapter 8. Recursion Exercises.

---

# Table of contents

1. [Task 1](#task-1)

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
