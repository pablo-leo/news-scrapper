import re
from dateutil import parser
from news_scrapper.news_scrapper import NewsScrapper


class MarketWatchNewsScrapper(NewsScrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def extract_title(soup):
        title = soup.find('h1', class_='article__headline').text
        title = title.replace('\n', '').strip()
        return title

    @staticmethod
    def extract_subtitle(soup):
        subtitle = soup.find('h2', class_='article__subhead')
        if subtitle is not None:
            subtitle = subtitle.text.replace('\n', '').strip()
        return subtitle

    @staticmethod
    def extract_author(soup):
        author = soup.find('div', class_='byline article__byline')
        if author.a is not None:
            author = author.a.text
        elif author.text is not None:
            author = author.text
        elif author.find('h4').text is not None:
            author = author.find('h4').text
        return author

    @staticmethod
    def extract_date(soup):
        date = soup.find('time', class_='timestamp timestamp--pub')
        if date is not None:
            date = date.text
            date = date.replace('\n', '').strip()
            date = date.split('Published: ')[-1]
        else:
            date = soup.find('time', class_='timestamp timestamp--update').text
            date = date.replace('\n', '').strip()
            date = date.split('Updated: ')[-1]
        date = parser.parse(date).strftime('%Y-%m-%d %H:%M:%S')
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
