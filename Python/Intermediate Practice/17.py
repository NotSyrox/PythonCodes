# all ai too hard rn
import datetime

from dateutil.relativedelta import relativedelta


def get_age(bday_str, today_str):
    """Return exact age difference as (years, months, days)."""
    bday = datetime.datetime.strptime(bday_str, "%Y-%m-%d").date()
    today = datetime.datetime.strptime(today_str, "%Y-%m-%d").date()
    diff = relativedelta(today, bday)
    return diff.years, diff.months, diff.days


if __name__ == "__main__":
    # Given input from the prompt
    birthdate = "1995-05-15"
    today = "2026-01-02"
    years, months, days = get_age(birthdate, today)
    print(f"Age: {years} years, {months} months, {days} days")
