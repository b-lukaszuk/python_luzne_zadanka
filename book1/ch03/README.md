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

Admission Price

(Part 1, Exercise 67 from the book)

## Description

A particular zoo determines the price of admission based on the age of the guest, i.e.

<pre>
Age             Price
<= 2 y.o.       $0
3 to 12 y.o.    $14
>= 65 y.o.      $18
others          $23
</pre>

Create a program that begins by reading the ages of all of the guests in a group from the user (blank line indicates end of data entry). Then the total cost should be displayed.

# Task 2

[Go to: Table of contents](#table-of-contents)

## Title

Parity Bits

(Part 1, Exercise 68 from the book)

## Description

Write a program that computes the [parity bit](https://en.wikipedia.org/wiki/Parity_bit) for groups of 8 bits entered by the user using even parity. Blank line ends input entry phase.

After each string is entered by the user your program should display a clear message indicating whether the parity bit should be 0 or 1.

## My notes

Instruction not entirely clear, so is user allowed to enter, e.g. just one bit (should I then calculate parity bit?).

I'll just stick to the [wikipedia page](https://en.wikipedia.org/wiki/Parity_bit), e.g. the user will be asked to enter 7 bits, the parity bit is 8th bit (calculated by program). Then the user will be given choice to enter another sequence of 7 bits for which another parity bit (8th bit) will be determined. The above will continue until the user quits.

# Task 3

[Go to: Table of contents](#table-of-contents)

## Title

Square Root

(Part 1, Exercise 71 from the book)

## Description

Write a program that implements Newton’s method to compute and display the square root of a number entered by the user.

<pre>
Read x from the user
Initialize guess to x/2
While guess is not good enough do
Update guess to be the average of guess and x/guess
</pre>

[...] good enough when the absolute value of the difference between guess ∗ guess and x was less than or equal to 10^(−12).

# Task 4

[Go to: Table of contents](#table-of-contents)

## Title

Multiple Word Palindromes

(Part 1, Exercise 73 from the book)

## Description

Write a program that checks if a string is a (palindrome)[https://en.wikipedia.org/wiki/Palindrome]. The program should ignore spaces and interpunction characters. It should also treat upper- and lowercase letters as equivalent, e.g.

<pre>
"go dog"
"Flee to me remote elf"
"Some men interpret nine memos."
</pre>

Are all multiple word palindromes.

# Task 5

[Go to: Table of contents](#table-of-contents)

## Title

Multiplication Table.

(Part 1, Exercise 74 from the book)

## Description

Write a program that displays multiplication table (from 1x1 till 10x10). The top row and the 1st left column are headers.

# Task 6

[Go to: Table of contents](#table-of-contents)

## Title

Greatest Common Divisor

(Part 1, Exercise 75 from the book)

## Description

Write a program that reads two positive integers from the user and uses this algorithm to determine and report their greatest common divisor (the largest number, `d`, which divides evenly into both `n` and `m`).

Proposed algorithm:

<pre>
Initialize d to the smaller of m and n.
While d does not evenly divide m or d does not evenly divide n do
Decrease the value of d by 1
Report d as the greatest common divisor of n and m
</pre>

# Task 7

[Go to: Table of contents](#table-of-contents)

## Title

Binary to Decimal

(Part 1, Exercise 77 from the book)

## Description

Write a program that converts a binary (base 2) number to decimal (base 10).

# Task 8

[Go to: Table of contents](#table-of-contents)

## Title

Coin Flip Simulation

(Part 1, Exercise 80 from the book)

## Description

[...]

Create a program that uses Python’s random number generator to simulate flipping a coin several times. The simulated coin should be fair, meaning that the probability of heads is equal to the probability of tails. Your program should flip simulated coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each time the outcome is heads, and a T each time the outcome is tails, with all of the outcomes shown on the same line. Then display the number of flips needed to reach 3 consecutive flips with the same outcome. When your program is run it should perform the simulation 10 times and report the average number of flips needed. Sample output is shown below:

<pre>
H T T T (4 flips)
H H T T H T H T T H H T H T T H T T T (19 flips)
T T T (3 flips)
T H H H (4 flips)
H H H (3 flips)
T H T T H T H H T T H H T H T H H H (18 flips)
H T T H H H (6 flips)
T H T T T (5 flips)
T T H T T H T H T H H H (12 flips)
T H T T T (5 flips)
On average, 7.9 flips were needed.
</pre>
