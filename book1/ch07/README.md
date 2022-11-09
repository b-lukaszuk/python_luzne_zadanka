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
9. [Task 9](#task-9)

---

# Task 1

[Go to: Table of contents](#table-of-contents)

## Title

Number the Lines in a File

(Part 1, Exercise 144 from the book)

## Description

Create a program that adds line numbers to a file. The name of the input file will be read from the user, as will the name of the new file that your program will create. Each line in the output file should begin with the line number, followed by a colon and a space, followed by the line from the input file.

## My Notes

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

## My Notes

I will download exemplary datasets from [this public source](https://www.ssa.gov/oact/babynames/limits.html). Let's say I will use data for years 1880 to 1930. I will change file suffix from `.txt` to `.csv`. If the dataset is sorted, I will scramble row order in a file. Finally I will use such files for this exercise.

Format of data (column names) in the `.csv` files: `name`, `gender`, `number of occurences`

# Task 7

[Go to: Table of contents](#table-of-contents)

## Title

Distinct Names

(Part 1, Exercise 157 from the book)

## Description

In this exercise, you will create a program that reads every file in the baby names data set described in Exercise 154. As your program reads the files, it should keep track of each name used for a boy and each name used for a girl. Your program should output two lists. One list will contain all of the names that have been used for girls. The other list will contain all of the names that have been used for boys. Neither of your lists should contain any repeated values.

## My Notes

There will be way too many names to print into the console (it will not be readable). I think I will limit myself to like 10 files. Additionally I will trim the amount of names per file to say 5 male and 5 female.

Since exemplary datasets (and the information how to obtain them) were placed in Task6 (above) here I will not include datasets.

# Task 8

[Go to: Table of contents](#table-of-contents)

## Title

Distinct Names

(Part 1, Exercise 158 from the book)

## Description

[...] write a program that reads a file and displays all of the words in it that are misspelled. Misspelled words will be identified by checking each word in the file against a list of known words. Any words in the user’s file that do not appear in the list of known words will be reported as spelling mistakes.

The user will provide the name of the file to check for spelling mistakes as a command line parameter.

Hint:

While you could load all of the English words from the words data set into a list, searching a list is slow if you use Python’s `in` operator. It is much faster to check if a key is present in a dictionary, or if a value is present in a set. [...]

## My Notes

I think I will use the dictionary that can be found in the file `/usr/share/dict/american-english`. Although I think I will not include the dictionary in the repo. Regarding the file for spellcheck I think I will create *.TXT quickly and include some semi-random words. Again I will not include the *.TXT file in the repo. I think I will require both the dictionary and the file to spellcheck as command line args during this program invocation.

## Usage Example

```bash
python3 main.py file_to_spell_check.txt dictionary.txt
```

# Task 9

[Go to: Table of contents](#table-of-contents)

## Title

Consistent Line Lengths

(Part 1, Exercise 162 from the book)

## Description

[...] Write a program that opens a file and displays it so that each line is filled as full as possible. If you read a line that is too long then your program should break it up into words and add words to the current line until it is full. Then your program should start a new line and display the remaining words. Similarly, if you read a line that is too short then you will need to use words from the next line of the file to finish filling the current line of output. [...]

Example:

Text before:

<pre>
Alice was
beginning to get very tired of sitting by her
sister
on the bank, and of having nothing to do: once
or twice she had peeped into the book her sister
was reading, but it had
no
pictures or conversations in it,"and what is
the use of a book," thought Alice, "without
pictures or conversations?"
</pre>

Text after (When formatted for a line length of 50 characters):

<pre>
Alice was beginning to get very tired of sitting
by her sister on the bank, and of having nothing
to do: once or twice she had peeped into the book
her sister was reading, but it had no pictures or
conversations in it, "and what is the use of a
book," thought Alice, "without pictures or
conversations?"
</pre>
