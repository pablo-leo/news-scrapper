from dateutil import parser
from news_scrapper.urls_scrapper import UrlsScrapper


class ElPaisUrlsScrapper(UrlsScrapper):

    NOT_INTERESTING_TOPICS = [
        'videos', 'opinion', 'noticias', 'eps', 'elcomidista', 'escaparate', 'babelia', 'ideas', 'elviajero', 'icon',
        'cultura', 'television', 'planeta-futuro', 'deportes', 'clima-y-medio-ambiente', 'ciencia', 'sociedad',
        'espana/un-futuro-cercano', 'juegos', 'gente', 'economia/si-lo-hubiera-sabido', 'elpais'
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def extract_urls(soup):
        articles = soup.find_all('article')
        references = [article.find('a')['href'] for article in articles]
        urls = []
        for reference in references:
            if reference.startswith('/'):
                urls.append(f'https://elpais.com{reference}')
            else:
                urls.append(reference)

        return urls

    def filter_urls(self, urls, main_url):
        root_filtered_urls = [url for url in urls if url.startswith(main_url)]
        topic_filtered_urls = []
        for url in root_filtered_urls:
            topic, subtopic = url.replace(main_url, '').split('/')[:2]
            try:
                parser.parse(subtopic)
            except:
                topic = f'{topic}/{subtopic}'

            topic_match = [t for t in self.NOT_INTERESTING_TOPICS if t in topic]
            if not len(topic_match):
                topic_filtered_urls.append(url)

        return topic_filtered_urls
