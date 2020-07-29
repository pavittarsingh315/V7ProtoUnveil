from . import models
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup
from django.db.models import F

# 07-07-20 12:43 a.m listening to pop smokes album its pretty good.
def searchcreateobject(request):
    search = request.POST.get('search').capitalize()
    user = request.user
    if search != '' and search is not None and search != 'None':
        # leave this here bc it stops the annoying None search when going to diff pages using pagination
        if models.User_Search.objects.filter(Search_value=search, Search_User=user):
            models.User_Search.objects.filter(Search_value=search, Search_User=user).update(Frequency=F('Frequency')+1)
        else:
            models.User_Search.objects.create(Search_value=search, Search_User=user, Frequency=1)

        if models.Search.objects.filter(Search_value=search):
            models.Search.objects.filter(Search_value=search).update(Frequency=F('Frequency')+1)
        else:
            models.Search.objects.create(Search_value=search, Frequency=1)


def Walmart(request):
    search = request.POST.get('search').capitalize()
    if search != '' and search is not None and search != 'None':
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

                if soup.find('h1', class_=['prod-ProductTitle', 'font-normal']) and soup.find('span', class_='price-group'):
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
                        if models.Product.objects.filter(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image):
                            continue
                        else:
                            models.Product.objects.filter(Search=search, Name=name, Link=link).update(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)
                    else:
                        models.Product.objects.update_or_create(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)


def Hollister(request):
    search = request.POST.get('search').capitalize()
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
            for link in soup.find_all('a', class_='product-card__name', href=True)[:2]:
                    product_links.append(base_url + link['href'])

        for link in product_links:
            r = requests.get(link, headers=headers)

            soup2 = BeautifulSoup(r.content, 'lxml')

            if soup2.find('h1', class_=['product-title-component', 'product-title-main-header']) and soup2.find_all('span', class_=['product-price-text', 'product-price-font-size']):
                name = soup2.find('h1', class_=['product-title-component', 'product-title-main-header']).text.strip()
                if soup2.find_all('span', class_=['product-price-text', 'product-price-font-size'])[1]:
                    price = soup2.find_all('span', class_=['product-price-text', 'product-price-font-size'])[1].text
                else:
                    price = soup2.find('span', class_=['product-price-text', 'product-price-font-size']).text
                description = 'N/A'
                image = soup.find('img', alt=f'{name}').get('src')
                link = link
                seller = 'Hollister'

                if models.Product.objects.filter(Name=name, Link=link, Seller=seller):
                    if models.Product.objects.filter(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller):
                        continue
                    else:
                        models.Product.objects.filter(Search=search, Name=name, Link=link).update(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)
                else:
                    models.Product.objects.update_or_create(Search=search,  Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)


def Abercrombie(request):
    search = request.POST.get('search').capitalize()
    if search != '' and search is not None and search != 'None':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }

        BASE_URL = 'https://www.abercrombie.com/shop/us/search?departmentCategoryId=10000&searchTerm={}'
        base_url = 'https://www.abercrombie.com'
        final_url = BASE_URL.format(quote_plus(search))

        product_links = []
        r = requests.get(final_url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        if soup.find('a', class_=['product-card__name'], href=True):
            for link in soup.find_all('a', class_=['product-card__name'], href=True)[:2]:
                product_links.append(base_url + link['href'])

        for link in product_links:
            r = requests.get(link, headers=headers)

            soup2 = BeautifulSoup(r.content, 'lxml')

            if soup2.find('h1', class_=['product-title-component', 'product-title-main-header']) and soup2.find('span', class_=['product-price-text', 'product-price-font-size']):
                name = soup2.find('h1', class_=['product-title-component', 'product-title-main-header']).text.strip()
                if soup2.find_all('span', class_=['product-price-text', 'product-price-font-size'])[1]:
                    price = soup2.find_all('span', class_=['product-price-text', 'product-price-font-size'])[1].text
                else:
                    price = soup2.find('span', class_=['product-price-text', 'product-price-font-size']).text
                description = 'N/A'
                image = soup.find('img', alt=f'{name}').get('src')
                link = link
                seller = 'Abercrombie'

                if models.Product.objects.filter(Name=name, Link=link, Seller=seller):
                    if models.Product.objects.filter(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller):
                        continue
                    else:
                        models.Product.objects.filter(Search=search, Name=name, Link=link).update(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)
                else:
                    models.Product.objects.update_or_create(Search=search,  Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)


def CostCo(request):
    search = request.POST.get('search').capitalize()
    if search != '' and search is not None and search != 'None':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }

        BASE_URL = 'https://www.costco.com/CatalogSearch?dept=All&keyword={}'
        final_url = BASE_URL.format(quote_plus(search))

        r = requests.get(final_url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        if soup.find('div', class_=['product-tile-set']):
            for product in soup.find_all('div', class_=['product-tile-set'])[:2]:
                productlinks = []
                essential = product.find('p', class_=['description'])
                if essential.find('a') and product.find('div', class_=['price']):
                    name = essential.find('a').text
                    price = product.find('div', class_=['price']).text
                    link = essential.find('a').get('href')
                    productlinks.append(link)
                    image = product.find('img', class_=['img-responsive']).get('src')
                    seller = 'CostCo'

                    for link in productlinks:
                        r2 = requests.get(link, headers=headers)
                        soup2 = BeautifulSoup(r2.content, 'lxml')

                        if soup2.find('ul', class_=['pdp-features']):
                            description = soup2.find('ul', class_=['pdp-features']).text.strip()
                        else:
                            description = 'N/A'


                    if models.Product.objects.filter(Name=name, Link=link, Seller=seller):
                        if models.Product.objects.filter(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller):
                            continue
                        else:
                            models.Product.objects.filter(Search=search, Name=name, Link=link).update(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)
                    else:
                        models.Product.objects.update_or_create(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)


def HomeDepot(request):
    search = request.POST.get('search').capitalize()
    if search != '' and search is not None and search != 'None':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }

        BASE_URL = 'https://www.homedepot.com/s/{}'
        base_url = 'https://www.homedepot.com'
        final_url = BASE_URL.format(quote_plus(search))

        productlinks = []
        r = requests.get(final_url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        if soup.find('div', class_=['pod-plp__description']):
            for idk in soup.find_all('div', class_=['pod-plp__description'])[:2]:
                link = idk.find('a', href=True).get('href')
                productlinks.append(base_url + link)


        for link in productlinks:
            r = requests.get(link, headers=headers)

            soup = BeautifulSoup(r.content, 'lxml')

            if soup.find('h1', class_=['product-title__title']) and soup.find('span', id=['ajaxPrice']):
                name = soup.find('h1', class_=['product-title__title']).text.strip()
                price = soup.find('span', id=['ajaxPrice']).text.strip()
                image = soup.find('img', id=['mainImage']).get('src')
                if soup.find_all('div', class_=['buybox__salient-points hidden-xs-down']):
                    description2 = soup.find_all('div', class_=['buybox__salient-points hidden-xs-down'])
                    for d in description2:
                        description = d.find('ul').text
                else:
                    description = 'N/A'
                link = link
                seller = 'Home Depot'

                if models.Product.objects.filter(Name=name, Link=link, Seller=seller):
                    if models.Product.objects.filter(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller):
                        continue
                    else:
                        models.Product.objects.filter(Search=search, Name=name, Link=link).update(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)
                else:
                    models.Product.objects.update_or_create(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)


def SamsClub(request):
    search = request.POST.get('search').capitalize()
    if search != '' and search is not None and search != 'None':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }

        BASE_URL = 'https://www.samsclub.com/s/{}'
        base_url = 'https://www.samsclub.com/'
        final_url = BASE_URL.format(quote_plus(search))

        productlinks = []
        r = requests.get(final_url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        if soup.find('div', class_=['sc-product-card', 'sc-product-card-grid', 'sc-product-card-has-flag']):
            for item in soup.find_all('div', class_=['sc-product-card', 'sc-product-card-grid', 'sc-product-card-has-flag'])[0:2]:
                if item.find('div', class_=['sc-product-card-title']) and item.find('span', class_=['Price-group']):
                    name = item.find('div', class_=['sc-product-card-title']).text
                    link = (base_url + item.find('a', class_=['sc-product-card-pdp-link']).get('href'))
                    productlinks.append(link)
                    image = item.find('img', class_=['sc-product-card-image']).get('src')
                    price = item.find('span', class_=['Price-group']).get('title')[15:]
                    seller = "Sam's Club"

                    for link in productlinks:
                        r2 = requests.get(link, headers=headers)
                        soup2 = BeautifulSoup(r2.content, 'lxml')

                        if soup2.find('div', class_=['sc-short-description']):
                            description = soup2.find('div', class_=['sc-short-description']).text.strip()
                        else:
                            description = 'N/A'

                    if models.Product.objects.filter(Name=name, Link=link, Seller=seller):
                        if models.Product.objects.filter(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller):
                            continue
                        else:
                            models.Product.objects.filter(Search=search, Name=name, Link=link).update(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)
                    else:
                        models.Product.objects.update_or_create(Search=search, Name=name, Price=price, Description=description, Link=link, Image=image, Seller=seller)