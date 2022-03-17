from bs4 import BeautifulSoup
import requests

def get_soup_ad_link(ad_link):
    response = requests.get(ad_link)
    return BeautifulSoup(response.content)

link = "https://999.md/ru/75394442"
element = get_soup_ad_link(link).find('a', {'class': 'adPage__aside__stats__owner__login'})
element_link = f"https://999.md{element.get('href')}"
element_name = element.text
print(element)
print(element_link)
print(element_name)