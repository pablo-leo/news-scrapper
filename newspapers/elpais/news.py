import pandas as pd
from news_scrapper import NewsScrapper


class ElPaisNewsScrapper(NewsScrapper):
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
        author = soup.find('div', class_='a_md_a')
        author = author.span.text if author.a is None else author.a.text
        return author

    @staticmethod
    def extract_date(soup):
        date = soup.find('time')
        date = date['data-date'] if date.a is None else date.a['data-date']
        date = pd.to_datetime(date).strftime('%Y-%m-%d %H:%M:%S')
        return date

    @staticmethod
    def extract_body(soup):
        body_frame = soup.find('div', class_='a_c clearfix')
        if body_frame is None:
            body_frame = soup.find('div', class_='a_c clearfix a_lib')
        body_paragraphs = body_frame.find_all('p')
        body = '\n'.join([body_p.text for body_p in body_paragraphs])
        return body
