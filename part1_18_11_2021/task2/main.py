from Prisoner import Prisoner
from Cupboard import Cupboard

prisoners: [Prisoner] = [Prisoner(i) for i in range(100)]
cupboard: Cupboard = Cupboard(100)


def didAllPrisonersFoundLuckyCard(somePrisoners: [Prisoner]) -> bool:
    return all([aPrisoner.isLuckyCardFound() for aPrisoner in somePrisoners])


def mkPrisLookForCardRandomly(
    somePrisoners: [Prisoner], aCupboard: Cupboard
) -> [Prisoner]:
    prisonersCopy: [Prisoner] = somePrisoners[:]
    upRangeOfGuess: int = len(prisonersCopy) - 1
    for aPrisoner in prisonersCopy:
        curGuess: int = 0
        uncoveredCardId: int = 0
        for _ in range(50):
            curGuess = aPrisoner.getRandInt(0, upRangeOfGuess)
            uncoveredCardId = aCupboard.getCardIdFromDrawer(curGuess)
            if uncoveredCardId == aPrisoner.getId():
                aPrisoner.setLuckyCardFound(True)
                break
    return prisonersCopy


def calcProbabilityOf100prisPardoned(
    noOfIterations: int, prisList: [Prisoner], aCupboard: Cupboard
) -> float:
    allFoundLuckyCard: [bool] = [False] * noOfIterations
    for i in range(noOfIterations):
        allFoundLuckyCard[i] = didAllPrisonersFoundLuckyCard(
            mkPrisLookForCardRandomly(prisList, aCupboard)
        )
    return sum(allFoundLuckyCard) / noOfIterations


print(calcProbabilityOf100prisPardoned(10000, prisoners, cupboard))
