from urls_scrapper import UrlsScrapper


class ElMundoUrlsScrapper(UrlsScrapper):

    NOT_INTERESTING_TOPICS = [
        'ofertas-regalos', 'cultura', 'album', 'metropoli', 'podcasts', 'vida-sana', 'papel', 'blogs', 'opinion',
        'eventos'
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def extract_urls(soup):
        urls = soup.find_all('a', class_='ue-c-cover-content__link-whole-content')
        urls = [url['href'] for url in urls]

        return urls

    def filter_urls(self, urls, main_url):
        root_filtered_urls = [url for url in urls if url.startswith(main_url)]
        topic_filtered_urls = []
        for url in root_filtered_urls:
            topic = url.replace(main_url, '').split('/')[0]
            if topic not in self.NOT_INTERESTING_TOPICS:
                topic_filtered_urls.append(url)

        return topic_filtered_urls
