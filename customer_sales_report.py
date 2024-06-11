import csv

sales = open('sales.csv','r',newline='')
sales_file = csv.reader(sales,delimiter=' ')
outfile = open('salesreport.csv', 'w', newline='')

outfile.write('Customer','Total')
next(sales_file)

for row in sales_file:
    id = row[0]
    odate = row[1]
    sdate = row[2]
    subtotal = float(row[3])
    tax = float(row[4])
    freight = float(row[5])

    total = subtotal + tax + freight
    print(id, total)


outfile.close()
