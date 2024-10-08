import requests
from bs4 import BeautifulSoup
import csv

with open('Black Diamond/urls.csv', 'r', newline='') as file:
    urls = []
    reader = csv.reader(file, quotechar='"')
    for row in reader:
        urls.append(row)


with open('Black Diamond/prod.csv', 'w', newline='') as file:
    writer = csv.writer(file, quotechar='"')
    writer.writerow(['Product ID', 'Product Name', 'Description'])
    product_id = 0
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
                writer.writerow([product_id, product_name, product_description])
                print('written')
                product_id += 1
            except:
                pass
        else:
            print(f'Failed to retrieve the webpage at {url}. Status code: {response.status_code}')

