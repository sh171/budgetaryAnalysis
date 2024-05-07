import csv

with open("city-of-seattle-2012-expenditures-dollars.csv") as file:
    reader = csv.reader(file, delimiter=",")
    department_expenses = {}
    row_number = 1
    for row in reader:
        if row_number != 1:
            name = row[0] if row[0] != "" else "No department name"
            actual = float(row[3]) if row[3] != "" else 0

            if row[0] not in department_expenses: department_expenses[name] = actual
            else: department_expenses[name] += actual
            row_number += 1
        else: row_number += 1

for name, total_expenses in department_expenses.items():
    print(f"{name} ${total_expenses:.2f}")