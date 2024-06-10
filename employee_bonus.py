import csv

infile = open('employee_data.csv','r',newline='')
reader = csv.reader(infile)
fields = next(reader)

for row in reader:
    name = row[1]
    salary = float(row[3])
    bonusrate = float(row[7])

    bonus = float(salary * bonusrate)
    pay = float(salary + bonus)

    print(f"Name: {name}\n")
    print(f"Salary: ${salary:>10.2f}\n")
    print(f"Bonus:  ${bonus:>10.2f}\n")
    print(f"Pay:    ${pay:>10.2f}\n")




    input()

infile.close()


