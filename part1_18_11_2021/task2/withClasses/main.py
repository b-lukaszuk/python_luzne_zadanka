from Prisoner import Prisoner
from Cupboard import Cupboard

prisoners: [Prisoner] = [Prisoner(i) for i in range(10)]
cupboard: Cupboard = Cupboard(10)


def mkPrisLookForLuckyCards(
    somePrisoners: [Prisoner],
    aCupboard: Cupboard,
    noOfGuessesPerPrisoner: int = 8,
    searchRandomly: bool = True,
) -> [bool]:

    upRangeOfGuess: int = len(somePrisoners) - 1
    luckyCardsFound: [bool] = [False] * (upRangeOfGuess + 1)

    for p in somePrisoners:

        if searchRandomly:
            curGuess: int = p.getRandInt(0, upRangeOfGuess)
        else:
            curGuess: int = p.getId()

        for _ in range(noOfGuessesPerPrisoner):
            uncoveredCardId: int = aCupboard.getCardIdFromDrawer(curGuess)
            if uncoveredCardId == p.getId():
                luckyCardsFound[p.getId()] = True
                break
            if searchRandomly:
                curGuess = p.getRandInt(0, upRangeOfGuess)
            else:
                curGuess = uncoveredCardId
    return luckyCardsFound  # lucky cards found or not


def calcProbabilityOfAllPrisPardoned(
    fn,
    noOfIterations: int,
) -> float:
    allFoundLuckyCard: [bool] = [False] * noOfIterations

    for i in range(noOfIterations):
        allFoundLuckyCard[i] = all(fn())

    return sum(allFoundLuckyCard) / noOfIterations
