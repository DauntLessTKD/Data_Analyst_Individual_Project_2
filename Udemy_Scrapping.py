import requests
import pandas as pd
from bs4 import BeautifulSoup


df_udemy = pd.read_csv('CSV/udemy_courses.csv')

web_list = df_udemy['url'].to_list()

rating_list = []
language_list = []

for webpage in web_list:

    result = requests.get(webpage)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    language = soup.find('div', class_='clp-lead__element-item clp-lead__locale')

    if language is None:
        language_list.append('NoData')

    else:
        language_list.append(language.get_text().strip())

    rating = soup.find('span', class_='ud-heading-sm star-rating-module--rating-number--2xeHu')

    if rating is None:
        rating_list.append('NoData')

    else:
        rating_list.append(rating.get_text().strip())

df_udemy['language'] = language_list

df_udemy['rating'] = rating_list

df_udemy.to_csv('Udemy/udemy.csv', index=False)