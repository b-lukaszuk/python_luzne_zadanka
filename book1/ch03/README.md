---

# Table of contents

1. [Task 1](#task-1)
2. [Task 2](#task-2)
3. [Task 3](#task-3)

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
