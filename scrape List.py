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


with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product ID', 'Product Name', 'Product Price', 'Description', 'Image URL', 'Manufacturer', 'Product URL', 'Supplier URL'])
    product_id = 0
    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            product_divs = soup.find_all('div', class_='grid-product__content')
            for div in product_divs:
                try:
                    product_name = div.find('div', class_='grid-product__title').text.strip()
                    product_price = div.find('div', class_='grid-product__price').text.strip()
                    try:
                        product_price = div.find('span', class_='grid-product__price--original').text.strip()
                    except:
                        product_price = div.find('div', class_='grid-product__price').text.strip()
                    product_url = 'https://www.blackdiamondequipment.com.au/collections/equipment-climb' + div.find('a', class_='grid-product__link')['href']
                    product_image_url = div.find('noscript').find('img')['src'][2:]
                    writer.writerow([product_id, product_name, product_price, '', product_image_url, 'Black Diamond', product_url, 'https://www.blackdiamondequipment.com.au/collections/equipment-climb'])
                    product_id += 1
                except:
                    pass
    else:
        print(f'Failed to retrieve the webpage at {url}. Status code: {response.status_code}')


