import time
import requests
from bs4 import BeautifulSoup

url_999 = 'https://999.md/ru/list/transport/cars?query={query}&sort_type=date_desc&page={page_nr}'


def get_soup_for_query(query, nr_of_pages=None):
    for a in range(nr_of_pages):
        time.sleep(5)
        response = requests.get(
            url_999.format(query=query, page_nr=a + 1),
            headers={
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
        )
        yield BeautifulSoup(response.content)


def get_soup_for_link(link):
    response = requests.get(link)
    return BeautifulSoup(response.content)


def get_data_for_element(element, relevant_keyword):
    try:
        if element.find('i', {'class': 'figure--booster'}):
            return None
        image_url = element.find('div', {'class': 'ads-list-photo-item-thumb'}).find('img').get('src')
        ad_title = element.find('div', {'class': 'ads-list-photo-item-title'}).find('a').text
        ad_link = f"https://999.md{element.find('div', {'class': 'ads-list-photo-item-title'}).find('a').get('href')}"
        title, year = ad_title.split(',')
        if relevant_keyword.lower() not in title.lower():
            return None
        price = element.find('div', {'class': 'ads-list-photo-item-price'}).find('span').text
        ad_soup = get_soup_for_link(ad_link)
        user_data = get_user_data_from_soup(ad_soup)
        seller_profile_soup = get_soup_for_link(user_data["link"])
        seller_rating = get_seller_rating_from_soup(seller_profile_soup)

        return dict(
            img_url=image_url,
            title=title,
            year=year,
            price=price,
            ad_link=ad_link,
            username=user_data["name"],
            user_link=user_data["link"],
            seller_rating=seller_rating
        )

    except Exception as ex:
        print(ex)
        return None


def get_data_from_soup(soup: BeautifulSoup, query):
    elements = soup.find_all('li', {'class': 'ads-list-photo-item'})
    data = []
    for eleme in elements:
        resl = get_data_for_element(eleme, query)
        if resl:
            data.append(resl)
    return data


def get_user_data_from_soup(soup):
    element = soup.find('a', {'class': 'adPage__aside__stats__owner__login'})
    element_link = f"https://999.md{element.get('href')}"
    element_name = element.text
    return dict(name=element_name, link=element_link)

def get_seller_rating_from_soup(soup):
    element = soup.find('div', {'class': 'rating'})
    if element:
        return float((element.text).replace(",","."))
    else:
        return None


def scrape_data(query, pages):
    all_data = []
    for element in get_soup_for_query(query, pages):
        all_data.extend(get_data_from_soup(element, query))
    import pandas as pd
    df = pd.DataFrame(all_data)
    df.to_excel('999.xlsx')


if __name__ == '__main__':
    scrape_data('BMW', 4)
