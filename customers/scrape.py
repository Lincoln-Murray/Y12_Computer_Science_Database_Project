import requests
import csv
import random

customers = open("db csv's/customers.csv", 'a')
products_orders = open("db csv's/products-orders.csv", 'a')
orders = open("db csv's/orders.csv", 'a')

customers_writer = csv.writer(customers, quotechar='"')
products_orders_writer = csv.writer(products_orders, quotechar='"')
orders_writer = csv.writer(orders, quotechar='"')

num = 85

#customers_writer.writerow(['CustomerID','Name','Address','Card Number','CVV','Expiry'])
#orders_writer.writerow(['OrderID','Date','Address','CustomerID'])
#products_orders_writer.writerow(['Product ID', 'Order ID'])

#modifier = 0
#for i in range(0,num):
#    try:
#        response = requests.get('https://random-person-generator.com/api?preset=personal-details&?country=us')
#        json = response.json()
#        customers_writer.writerow([i+modifier,json['identification']['full_name'], json['contact_information']['home_address'], json['financial_information']['credit_card_number'], json['financial_information']['cvv2'], json['financial_information']['expiration_date']])
#    except:
#        modifier-=1

#num+=modifier



num2 = random.randint(num,2*num)
for ii in range(0, num2):
    orders_writer.writerow([ii, random.randint(0,num)])
    products_orders_writer.writerow([random.randint(0,176),ii])

for iii in range(0, num2):
    if random.randint(1,5) <= 4:
        products_orders_writer.writerow([random.randint(0,176),iii])