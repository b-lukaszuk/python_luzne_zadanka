from typing import List


def are_all_coins_legal(coins: List[int]) -> bool:
    illegal_coins: List[int] = [coin for coin in coins if coin not in [1, 5, 10, 25]]
    return len(illegal_coins) == 0


def can_make_change(amount_cents: int, coins: List[int]) -> bool:
    if amount_cents == 0 and len(coins) == 0:
        return True
    if amount_cents <= 0 and len(coins) > 0:
        return False
    if amount_cents >= 0 and len(coins) == 0:
        return False
    else:
        return can_make_change(amount_cents - coins[0], coins[1:])


def get_coins_as_str(coins: List[int]) -> str:
    coins_sorted: List[int] = sorted(coins)
    return ", ".join([str(coin) + "c" for coin in coins_sorted])


def declare_making_change(amount_dollars: float, coins_cents: List[int]) -> None:
    if not are_all_coins_legal(coins_cents):
        raise ValueError("Only 1, 5, 10, 25 cents are accepted.")
    print("\nTrying to make change of ${0}".format(amount_dollars))
    print("Available coins:")
    print(get_coins_as_str(coins_cents))
    print(
        "Operation {0}.".format(
            "successful"
            if can_make_change(int(amount_dollars * 100), coins_cents)
            else "failed"
        )
    )


def print_program_description() -> None:
    print("\nHi.\n")
    print("This is a toy program.")
    print("It checks whether you can make a change.")
    print("For that it requires the amount of money in dollars.")
    print("It also requires a list of coins.")
    print("The input is put into a recursive function.")
    print("The result is displayed on the screen.")
    print("The operation is succesful only if sum(coins) == amount dollars.")
    print("NO GUARANTEE OF ITS ACCURACY. Still, I hope it'll work fine.")
    print("All clear. Then let's begin.")


def main() -> None:
    print_program_description()
    amounts_usd: List[float] = [1, 1, 1, 1.25, 1.25, 1.25, 1.25]
    coins_cents: List[List[int]] = [
        [25, 25, 25, 25],
        [5, 10, 25, 10, 10],
        [25, 25, 25, 10, 10, 5],
        [25, 25, 10, 25, 10, 5, 10, 5],
        [25, 25, 10, 25, 10, 10, 10, 5],
        [25, 25, 10, 25, 10, 25, 10, 5],
        [25, 25, 5, 25, 5, 25, 10, 5],
    ]
    for (amount, coins) in zip(amounts_usd, coins_cents):
        declare_making_change(amount, coins)
    print("\nThat's all. Goodbye!\n")


if __name__ == "__main__":
    main()
