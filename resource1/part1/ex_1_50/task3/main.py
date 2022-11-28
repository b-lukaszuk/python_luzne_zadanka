# -*- coding: utf-8 -*-

from datetime import datetime as dt
from typing import List, Tuple

# date1, date2 example: 2022-11-27 (yyyy-mm-dd)
def get_no_of_days_between_dates(date1, date2) -> int:
    d1: dt = dt.strptime(date1, "%Y-%m-%d")
    d2: dt = dt.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def main() -> None:
    print("Day difference (inclusive-exclusive) between two dates examples.")
    dates: List[Tuple[str, str]] = [
        ("2014-07-02", "2014-07-11"),
        ("2022-11-27", "2022-12-01"),
        ("2022-02-24", "2022-11-27"),
    ]
    for (date1, date2) in dates:
        print("\nCalculating number of days between {0} and {1}".format(date1, date2))
        print("Result {0}".format(get_no_of_days_between_dates(date1, date2)))
    print("\nThat's all. Goodbye!")


if __name__ == "__main__":
    main()
