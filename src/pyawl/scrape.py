import pprint
import re
import requests
from bs4 import BeautifulSoup

def parse(amazon_id='3F9MA6OUOXDV6', amazon_country='de', reveal='all', sortorder='date-added'):
    '''
    :param amazon_id:
    :param amazon_country: shop top level domain
    :param reveal: all, unpurchased or purchased
    :param sortorder: priority, universal-title, universal-price,
                        universal-price-desc, last-updated, date-added
    :return:
    '''

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }

    url = 'http://www.amazon.{}/registry/wishlist/{}'.format(
        amazon_country, amazon_id)
    response = requests.get(url, headers=headers, params={'reveal': reveal, 'sort': sortorder, 'layout': 'standard'})
    soup = BeautifulSoup(response.text, 'html.parser')
    list = soup.find('div', class_='g-items-section')
    items = list.find_all('a', id=re.compile('^itemName_(.*)'))
    pprint.pprint(items)


if __name__ == '__main__':
    parse()