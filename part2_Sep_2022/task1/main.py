no_of_years: int = 30
months_in_year: int = 12
monthly_savings_usd: int = 700
annual_return: float = 0.07
account_balance_goal: float = 1e6
final_account_balance: float = 0


def calculate_compound_interest(
    monthly_deposit: int = monthly_savings_usd,
    no_of_months: int = no_of_years * months_in_year,
    annual_interest_rate: float = annual_return,
) -> float:
    sum: float = 0
    for _ in range(no_of_months):
        sum += monthly_deposit
        sum += sum * (annual_interest_rate / 12)
    return sum


final_account_balance = calculate_compound_interest()


def print_task_description(
    no_of_years: int = no_of_years,
    monthly_savings_usd: int = monthly_savings_usd,
    annual_return: float = annual_return,
) -> None:
    print("\nTask description")
    print(
        "Bryn just started a new job, but is already thinking of retirement"
    )
    print("She wants to retire as a millionaire")
    print("She plans on saving ${0} per month".format(monthly_savings_usd))
    print(
        "She expects to receive an annual return of {:0.2f}%".format(
            annual_return * 100
        )
    )
    print(
        "Will she be a millionaire if she retires in {0} years?\n".format(
            no_of_years
        )
    )
    print("My assumptions:")
    print("Money are put into account 1st day of a month")
    print("Interests are calculated last day of a month (1/12 of +7%)\n")


def main() -> None:
    print("Welcome in the program calculating compound interest")
    print_task_description()
    print("In the end, Bryn saved is ${:0,.2f}".format(final_account_balance))
    print(
        "Is she a millionaire? {0}".format(
            final_account_balance >= account_balance_goal
        )
    )
    print("WARNING! NO GUARANTEE THAT THE RESULT IS CORRECT!")
    print("\nThat is all. Goodbye.")


if __name__ == "__main__":
    main()
