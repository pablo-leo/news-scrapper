import re
import pandas as pd
from scrapper import Scrapper


class MarketWatchScrapper(Scrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def extract_title(soup):
        title = soup.find('h1', class_='article__headline').text
        title = title.replace('\n', '').strip()
        return title

    @staticmethod
    def extract_subtitle(soup):
        subtitle = soup.find('h2', class_='article__subhead').text
        subtitle = subtitle.replace('\n', '').strip()
        return subtitle

    @staticmethod
    def extract_author(soup):
        author = soup.find('div', class_='byline article__byline').a.text
        return author

    @staticmethod
    def extract_date(soup):
        date = soup.find('time', class_='timestamp timestamp--pub').text
        date = date.replace('\n', '').strip()
        date = date.split('Published: ')[-1]
        date = pd.to_datetime(date).strftime('%Y-%m-%d %H:%M:%S')
        return date

    @staticmethod
    def extract_body(soup):
        body_paragraphs = soup.find('div', class_='column column--full article__content').find_all('p')
        body = []
        for body_p in body_paragraphs:
            body_p_text = body_p.text.replace('\n', ' ')
            body.append(re.sub(' +', ' ', body_p_text))
        body = '\n'.join(body)
        return body
