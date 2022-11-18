# Chapter 8. Recursion Exercises.

---

# Table of contents

1. [Task 1](#task-1)
2. [Task 2](#task-2)
3. [Task 3](#task-3)

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

# Task 3

[Go to: Table of contents](#table-of-contents)

## Title

String Edit Distance

(Part 1, Exercise 169 from the book)

## Description

[...]

Write a recursive function that computes the [edit distance](https://en.wikipedia.org/wiki/Levenshtein_distance) between two strings.

Use the following algorithm:

<pre>
Let s and t be the strings
If the length of s is 0 then
	Return the length of t
Else if the length of t is 0 then
	Return the length of s
Else
	Set cost to 0
	If the last character in s does not equal the last character in t then
		Set cost to 1
	Set d1 equal to the edit distance between all characters except the last one
	in s, and all characters in t, plus 1
	Set d2 equal to the edit distance between all characters in s, and all
	characters except the last one in t, plus 1
	Set d3 equal to the edit distance between all characters except the last one
	in s, and all characters except the last one in t, plus cost
	Return the minimum of d1, d2 and d3
</pre>
