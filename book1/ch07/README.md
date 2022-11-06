---

# Table of contents

1. [Task 1](#task-1)
2. [Task 2](#task-2)
3. [Task 3](#task-3)
4. [Task 4](#task-4)
5. [Task 5](#task-5)
6. [Task 6](#task-6)
7. [Task 7](#task-7)

---

# Task 1

[Go to: Table of contents](#table-of-contents)

## Title

Number the Lines in a File

(Part 1, Exercise 144 from the book)

## Description

Create a program that adds line numbers to a file. The name of the input file will be read from the user, as will the name of the new file that your program will create. Each line in the output file should begin with the line number, followed by a colon and a space, followed by the line from the input file.

## My notes

Name of the input file and output file will be read from command line args (so, `sys.argv`).

# Task 2

[Go to: Table of contents](#table-of-contents)

## Title

Letter Frequencies

(Part 1, Exercise 146 from the book)

## Description

Write a program that [...] displayes the frequencies of all letters in a file. Ignore spaces, punctuation marks, and numbers as you perform this analysis. Your program should be case insensitive [...]. The user will provide the file name as a command line parameter.

# Task 3

[Go to: Table of contents](#table-of-contents)

## Title

Sum a List of Numbers

(Part 1, Exercise 148 from the book)

## Description

Create a program that sums all of the numbers entered by the user while ignoring any lines entered by the user that are not valid numbers. Your program should display the current sum after each number is entered. It should display an appropriate error message after any invalid input, and then continue to sum any additional numbers entered by the user. Your program should exit when the user enters a blank line. Ensure that your program works correctly for both integers and floating point numbers.

# Task 4

[Go to: Table of contents](#table-of-contents)

## Title

Remove Comments

(Part 1, Exercise 150 from the book)

## Description

[...] create a program that removes all of the comments from a Python source file.

# Task 5

[Go to: Table of contents](#table-of-contents)

## Title

What’s that Element Again?

(Part 1, Exercise 152 from the book)

## Description

Write a program that reads a file containing information about chemical elements and stores it in one or more appropriate data structures. Then your program should read and process input from the user. If the user enters an integer then your program should display the symbol and name of the element with the number of protons entered. If the user enters a string then your program should display the number of protons for the element with that name or symbol. [...] Continue to read input from the user until a blank line is entered.

## My Notes

I will download the periodic table of elements from [PubChem](https://pubchem.ncbi.nlm.nih.gov/periodic-table/) as a CSV file.

My solution is slightly different from the one mentioned in the description, but it is close enough. I could have written the solution to adhere more closely to the requirements, but I prefer it that way (and this is but an exercise).

# Task 6

[Go to: Table of contents](#table-of-contents)

## Title

Names that Reached Number One

(Part 1, Exercise 154 from the book)

## Description

The baby names data set consists of over X files. [...] Write a program that reads every file [...] and identifies all of the names that were most popular [...]. Your program should output two lists: one containing the most popular names for boys and the other containing the most popular names for girls.

## My notes

I will download exemplary datasets from [this public source](https://www.ssa.gov/oact/babynames/limits.html). Let's say I will use data for years 1880 to 1930. I will change file suffix from `.txt` to `.csv`. If the dataset is sorted, I will scramble row order in a file. Finally I will use such files for this exercise.

Format of data (column names) in the `.csv` files: `name`, `gender`, `number of occurences`

# Task 7

[Go to: Table of contents](#table-of-contents)

## Title

Distinct Names

(Part 1, Exercise 157 from the book)

In this exercise, you will create a program that reads every file in the baby names data set described in Exercise 154. As your program reads the files, it should keep track of each name used for a boy and each name used for a girl. Your program should output two lists. One list will contain all of the names that have been used for girls. The other list will contain all of the names that have been used for boys. Neither of your lists should contain any repeated values.
