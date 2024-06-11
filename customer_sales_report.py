import csv

customer_totals = {}

sales = open('sales.csv', 'r', newline='')
sales_file = csv.reader(sales, delimiter=',')
next(sales_file)
    
for row in sales_file:
    id = int(row[0])
    subtotal = float(row[3])
    tax = float(row[4])
    freight = float(row[5])   
        
    total = subtotal + tax + freight
        
    
    if id in customer_totals:
        customer_totals[id] += total
    else:
        customer_totals[id] = total

outfile = open('salesreport.csv', 'w', newline='')
outfile.write('Customer , Total\n') 

for id, total in customer_totals.items():
    outfile.write(f"{id}{'  '}{(total):.2f}\n")

outfile.close()

