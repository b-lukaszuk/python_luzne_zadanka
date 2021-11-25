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


def main():

    print("Calculating probability of success for:")
    print("100 prisoners 100 cards, strategy: random, iterations: 10k ")
    print("Please be patient, this may take a while")
    print(
        "p =",
        calcProbability(
            lambda: didAllGuessesSucceded(100, 100, 50, True), 10000
        ),
    )

    print("====")
    print("Calculating probability of success for:")
    print(
        "100 prisoners 100 cards, strategy: methodological, iterations: 10 k"
    )
    print("Please be patient, this may take a while")
    print(
        "p = ",
        calcProbability(
            lambda: didAllGuessesSucceded(100, 100, 50, False), 10000
        ),
    )

    print("\n====")
    print("That's all. Goodbye.")


if __name__ == "__main__":
    main()
