from . import models
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup

# 07-07-20 12:43 a.m listening to pop smokes album its pretty good.
def walmart(request):
    search = request.POST.get('search')
    if search != '' and search is not None and search != 'None':
        # leave this here bc it stops the annoying None search when going to diff pages using pagination
        user = request.user
        models.Search.objects.create(Search_value=search, Search_User=user)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }


        BASE_URL = 'https://www.walmart.com/search/?query={}'
        base_url = 'https://www.walmart.com'
        final_url = BASE_URL.format(quote_plus(search))

        product_links = []
        r = requests.get(final_url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')

        if soup.find('a', class_=['product-title-link', 'line-clamp', 'line-clamp-2', 'truncate-title'], href=True):
            for link in soup.find_all('a', class_=['product-title-link', 'line-clamp', 'line-clamp-2', 'truncate-title'], href=True)[:2]:
                product_links.append(base_url + link['href'])

            for link in product_links:
                r = requests.get(link, headers=headers)

                soup = BeautifulSoup(r.content, 'lxml')

                if soup.find('h1', class_=['prod-ProductTitle', 'font-normal']):
                    name = soup.find('h1', class_=['prod-ProductTitle', 'font-normal']).text
                    price = soup.find('span', class_='price-group').text
                    if soup.find('div', class_=['about-desc', 'about-product-description']):
                        description = (soup.find('div', class_=['about-desc', 'about-product-description']).text[:300] + '...')
                    else:
                        description = 'N/A'
                    link = link
                    image = ('https:' + soup.find('img', alt=f'{name}').get('src'))
                    seller = 'Walmart'

                    if models.Product.objects.filter(Name=name, Link=link, Seller=seller):
                        if models.Product.objects.filter(Name=name, Price=price, Description=description, Link=link, Image=image):
                            continue
                        else:
                            models.Product.objects.filter(Name=name, Link=link).update(Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)
                    else:
                        models.Product.objects.update_or_create(Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)


def hollister(request):
    search = request.POST.get('search')
    if search != '' and search is not None and search != 'None':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }


        BASE_URL = 'https://www.hollisterco.com/shop/us/search?departmentCategoryId=10006&searchTerm={}'
        base_url = 'https://www.hollisterco.com'
        final_url = BASE_URL.format(quote_plus(search))

        product_links = []
        r = requests.get(final_url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        if soup.find('a', class_='product-card__name', href=True):
            for product_link in soup.find_all('a', class_='product-card__name', href=True)[:2]:
                    product_links.append(base_url + product_link['href'])

        for link in product_links:
            r = requests.get(link, headers=headers)

            soup2 = BeautifulSoup(r.content, 'lxml')

            if soup2.find('h1', class_=['product-title-component', 'product-title-main-header']):
                name = soup2.find('h1', class_=['product-title-component', 'product-title-main-header']).text.strip()
                price = soup2.find('span', class_=['product-price-text', 'product-price-font-size']).text
                description = 'N/A'
                image = soup.find('img', alt=f'{name}').get('src')
                link = link
                seller = 'Hollister'

                if models.Product.objects.filter(Name=name, Link=link):
                    if models.Product.objects.filter(Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller):
                        continue
                    else:
                        models.Product.objects.filter(Name=name, Link=link).update(Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)
                else:
                    models.Product.objects.update_or_create(Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)