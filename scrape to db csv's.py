import requests
from bs4 import BeautifulSoup
import csv

with open('urls.csv', 'r', newline='') as file:
    urls = []
    reader = csv.reader(file, quotechar='"')
    for row in reader:
        urls.append(row)


#manufacturer = open("db csv's/manufacturer.csv", 'a')
options = open("db csv's/options.csv", 'a')
products_supplier = open("db csv's/products-supplier.csv", 'a')
products = open("db csv's/products.csv", 'a')
#supplier = open("db csv's/supplier.csv", 'a')
#manufacturer_writer = csv.writer(manufacturer, quotechar='"')
options_writer = csv.writer(options, quotechar='"',)
products_supplier_writer = csv.writer(products_supplier, quotechar='"')
products_writer = csv.writer(products, quotechar='"')
#supplier_writer = csv.writer(supplier, quotechar='"')

#products_writer.writerow(['Product ID','Manufacturer ID', 'Product Name', 'Description'])
#products_supplier_writer.writerow(['Product ID','Supplier ID', 'Product URL', 'Price'])


product_id = 177
for url in urls:
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            product_name = soup.find('h1', class_='h1 product-single__title').text.strip()
            print(product_name)
            try:
                product_description = soup.find('div', class_='product-description long').text.strip()
            except:
                product_description = soup.find('div', class_='rte').text.strip()
            try:
                product_price = soup.find('span', class_='product__price product__price--compare').text.strip()
            except:
                product_price = soup.find('span', class_='product__price').text.strip()
            products_writer.writerow([product_id, 0, product_name, product_description])
            products_supplier_writer.writerow([product_id, 0, str(url), product_price])
            print('written' + str(url))
            product_id += 1
        except:
            pass
    else:
        print(f'Failed to retrieve the webpage at {url}. Status code: {response.status_code}')


