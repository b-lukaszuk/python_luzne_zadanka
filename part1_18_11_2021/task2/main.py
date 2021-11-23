from Prisoner import Prisoner
from Cupboard import Cupboard

prisoners: [Prisoner] = [Prisoner(i) for i in range(10)]
cupboard: Cupboard = Cupboard(10)


def mkPrisLookForCardRandomly(
    somePrisoners: [Prisoner],
    aCupboard: Cupboard,
    noOfGuessesPerPrisoner: int = 50,
) -> [bool]:
    prisonersCopy: [Prisoner] = somePrisoners[:]
    upRangeOfGuess: int = len(prisonersCopy) - 1
    luckyCardsFound: [bool] = [False] * (upRangeOfGuess + 1)
    for aPrisoner in prisonersCopy:
        curGuess: int = 0
        uncoveredCardId: int = 0
        for _ in range(noOfGuessesPerPrisoner):
            curGuess = aPrisoner.getRandInt(0, upRangeOfGuess)
            uncoveredCardId = aCupboard.getCardIdFromDrawer(curGuess)
            if uncoveredCardId == aPrisoner.getId():
                luckyCardsFound[aPrisoner.getId()] = True
                break
    return luckyCardsFound


def mkPrisLookForCardMethodically(
    somePrisoners: [Prisoner],
    aCupboard: Cupboard,
    noOfGuessesPerPrisoner: int = 50,
):
    upRangeOfGuess: int = len(somePrisoners) - 1
    luckyCardsFound: [bool] = [False] * (upRangeOfGuess + 1)
    for aPrisoner in somePrisoners:
        curGuess: int = aPrisoner.getId()
        uncoveredCardId: int = 0
        for _ in range(noOfGuessesPerPrisoner):
            uncoveredCardId = aCupboard.getCardIdFromDrawer(curGuess)
            if uncoveredCardId == aPrisoner.getId():
                luckyCardsFound[aPrisoner.getId()] = True
                break
            curGuess = uncoveredCardId
    return luckyCardsFound


def calcProbabilityOf100prisPardoned(
    noOfIterations: int,
    prisList: [Prisoner],
    aCupboard: Cupboard,
    noOfGuessesPerPrisoner: int = 50,
    searchRandomly: bool = True,
) -> float:
    allFoundLuckyCard: [bool] = [False] * noOfIterations
    for i in range(noOfIterations):
        if searchRandomly:
            allFoundLuckyCard[i] = all(
                mkPrisLookForCardRandomly(
                    prisList, aCupboard, noOfGuessesPerPrisoner
                )
            )
        else:
            allFoundLuckyCard[i] = all(
                mkPrisLookForCardMethodically(
                    prisList, aCupboard, noOfGuessesPerPrisoner
                )
            )

    return sum(allFoundLuckyCard) / noOfIterations


print(calcProbabilityOf100prisPardoned(1000, prisoners, cupboard, 2))
