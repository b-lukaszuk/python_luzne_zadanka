Task 8

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
