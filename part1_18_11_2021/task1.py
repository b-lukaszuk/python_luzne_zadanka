class Door:
    def __init__(self, id: int):
        self.__open: bool = False
        self.__id: int = id

    def toggleState(self):
        self.__open = not self.__open

    def getId(self) -> int:
        return self.__id

    def isOpen(self) -> bool:
        return self.__open

    def __str__(self) -> str:
        return "door no. %d, state: %s" % (
            self.__id,
            "open" if self.__open else "closed",
        )

    def __repr__(self) -> str:
        return self.__str__()


doors = [Door(i) for i in range(1, 101)]

for i in range(100):
    for someDoor in doors:
        if someDoor.getId() % (i + 1) == 0:
            someDoor.toggleState()

print("I got 100 doors. All of them are closed at the moment.")
print("I go 100 times to the set of doors.")
print("If the index of a door is divisible by the current number of passage")
print("I change its state to the opposite")
print("At the end the only open doors are:")

for aDoor in doors:
    if aDoor.isOpen():
        print(aDoor)

print("That's it. Goodbye!")
