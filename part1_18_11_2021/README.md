---

# Table of contents

1. [Info](#info)
2. [Task 1](#task-1)
3. [Task 2](#task-2)
4. [Task 3](#task-3)
5. [Task 4](#task-4)

---

# Info

Tasks from [Rosetta Code. Category: Programming Tasks](https://rosettacode.org/wiki/Category:Programming_Tasks)

# Task 1

[Go to: Table of contents](#table-of-contents)

[100 doors on rosettacode webpage](https://rosettacode.org/wiki/100_doors):

There are 100 doors in a row that are all initially closed.

You make 100 passes by the doors.

The first time through, visit every door and  toggle  the door  (if the door is closed,  open it;   if it is open,  close it).

The second time, only visit every 2nd door   (door #2, #4, #6, ...),   and toggle it.

The third time, visit every 3rd door   (door #3, #6, #9, ...), etc,   until you only visit the 100th door.

**Answer the question:** what state are the doors in after the last pass? Which are open, which are closed?

# Task 2

[Go to: Table of contents](#table-of-contents)

[100 prisoners on rosettacode webpage](https://rosettacode.org/wiki/100_prisoners):

## The Problem

100 prisoners are individually numbered 1 to 100

A room having a cupboard of 100 opaque drawers numbered 1 to 100, that cannot be seen from outside.

Cards numbered 1 to 100 are placed randomly, one to a drawer, and the drawers all closed; at the start.

Prisoners start outside the room
- They can decide some strategy before any enter the room.
- Prisoners enter the room one by one, can open a drawer, inspect the card number in the drawer, then close the drawer.
- A prisoner can open no more than 50 drawers.
- A prisoner tries to find his own number.
- A prisoner finding his own number is then held apart from the others.
- If all 100 prisoners find their own numbers then they will all be pardoned. If any don't then all sentences stand.

## What to do

Simulate several thousand instances of the game where the prisoners randomly open drawers
Simulate several thousand instances of the game where the prisoners use the optimal strategy mentioned in the Wikipedia article, of:
- First opening the drawer whose outside number is his prisoner number.
- If the card within has his number then he succeeds otherwise he opens the drawer with the same number as that of the revealed card. (until he opens his maximum).

Show and compare the computed probabilities of success for the two strategies.

# Task 3

[Go to: Table of contents](#table-of-contents)

[15 puzzle game](https://rosettacode.org/wiki/15_puzzle_game):

## What to do

Implement the 15 puzzle game -> description on [wikipedia page](https://en.wikipedia.org/wiki/15_puzzle)

## How Should I start the game

Just type the following command in Bash:

```bash
python3.8 main.py
```

And enjoy the game!

## To abort the game in the middle

Press C-c (Ctrl-C)

# Task 4

[Go to: Table of contents](#table-of-contents)

[15 puzzle game solver](https://rosettacode.org/wiki/15_puzzle_solver):

## What to do

Your task is to write a program that finds a solution in the fewest moves possible single moves to a random Fifteen Puzzle Game.
I took the liberty of not following the left, right, left ("lrl....") format of the solution (output) suggested on the rosettacode webpage.

## Initial approach

[Wikipedia](https://en.wikipedia.org/wiki/15_puzzle) mentions [A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) as a solver.
So I will start with that and we will see.
