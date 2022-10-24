def main() -> None:
    users_input: str = "xxx"
    sum: float = 0
    cur_num: float = 0
    while users_input.strip() != "":
        print("\nEnter a number to add to total or press Enter to terminate program.")
        print("Curent total: {0:.2f}".format(sum))
        users_input = input("Your input: ")
        try:
            if users_input.strip() != "":
                cur_num = float(users_input)
                sum += cur_num
        except ValueError:
            print("This is not number. Try again.")
    print("Terminating program.")
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
