import requests
from bs4 import BeautifulSoup
import csv

urls = [
    'https://www.lasportiva.com/au/man/apparel/climbing?p=1',
    'https://www.lasportiva.com/au/man/apparel/climbing?p=2',
    'https://www.lasportiva.com/au/man/apparel/climbing?p=3',
    'https://www.lasportiva.com/au/man/apparel/climbing?p=4',
    'https://www.lasportiva.com/au/man/apparel/climbing?p=5',
    'https://www.lasportiva.com/au/man/apparel/climbing?p=6',
    'https://www.lasportiva.com/au/man/apparel/climbing?p=7',
    'https://www.lasportiva.com/au/man/apparel/climbing?p=8',
    'https://www.lasportiva.com/au/man/apparel/climbing?p=9',
    'https://www.lasportiva.com/au/man/apparel/climbing?p=10'
        ]


with open('La Sportiva/urls.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for url in urls:
        response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        print(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            product_divs = soup.find_all('li', class_='item product product-item')
            for div in product_divs:
                try:
                    product_url = div.find('a', class_='product photo product-item-photo')['href']
                    print('    ' + str(product_url))
                    writer.writerow([product_url])
                    print('    written')
                except:
                    pass
        else:
            print(f'Failed to retrieve the webpage at {url}. Status code: {response.status_code}')