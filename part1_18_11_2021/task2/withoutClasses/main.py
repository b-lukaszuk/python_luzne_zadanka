#!/usr/bin/env python3.8
import numpy as np
import random

noOfPrisoners: int = 100
noOfCards: int = 100
guessesPerPrisoner: int = 50
noOfIterations: int = 10000


def didAllGuessesSucceded(
    cupboardSize: int = 10,
    noOfPrisoners: int = 10,
    guessesPerPrisoner: int = 8,
    guessRandom: bool = True,
) -> bool:

    cardsFound: np.ndarray = np.zeros(noOfPrisoners)
    cupboard: np.ndarray = np.arange(cupboardSize)
    np.random.shuffle(cupboard)

    for i in range(noOfPrisoners):  # for every prisoner
        if guessRandom:
            guess: int = random.randint(0, cupboardSize - 1)  # incl, incl
        else:
            guess: int = i
        for j in range(guessesPerPrisoner):
            if cupboard[guess] == i:
                cardsFound[i] = 1
                break
            if guessRandom:
                guess = random.randint(0, cupboardSize - 1)  # incl, incl
            else:
                guess = cupboard[guess]

    return np.all(cardsFound == 1)


def calcProbability(fn, nIter: int = 2000) -> float:

    successes: [bool] = [fn() for _ in range(nIter)]
    return np.mean(successes)


def displayInfoAboutStrategy(random: bool) -> None:

    strategy: str = "random" if random else "methodical"
    print("=======================================")
    print(
        "Strategy: {}. No of iterations: {:d}".format(
            strategy, noOfIterations
        )
    )
    print("Please be patient, this may take a while")
    print(
        "p =",
        calcProbability(
            lambda: didAllGuessesSucceded(
                noOfCards, noOfPrisoners, guessesPerPrisoner, random
            ),
            noOfIterations,
        ),
    )


def main() -> None:

    print("====")
    print("Calculating probability of success for:")
    print(
        "{:d} prisoners, {:d} cards,\n{:d} guesses per each prisoner".format(
            noOfPrisoners, noOfCards, guessesPerPrisoner
        )
    )

    displayInfoAboutStrategy(True)
    displayInfoAboutStrategy(False)

    print("====")
    print("That's all. Goodbye.")


if __name__ == "__main__":
    main()
