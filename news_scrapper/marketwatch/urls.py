from news_scrapper.urls_scrapper import UrlsScrapper


class MarketWatchUrlsScrapper(UrlsScrapper):

    NOT_INTERESTING_TOPICS = [
        'video', 'picks'
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def extract_urls(soup):
        articles = soup.find_all('h3', class_='article__headline')
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
            topic = url.replace(main_url, '').split('/')[0]
            if topic not in self.NOT_INTERESTING_TOPICS:
                topic_filtered_urls.append(url)

        return topic_filtered_urls
