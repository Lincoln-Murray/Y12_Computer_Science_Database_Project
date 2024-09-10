import requests
import csv
import random

customers = open("../db csv's/customers.csv", 'a')
products_orders = open("db csv's/products-orders.csv", 'a')
orders = open("db csv's/orders.csv", 'a')

customers_writer = csv.writer(customers, quotechar='"')
products_orders_writer = csv.writer(products_orders, quotechar='"')
orders_writer = csv.writer(orders, quotechar='"')

num = 1

for i in range(0,num):
    response = requests.get('https://random-person-generator.com/api?preset=personal-details&?country=us')
    json = response.json()
    customers_writer.writerow([i,json['identification']['full_name'], json['contact_information']['home_address'], json['financial_information']['credit_card_number'], json['financial_information']['cvv2'], json['financial_information']['expiration_date']])
    products_orders_writer.writerow()
for i in range(0, random.randint(num,2*num)):
    orders_writer.writerow([i,json['contact_information']['home_address']])