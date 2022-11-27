# -*- coding: utf-8 -*-

from datetime import datetime
import calendar
from typing import List


def main() -> None:
    cal: calendar.TextCalendar = calendar.TextCalendar()
    today_month: int = datetime.today().month
    today_year: int = datetime.today().year
    months_text: List[str] = [
        cal.formatmonth(today_year, month)
        for month in range(today_month - 1, today_month + 2)
    ]
    print("Calendar examples.")
    print("\nPrinting calendar for the current, previous and next month.\n")
    for month in months_text:
        print(month)
    print("That's all. Goodbye!")


if __name__ == "__main__":
    main()
