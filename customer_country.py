import csv

customers = open('customers.csv' , 'r' , newline='')
customer_file = csv.reader(customers,delimiter=',')
outfile = open('customer_country.csv','w' , newline='')
outfile.write('Name and Country\n')
next(customer_file)

for row in customer_file:
    id = row[0]
    fname = row[1]
    lname = row[2]
    city = row[3]
    country = row[4]
    phone = row[5]
    name = fname + ' ' + lname
    outfile.write(name + ' ' + country + '\n')


outfile.close()