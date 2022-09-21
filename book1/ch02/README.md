---

# Table of contents

1. [Task 1](#task-1)
2. [Task 2](#task-2)
3. [Task 3](#task-3)
4. [Task 4](#task-4)
5. [Task 5](#task-5)
6. [Task 6](#task-6)

---

# Task 1

[Go to: Table of contents](#table-of-contents)

## Title

Dog Years

(Part 1, Exercise 33 from the book)

## Description

Write a program that implements the conversion from human years to dog years described in the previous paragraph, i.e.

[...] it is better to count each of the first two human years as 10.5 dog years, and then count each additional human year as 4 dog years.


# Task 2

[Go to: Table of contents](#table-of-contents)

## Title

What Color is that Square?

(Part 1, Exercise 45 from the book)

## Description

Write a program that reads a position on a chessboard from the user (e.g. a8, b3). Determine the color of that square.

# Task 3

[Go to: Table of contents](#table-of-contents)

## Title

Chinese Zodiac

(Part 1, Exercise 48 from the book)

## Description

The Chinese zodiac assigns animals to years in a 12 year cycle, e.g.

<pre>
Year: Animal
2000: Dragon
2001: Snake
2002: Horse
2003: Sheep
2004: Monkey
2005: Rooster
2006: Dog
2007: Pig
2008: Rat
2009: Ox
2010: Tiger
2011: Hare
</pre>

Write a program that reads a year from the user and displays the animal associated with that year. Your program should work correctly for any year greater than or equal to zero, not just the ones listed in the table.

## My notes

A year 0 does not exist [see: wikipedia](https://en.wikipedia.org/wiki/Year_zero) so instead the lower limit will be year 1.

# Task 4

[Go to: Table of contents](#table-of-contents)

## Title

Wavelengths of Visible Light

(Part 1, Exercise 54 from the book)

## Description

The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the spectrum is continuous, it is often divided into 6 colors as shown below:

<pre>
Color    Wavelength (nm)
Violet   380 to less than 450
Blue     450 to less than 495
Green    495 to less than 570
Yellow   570 to less than 590
Orange   590 to less than 620
Red      620 to 750
</pre>

Write a program that reads a wavelength from the user and reports its color.

## My notes

I was taught that there are [7 colors of the rainbow](https://en.wikipedia.org/wiki/ROYGBIV)
So instead of violet, I will define:

Indigo: 428-450 nm (should be: 420-450 nm)
Violet: 380-427 nm (should be: 380-435 nm)

# Task 5

[Go to: Table of contents](#table-of-contents)

## Title

Frequency to Name

(Part 1, Exercise 55 from the book)

## Description

Electromagnetic radiation can be classified into one of 7 categories according to its frequency, as shown in the table below:

<pre>
Name              Frequency range (Hz)
Radio waves       Less than 3 × 10^9
Microwaves        3 × 10^9 to less than 3 × 10^12
Infrared light    3 × 10^12 to less than 4.3 × 10^14
Visible light     4.3 × 10^14 to less than 7.5 × 10^14
Ultraviolet light 7.5 × 10^14 to less than 3 × 10^17
X-rays            3 × 10^17 to less than 3 × 10^19
Gamma rays        3 × 10^19 or more
</pre>

Write a program that reads the frequency of the radiation from the user and displays the appropriate name.

# Task 6

[Go to: Table of contents](#table-of-contents)

## Title

Roulette Payouts

(Part 1, Exercise 60 from the book)

## Description

A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34 and 36. The remaining integers between 1 and 36 are used to number the black spaces.

[...] consider the following subset of them in this exercise:
   + Single number (1 to 36, 0, or 00)
   + Red versus Black
   + Odd versus Even (Note that 0 and 00 do not pay out for even)
   + 1 to 18 versus 19 to 36

Write a program that simulates a spin of a roulette wheel by using Python’s random number generator. Display the number that was selected and all of the bets that must be payed, e.g.

<pre>
The spin resulted in 13...
Pay 13
Pay Black
Pay Odd
Pay 1 to 18
</pre>

or

<pre>
The spin resulted in 0...
Pay 0
</pre>

or

<pre>
The spin resulted in 00...
Pay 00
</pre>
