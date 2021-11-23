import numpy as np


def didAllRandGuessesSucceded(
    cupboardSize: int = 10,
    noOfPrisoners: int = 10,
    guessesPerPrisoner: int = 8,
) -> bool:
    cupboard: np.ndarray = np.arange(cupboardSize)
    np.random.shuffle(cupboard)
    cardsFound: np.ndarray = np.zeros(noOfPrisoners)
    for i in range(noOfPrisoners):  # for every prisoner
        guesses: np.ndarray = np.random.randint(
            0, noOfPrisoners, guessesPerPrisoner
        )
        if np.any(guesses == i):
            cardsFound[i] = 1
    return np.all(cardsFound == 1)


def calcProbability(fn, nIter: int = 2000) -> float:
    successes: [bool] = [fn() for _ in range(nIter)]
    return np.mean(successes)
