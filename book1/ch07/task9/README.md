Task 9

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
pictures or conversations in it, "and what is
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

## Usage Example

```bash
python3 main.py alice.txt
```
