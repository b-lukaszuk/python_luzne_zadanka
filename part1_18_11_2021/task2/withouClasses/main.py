import numpy as np
import random


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
