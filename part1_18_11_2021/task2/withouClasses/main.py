import numpy as np
import random


def didAllRandGuessesSucceded(
    cupboardSize: int = 10,
    noOfPrisoners: int = 10,
    guessesPerPrisoner: int = 8,
) -> bool:
    cardsFound: np.ndarray = np.zeros(noOfPrisoners)
    for i in range(noOfPrisoners):  # for every prisoner
        for j in range(guessesPerPrisoner):
            guess: np.ndarray = random.randint(0, cupboardSize)
            if guess == i:
                cardsFound[i] = 1
    return np.all(cardsFound == 1)


def calcProbability(fn, nIter: int = 2000) -> float:
    successes: [bool] = [fn() for _ in range(nIter)]
    return np.mean(successes)
