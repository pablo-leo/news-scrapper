import pandas as pd
from scrapper import Scrapper


class ElMundoScrapper(Scrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def extract_title(soup):
        title = soup.find('h1', class_='ue-c-article__headline js-headline').text
        return title

    @staticmethod
    def extract_subtitle(soup):
        subtitle = soup.find('p', class_='ue-c-article__standfirst').text
        return subtitle

    @staticmethod
    def extract_author(soup):
        author = soup.find('div', class_='ue-c-article__byline-name').text.replace('\n', '')
        return author

    @staticmethod
    def extract_date(soup):
        date = soup.find('div', class_='ue-c-article__publishdate').time['datetime']
        date = pd.to_datetime(date)
        return date

    @staticmethod
    def extract_body(soup):
        body_paragraphs = soup.find('div', class_='ue-l-article__body ue-c-article__body').find_all('p')
        body = '\n'.join([body_p.text.strip() for body_p in body_paragraphs])
        return body
