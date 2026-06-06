# all ai, not sure how to use the time module.
from datetime import date, timedelta

def business_days_calculator(start_date, n):
    current = start_date
    
    while n > 0:
        current = current + timedelta(days=1)
        if current.weekday() < 5:
            n -= 1
    
    start_name = start_date.strftime("%A")
    end_name = current.strftime("%A")
    
    print(f"Start: {start_name}, {start_date}")
    print(f"Business Target: {end_name}, {current}")

start = date(2026, 1, 2)
business_days_calculator(start, 5)


# **Output:**

# Start: Friday, 2026-01-02
# Business Target: Friday, 2026-01-09