import pandas as pd
from scrapper import Scrapper


class ElPaisScrapper(Scrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def extract_title(soup):
        title = soup.find('h1', class_='a_t').text
        return title

    @staticmethod
    def extract_subtitle(soup):
        subtitle = soup.find('h2', class_='a_st').text
        return subtitle

    @staticmethod
    def extract_author(soup):
        author = soup.find('div', class_='a_md_a').a.text
        return author

    @staticmethod
    def extract_date(soup):
        date = soup.find('div', class_='a_md_f').time.a['data-date']
        date = pd.to_datetime(date)
        return date

    @staticmethod
    def extract_body(soup):
        body_paragraphs = soup.find('div', class_='a_c clearfix').find_all('p')
        body = '\n'.join([body_p.text for body_p in body_paragraphs])
        return body
