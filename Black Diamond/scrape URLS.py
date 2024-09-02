import requests
from bs4 import BeautifulSoup
import csv

urls = [
    'https://www.blackdiamondequipment.com.au/collections/equipment-climb?page=1',
    'https://www.blackdiamondequipment.com.au/collections/equipment-climb?page=2',
    'https://www.blackdiamondequipment.com.au/collections/equipment-climb?page=3',
    'https://www.blackdiamondequipment.com.au/collections/equipment-climb?page=4',
    'https://www.blackdiamondequipment.com.au/collections/equipment-climb?page=5',
    'https://www.blackdiamondequipment.com.au/collections/equipment-climb?page=6',
    'https://www.blackdiamondequipment.com.au/collections/equipment-climb?page=7',
    'https://www.blackdiamondequipment.com.au/collections/equipment-climb?page=8',
    'https://www.blackdiamondequipment.com.au/collections/equipment-climb?page=9'
        ]


with open('Black Diamond/urls.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            product_divs = soup.find_all('div', class_='grid-product__content')
            for div in product_divs:
                try:
                    product_url = 'https://www.blackdiamondequipment.com.au/collections/equipment-climb' + div.find('a', class_='grid-product__link')['href']
                    writer.writerow([product_url])
                except:
                    pass
        else:
            print(f'Failed to retrieve the webpage at {url}. Status code: {response.status_code}')


