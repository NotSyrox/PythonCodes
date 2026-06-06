# ALL AI (DIDN'T KNOW WHAT LAMBDA DOES AND HOW TI WORKS)

employees = [
    {"name": "A", "salary": 50},
    {"name": "B", "salary": 70},
    {"name": "C", "salary": 60}
]

sorted_employees = sorted(
    employees,
    key=lambda emp: emp["salary"],
    reverse=True
)

print(sorted_employees)
